# the Gams generator script is responsible for generating structured reasoning chains and executable GAMS code.

from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
import re
import random

@dataclass
class GenerationResult:
    success: bool
    reasoning: str
    gams_code: str
    problem_type: str
    confidence: float
    error_message: str = ""

class GAMSGenerator:
    """
    The generator which creates the Chain-of-Thought reasoning and also GAMS code
    for all optimization problem types
    """
    
    def __init__(self):
        self.problem_templates = self._initialize_templates()
        self.reasoning_templates = self._initialize_reasoning_templates()
        
    def _initialize_templates(self) -> Dict[str, Dict]:
        """Initialize GAMS code templates for all problem types"""
        return {
            "transport": {
                "description": "Transportation problem with supply, demand, and cost minimization",
                "template": """Sets
    i   supply nodes    / {supply_nodes} /
    j   demand nodes    / {demand_nodes} /;

Parameters
    a(i)    capacity of supply node i
        / {supply_data} /
    b(j)    demand at node j  
        / {demand_data} /
    c(i,j)  transportation cost from i to j
        / {cost_data} /;

Variables
    x(i,j)  shipment quantities from i to j
    z       total transportation cost;

Positive Variable x;

Equations
    cost        define objective function
    supply(i)   supply limit at node i
    demand(j)   demand satisfaction at node j;

cost ..        z =e= sum((i,j), c(i,j) * x(i,j));
supply(i) ..   sum(j, x(i,j)) =l= a(i);
demand(j) ..   sum(i, x(i,j)) =g= b(j);

Model transport /all/;
Solve transport using lp minimizing z;

display "Transportation Problem Solution";
display z.l, x.l;"""
            },
            
            "assignment": {
                "description": "Assignment problem with worker-task matching and cost minimization",
                "template": """Sets
    i   workers    / {workers} /
    j   tasks      / {tasks} /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / {cost_data} /;

Variables
    x(i,j)  assignment of worker i to task j
    z       total assignment cost;

Binary Variable x;

Equations
    cost        define objective function
    worker(i)   each worker assigned to one task
    task(j)     each task assigned to one worker;

cost ..        z =e= sum((i,j), c(i,j) * x(i,j));
worker(i) ..   sum(j, x(i,j)) =e= 1;
task(j) ..     sum(i, x(i,j)) =e= 1;

Model assignment /all/;
Solve assignment using mip minimizing z;

display "Assignment Problem Solution";
display z.l, x.l;"""
            },
            
            "knapsack": {
                "description": "Knapsack problem with item selection and value maximization",
                "template": """Sets
    i   items   / {items} /;

Parameters
    w(i)    weight of item i
        / {weight_data} /
    v(i)    value of item i
        / {value_data} /;

Scalar capacity / {capacity} /;

Variables
    x(i)    selection of item i
    z       total value;

Binary Variable x;

Equations
    objective
    weight_limit;

objective ..     z =e= sum(i, v(i) * x(i));
weight_limit ..  sum(i, w(i) * x(i)) =l= capacity;

Model knapsack /all/;
Solve knapsack using mip maximizing z;

display "Knapsack Problem Solution";
display z.l, x.l;"""
            },
            
            "facility_location": {
                "description": "Facility location problem with fixed costs and transportation",
                "template": """Sets
    i   facilities   / {facilities} /
    j   customers    / {customers} /;

Parameters
    f(i)    fixed cost of opening facility i
        / {fixed_costs} /
    cap(i)  capacity of facility i
        / {capacities} /
    d(j)    demand of customer j
        / {demands} /
    c(i,j)  transportation cost from facility i to customer j
        / {transport_costs} /;

Variables
    y(i)    whether to open facility i
    x(i,j)  shipment from facility i to customer j
    z       total cost;

Binary Variable y;
Positive Variable x;

Equations
    cost            total cost definition
    supply(i)       capacity constraint at facility i
    demand(j)       demand satisfaction for customer j
    facility_use(i,j)  only ship from open facilities;

cost ..        z =e= sum(i, f(i) * y(i)) + sum((i,j), c(i,j) * x(i,j));
supply(i) ..   sum(j, x(i,j)) =l= cap(i) * y(i);
demand(j) ..   sum(i, x(i,j)) =g= d(j);
facility_use(i,j) .. x(i,j) =l= cap(i) * y(i);

Model facility /all/;
Solve facility using mip minimizing z;

display "Facility Location Solution";
display z.l, y.l, x.l;"""
            },
            
            "generic_lp": {
                "description": "Generic linear programming problem with resource constraints",
                "template": """Sets
    i   products   / {products} /;

Parameters
    profit(i)   profit per unit of product i
        / {profit_data} /
    machine(i)  machine hours required per unit of product i
        / {machine_data} /
    labor(i)    labor hours required per unit of product i
        / {labor_data} /;

Scalars
    max_machine   maximum machine hours available / {max_machine} /
    max_labor     maximum labor hours available / {max_labor} /;

Variables
    x(i)    production quantity of product i
    z       total profit;

Positive Variable x;

Equations
    objective        total profit
    machine_limit   machine hours constraint
    labor_limit     labor hours constraint;

objective ..     z =e= sum(i, profit(i) * x(i));
machine_limit .. sum(i, machine(i) * x(i)) =l= max_machine;
labor_limit ..   sum(i, labor(i) * x(i)) =l= max_labor;

Model production /all/;
Solve production using lp maximizing z;

display "Production Planning Solution";
display z.l, x.l;"""
            }
        }
    
    def _initialize_reasoning_templates(self) -> Dict[str, str]:
        """Initialize Chain-of-Thought reasoning templates for all problem types"""
        return {
            "transport": """PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: {supply_nodes} (plants/factories)
- Demand nodes: {demand_nodes} (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: {supply_data_formatted}
- Demand requirements: {demand_data_formatted}  
- Transportation costs: {cost_data_formatted}

VARIABLES DECLARATION:
- x(i,j): shipment quantity from supply i to demand j
- z: total transportation cost (objective)

EQUATIONS FORMULATION:
1. Objective: minimize total cost = sum of (cost * shipment) for all routes
2. Supply constraints: total shipments from each supply ≤ capacity
3. Demand constraints: total shipments to each demand ≥ requirement

MATHEMATICAL STRUCTURE:
- Linear programming problem
- Flow conservation with capacity and demand bounds
- Balanced/Unbalanced: {balance_status}

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost""",

            "assignment": """PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: {workers} (available resources)
- Tasks: {tasks} (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: {cost_data_formatted} (cost of each worker-task assignment)

VARIABLES DECLARATION:
- x(i,j): binary variable for assignment (1 if worker i assigned to task j)
- z: total assignment cost (objective)

EQUATIONS FORMULATION:
1. Objective: minimize total assignment cost
2. Worker constraints: each worker assigned to exactly one task
3. Task constraints: each task assigned to exactly one worker

MATHEMATICAL STRUCTURE:
- Integer programming problem
- Perfect matching in bipartite graph
- Assignment problem specialization of transportation

SOLUTION APPROACH:
- Use MIP solver to find optimal assignment
- Ensure one-to-one matching between workers and tasks
- Minimize total assignment cost""",

            "knapsack": """PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: {items} (available items for selection)

PARAMETERS DEFINITION:
- Weights: {weight_data_formatted}
- Values: {value_data_formatted}  
- Capacity: {capacity} (maximum weight limit)

VARIABLES DECLARATION:
- x(i): binary variable for item selection (1 if item i selected)
- z: total value of selected items (objective)

EQUATIONS FORMULATION:
1. Objective: maximize total value of selected items
2. Capacity constraint: total weight of selected items ≤ capacity

MATHEMATICAL STRUCTURE:
- Integer programming problem
- 0-1 knapsack optimization
- Resource allocation with binary decisions

SOLUTION APPROACH:
- Use MIP solver to select optimal item combination
- Balance value maximization with weight constraint
- Binary selection decisions""",

            "facility_location": """PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: {facilities} (potential locations)
- Customers: {customers} (demand points)

PARAMETERS DEFINITION:
- Fixed costs: {fixed_costs_formatted} (cost to open each facility)
- Capacities: {capacities_formatted} (maximum output per facility)
- Customer demands: {demands_formatted}
- Transportation costs: {transport_costs_formatted}

VARIABLES DECLARATION:
- y(i): binary variable for facility opening
- x(i,j): continuous variable for shipments
- z: total cost (fixed + transportation)

EQUATIONS FORMULATION:
1. Objective: minimize total cost (fixed + transportation)
2. Supply constraints: shipments from facility ≤ capacity if open
3. Demand constraints: each customer demand satisfied
4. Logical constraints: only ship from open facilities

MATHEMATICAL STRUCTURE:
- Mixed-integer programming problem
- Fixed charge network design
- Capacity installation with flow distribution

SOLUTION APPROACH:
- Use MIP solver to decide facility openings
- Optimize transportation flows
- Balance fixed costs vs transportation costs""",

            "generic_lp": """PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: {products} (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: {profit_data_formatted}
- Machine requirements: {machine_data_formatted}
- Labor requirements: {labor_data_formatted}
- Resource limits: Machine hours: {max_machine}, Labor hours: {max_labor}

VARIABLES DECLARATION:
- x(i): production quantity of product i
- z: total profit (objective)

EQUATIONS FORMULATION:
1. Objective: maximize total profit
2. Machine constraint: total machine hours used ≤ available
3. Labor constraint: total labor hours used ≤ available

MATHEMATICAL STRUCTURE:
- Linear programming problem
- Resource allocation with continuous variables
- Multi-product optimization with shared resources

SOLUTION APPROACH:
- Use LP solver to find optimal production quantities
- Balance profit maximization with resource constraints
- Continuous production decisions"""
        }
    
    def generate_from_text_and_tables(self, problem_text: str, tables_data: Dict) -> GenerationResult:
        """
        Main generation function: Creates CoT reasoning and GAMS code
        
        Args:
            problem_text: Natural language problem description
            tables_data: Structured data in dictionary format
            
        Returns:
            GenerationResult with reasoning chain and GAMS code
        """
        try:
            #  Classify problem type
            problem_type = self._classify_problem_type(problem_text, tables_data)
            
            #  Extract and validate parameters
            extraction_result = self._extract_and_validate_parameters(problem_text, tables_data, problem_type)
            if not extraction_result["success"]:
                return GenerationResult(
                    success=False,
                    reasoning="",
                    gams_code="",
                    problem_type=problem_type,
                    confidence=0.0,
                    error_message=extraction_result["error"]
                )
            
            params = extraction_result["parameters"]
            
            #  Generate reasoning chain
            reasoning = self._generate_reasoning_chain(problem_type, params)
            
            #  Generate GAMS code
            gams_code = self._generate_gams_code(problem_type, params)
            
            #  Validate generation quality
            validation_result = self._validate_generation(gams_code, reasoning, problem_type)
            
            return GenerationResult(
                success=validation_result["valid"],
                reasoning=reasoning,
                gams_code=gams_code,
                problem_type=problem_type,
                confidence=validation_result["confidence"],
                error_message=validation_result.get("error", "")
            )
            
        except Exception as e:
            return GenerationResult(
                success=False,
                reasoning="",
                gams_code="",
                problem_type="unknown",
                confidence=0.0,
                error_message=f"Generation failed: {str(e)}"
            )
    
    def _classify_problem_type(self, problem_text: str, tables_data: Dict) -> str:
        """Classify problem type based on keywords and table structure"""
        text_lower = problem_text.lower()
        table_keys = set(tables_data.keys())
        
        # Check for specific table structures first
        if 'fixed_costs' in table_keys and 'transport_costs' in table_keys:
            return "facility_location"
        elif 'profit' in table_keys and 'machine_hours' in table_keys:
            return "generic_lp"
        elif 'items' in table_keys and 'weight' in next(iter(tables_data['items'].values())):
            return "knapsack"
        elif 'cost_matrix' in table_keys:
            return "assignment"
        elif 'supply' in table_keys and 'demand' in table_keys:
            return "transport"
        
        # Fallback to keyword-based classification
        transport_keywords = ['transport', 'ship', 'supply', 'demand', 'plant', 'factory', 'market']
        if any(keyword in text_lower for keyword in transport_keywords):
            return "transport"
        
        assignment_keywords = ['assign', 'worker', 'task', 'job', 'matching', 'crew', 'team']
        if any(keyword in text_lower for keyword in assignment_keywords):
            return "assignment"
        
        knapsack_keywords = ['knapsack', 'backpack', 'capacity', 'weight', 'value', 'select', 'choose', 'item']
        if any(keyword in text_lower for keyword in knapsack_keywords):
            return "knapsack"
        
        facility_keywords = ['facility', 'location', 'open', 'fixed cost', 'warehouse', 'distribution']
        if any(keyword in text_lower for keyword in facility_keywords):
            return "facility_location"
        
        # Default to generic LP
        return "generic_lp"
    
    def _extract_and_validate_parameters(self, problem_text: str, tables_data: Dict, problem_type: str) -> Dict:
        """Extract and validate parameters from text and tables"""
        
        if problem_type == "transport":
            return self._extract_transport_parameters(problem_text, tables_data)
        elif problem_type == "assignment":
            return self._extract_assignment_parameters(problem_text, tables_data)
        elif problem_type == "knapsack":
            return self._extract_knapsack_parameters(problem_text, tables_data)
        elif problem_type == "facility_location":
            return self._extract_facility_parameters(problem_text, tables_data)
        elif problem_type == "generic_lp":
            return self._extract_generic_lp_parameters(problem_text, tables_data)
        else:
            return {"success": False, "error": f"Unsupported problem type: {problem_type}"}
    
    def _extract_transport_parameters(self, problem_text: str, tables_data: Dict) -> Dict:
        """Extract parameters for transportation problems"""
        params = {}
        
        try:
            # Extract from tables
            if 'supply' in tables_data:
                supply_data = tables_data['supply']
                params['supply_nodes'] = ", ".join(supply_data.keys())
                params['supply_data'] = ", ".join([f"{k} {v}" for k, v in supply_data.items()])
                params['supply_data_formatted'] = self._format_parameter_display(supply_data)
            else:
                return {"success": False, "error": "Missing supply data in tables"}
            
            if 'demand' in tables_data:
                demand_data = tables_data['demand']
                params['demand_nodes'] = ", ".join(demand_data.keys())
                params['demand_data'] = ", ".join([f"{k} {v}" for k, v in demand_data.items()])
                params['demand_data_formatted'] = self._format_parameter_display(demand_data)
            else:
                return {"success": False, "error": "Missing demand data in tables"}
            
            if 'costs' in tables_data:
                cost_data = tables_data['costs']
                cost_strings = []
                for from_node, to_costs in cost_data.items():
                    for to_node, cost in to_costs.items():
                        cost_strings.append(f"{from_node}.{to_node} {cost}")
                params['cost_data'] = ", ".join(cost_strings)
                params['cost_data_formatted'] = self._format_cost_matrix(cost_data)
            else:
                return {"success": False, "error": "Missing cost data in tables"}
            
            # Calculate balance status
            total_supply = sum(tables_data['supply'].values())
            total_demand = sum(tables_data['demand'].values())
            if total_supply == total_demand:
                params['balance_status'] = "Balanced (total supply = total demand)"
            elif total_supply > total_demand:
                params['balance_status'] = f"Unbalanced (supply {total_supply} > demand {total_demand})"
            else:
                params['balance_status'] = f"Unbalanced (supply {total_supply} < demand {total_demand})"
            
            return {"success": True, "parameters": params}
            
        except Exception as e:
            return {"success": False, "error": f"Parameter extraction failed: {str(e)}"}
    
    def _extract_assignment_parameters(self, problem_text: str, tables_data: Dict) -> Dict:
        """Extract parameters for assignment problems"""
        params = {}
        
        try:
            if 'workers' in tables_data:
                workers = list(tables_data['workers'].keys())
                params['workers'] = ", ".join(workers)
            else:
                # Try to extract from cost matrix
                if 'cost_matrix' in tables_data:
                    workers = list(tables_data['cost_matrix'].keys())
                    params['workers'] = ", ".join(workers)
                else:
                    return {"success": False, "error": "Missing worker data in tables"}
            
            if 'tasks' in tables_data:
                tasks = list(tables_data['tasks'].keys())
                params['tasks'] = ", ".join(tasks)
            else:
                # Try to extract from cost matrix
                if 'cost_matrix' in tables_data:
                    first_worker = list(tables_data['cost_matrix'].keys())[0]
                    tasks = list(tables_data['cost_matrix'][first_worker].keys())
                    params['tasks'] = ", ".join(tasks)
                else:
                    return {"success": False, "error": "Missing task data in tables"}
            
            if 'cost_matrix' in tables_data:
                cost_data = tables_data['cost_matrix']
                cost_strings = []
                for worker, task_costs in cost_data.items():
                    for task, cost in task_costs.items():
                        cost_strings.append(f"{worker}.{task} {cost}")
                params['cost_data'] = ", ".join(cost_strings)
                params['cost_data_formatted'] = self._format_cost_matrix(cost_data)
            else:
                return {"success": False, "error": "Missing cost matrix in tables"}
            
            return {"success": True, "parameters": params}
            
        except Exception as e:
            return {"success": False, "error": f"Parameter extraction failed: {str(e)}"}
    
    def _extract_knapsack_parameters(self, problem_text: str, tables_data: Dict) -> Dict:
        """Extract parameters for knapsack problems"""
        params = {}
        
        try:
            if 'items' in tables_data:
                items_data = tables_data['items']
                params['items'] = ", ".join(items_data.keys())
                
                weights = []
                values = []
                for item, specs in items_data.items():
                    if 'weight' in specs:
                        weights.append(f"{item} {specs['weight']}")
                    if 'value' in specs:
                        values.append(f"{item} {specs['value']}")
                
                if weights:
                    params['weight_data'] = ", ".join(weights)
                    params['weight_data_formatted'] = self._format_parameter_display(
                        {k: v['weight'] for k, v in items_data.items() if 'weight' in v}
                    )
                else:
                    return {"success": False, "error": "Missing weight data in items"}
                
                if values:
                    params['value_data'] = ", ".join(values)
                    params['value_data_formatted'] = self._format_parameter_display(
                        {k: v['value'] for k, v in items_data.items() if 'value' in v}
                    )
                else:
                    return {"success": False, "error": "Missing value data in items"}
            else:
                return {"success": False, "error": "Missing items data in tables"}
            
            # Extract capacity from text or tables
            capacity_match = re.search(r'capacity\s*[=:]?\s*(\d+)', problem_text.lower())
            if capacity_match:
                params['capacity'] = capacity_match.group(1)
            elif 'capacity' in tables_data:
                params['capacity'] = str(tables_data['capacity'])
            else:
                # Default capacity based on total weight
                total_weight = sum(specs.get('weight', 0) for specs in items_data.values())
                params['capacity'] = str(int(total_weight * 0.6))  # 60% of total weight
            
            return {"success": True, "parameters": params}
            
        except Exception as e:
            return {"success": False, "error": f"Parameter extraction failed: {str(e)}"}
    
    def _extract_facility_parameters(self, problem_text: str, tables_data: Dict) -> Dict:
        """Extract parameters for facility location problems"""
        params = {}
        
        try:
            # Extract facilities
            if 'facilities' in tables_data:
                facilities_data = tables_data['facilities']
                params['facilities'] = ", ".join(facilities_data.keys())
            else:
                # Try to extract from fixed_costs
                if 'fixed_costs' in tables_data:
                    facilities = list(tables_data['fixed_costs'].keys())
                    params['facilities'] = ", ".join(facilities)
                else:
                    return {"success": False, "error": "Missing facilities data in tables"}
            
            # Extract customers
            if 'customers' in tables_data:
                customers_data = tables_data['customers']
                params['customers'] = ", ".join(customers_data.keys())
            else:
                # Try to extract from demands
                if 'demands' in tables_data:
                    customers = list(tables_data['demands'].keys())
                    params['customers'] = ", ".join(customers)
                else:
                    return {"success": False, "error": "Missing customers data in tables"}
            
            # Extract fixed costs
            if 'fixed_costs' in tables_data:
                fixed_costs = tables_data['fixed_costs']
                fixed_strings = [f"{k} {v}" for k, v in fixed_costs.items()]
                params['fixed_costs'] = ", ".join(fixed_strings)
                params['fixed_costs_formatted'] = self._format_parameter_display(fixed_costs)
            else:
                return {"success": False, "error": "Missing fixed_costs in tables"}
            
            # Extract capacities
            if 'capacities' in tables_data:
                capacities = tables_data['capacities']
                capacity_strings = [f"{k} {v}" for k, v in capacities.items()]
                params['capacities'] = ", ".join(capacity_strings)
                params['capacities_formatted'] = self._format_parameter_display(capacities)
            else:
                # Default capacities
                facilities = params['facilities'].split(', ')
                default_capacities = {facility: 500 + i*100 for i, facility in enumerate(facilities)}
                capacity_strings = [f"{k} {v}" for k, v in default_capacities.items()]
                params['capacities'] = ", ".join(capacity_strings)
                params['capacities_formatted'] = self._format_parameter_display(default_capacities)
            
            # Extract demands
            if 'demands' in tables_data:
                demands = tables_data['demands']
                demand_strings = [f"{k} {v}" for k, v in demands.items()]
                params['demands'] = ", ".join(demand_strings)
                params['demands_formatted'] = self._format_parameter_display(demands)
            else:
                return {"success": False, "error": "Missing demands in tables"}
            
            # Extract transport costs
            if 'transport_costs' in tables_data:
                transport_costs = tables_data['transport_costs']
                transport_strings = []
                for facility, customer_costs in transport_costs.items():
                    for customer, cost in customer_costs.items():
                        transport_strings.append(f"{facility}.{customer} {cost}")
                params['transport_costs'] = ", ".join(transport_strings)
                params['transport_costs_formatted'] = self._format_cost_matrix(transport_costs)
            else:
                return {"success": False, "error": "Missing transport_costs in tables"}
            
            return {"success": True, "parameters": params}
            
        except Exception as e:
            return {"success": False, "error": f"Parameter extraction failed: {str(e)}"}
    
    def _extract_generic_lp_parameters(self, problem_text: str, tables_data: Dict) -> Dict:
        """Extract parameters for generic LP problems"""
        params = {}
        
        try:
            # Extract products
            if 'products' in tables_data:
                products_data = tables_data['products']
                params['products'] = ", ".join(products_data.keys())
            else:
                # Try to extract from profit
                if 'profit' in tables_data:
                    products = list(tables_data['profit'].keys())
                    params['products'] = ", ".join(products)
                else:
                    return {"success": False, "error": "Missing products data in tables"}
            
            # Extract profit data
            if 'profit' in tables_data:
                profit_data = tables_data['profit']
                profit_strings = [f"{k} {v}" for k, v in profit_data.items()]
                params['profit_data'] = ", ".join(profit_strings)
                params['profit_data_formatted'] = self._format_parameter_display(profit_data)
            else:
                return {"success": False, "error": "Missing profit data in tables"}
            
            # Extract machine hours
            if 'machine_hours' in tables_data:
                machine_data = tables_data['machine_hours']
                machine_strings = [f"{k} {v}" for k, v in machine_data.items()]
                params['machine_data'] = ", ".join(machine_strings)
                params['machine_data_formatted'] = self._format_parameter_display(machine_data)
            else:
                return {"success": False, "error": "Missing machine_hours in tables"}
            
            # Extract labor hours
            if 'labor_hours' in tables_data:
                labor_data = tables_data['labor_hours']
                labor_strings = [f"{k} {v}" for k, v in labor_data.items()]
                params['labor_data'] = ", ".join(labor_strings)
                params['labor_data_formatted'] = self._format_parameter_display(labor_data)
            else:
                return {"success": False, "error": "Missing labor_hours in tables"}
            
            # Extract resource limits
            if 'max_machine_hours' in tables_data:
                params['max_machine'] = str(tables_data['max_machine_hours'])
            else:
                params['max_machine'] = "100"  # Default
            
            if 'max_labor_hours' in tables_data:
                params['max_labor'] = str(tables_data['max_labor_hours'])
            else:
                params['max_labor'] = "120"  # Default
            
            return {"success": True, "parameters": params}
            
        except Exception as e:
            return {"success": False, "error": f"Parameter extraction failed: {str(e)}"}
    
    def _generate_reasoning_chain(self, problem_type: str, params: Dict) -> str:
        """Generate structured Chain-of-Thought reasoning"""
        if problem_type in self.reasoning_templates:
            template = self.reasoning_templates[problem_type]
            try:
                return template.format(**params)
            except KeyError as e:
                return f"Reasoning generation incomplete. Missing parameter: {e}"
        else:
            return f"Reasoning template not available for problem type: {problem_type}"
    
    def _generate_gams_code(self, problem_type: str, params: Dict) -> str:
        """Generate GAMS code using templates"""
        if problem_type in self.problem_templates:
            template = self.problem_templates[problem_type]["template"]
            try:
                return template.format(**params)
            except KeyError as e:
                return f"* Error: Missing parameter for GAMS generation: {e}\n* Available parameters: {list(params.keys())}"
        else:
            return f"* Error: No template available for problem type: {problem_type}"
    
    def _validate_generation(self, gams_code: str, reasoning: str, problem_type: str) -> Dict:
        """Validate the quality of generated content"""
        validation = {
            "valid": True,
            "confidence": 0.8,
            "warnings": []
        }
        
        # Check GAMS code completeness
        required_sections = ["Sets", "Parameters", "Variables", "Equations", "Model", "Solve"]
        missing_sections = [section for section in required_sections if section not in gams_code]
        
        if missing_sections:
            validation["valid"] = False
            validation["confidence"] = 0.2
            validation["error"] = f"Missing GAMS sections: {missing_sections}"
            return validation
        
        # Check reasoning completeness
        if len(reasoning.strip()) < 100:
            validation["warnings"].append("Reasoning chain seems brief")
            validation["confidence"] *= 0.9
        
        # Check for error markers in GAMS code
        if "* Error:" in gams_code:
            validation["valid"] = False
            validation["confidence"] = 0.1
            validation["error"] = "GAMS code contains error markers"
            return validation
        
        # Problem-type specific validations
        if problem_type in ["assignment", "knapsack", "facility_location"]:
            if "Binary Variable" not in gams_code:
                validation["valid"] = False
                validation["confidence"] = 0.3
                validation["error"] = "Binary variables missing for integer problem"
                return validation
        
        return validation
    
    def _format_parameter_display(self, data: Dict) -> str:
        """Format parameter data for display in reasoning"""
        if not data:
            return "No data"
        items = [f"{k}: {v}" for k, v in data.items()]
        return "; ".join(items)
    
    def _format_cost_matrix(self, cost_matrix: Dict) -> str:
        """Format cost matrix for display in reasoning"""
        if not cost_matrix:
            return "No cost data"
        
        lines = []
        for from_item, to_costs in cost_matrix.items():
            cost_strings = [f"{to}: {cost}" for to, cost in to_costs.items()]
            lines.append(f"{from_item} -> {', '.join(cost_strings)}")
        
        return "; ".join(lines)


# Test function to demonstrate the generator
def test_generator():
    """Test the GAMS generator with all problem types"""
    print("COMPLETE GAMS GENERATOR TEST")
    print("=" * 60)
    
    generator = GAMSGenerator()
    
    # Test cases for all problem types
    test_cases = [
        {
            "name": "Transport Problem",
            "text": "A company needs to transport goods from plants to markets. Minimize transportation cost.",
            "tables": {
                "supply": {"plant1": 350, "plant2": 600},
                "demand": {"market1": 325, "market2": 300, "market3": 275},
                "costs": {
                    "plant1": {"market1": 2.5, "market2": 1.7, "market3": 1.8},
                    "plant2": {"market1": 2.5, "market2": 1.8, "market3": 1.4}
                }
            }
        },
        {
            "name": "Assignment Problem",
            "text": "Assign workers to tasks to minimize total assignment cost.",
            "tables": {
                "cost_matrix": {
                    "w1": {"t1": 10, "t2": 12, "t3": 15},
                    "w2": {"t1": 8, "t2": 11, "t3": 13},
                    "w3": {"t1": 9, "t2": 14, "t3": 10}
                }
            }
        },
        {
            "name": "Knapsack Problem", 
            "text": "Select items for a knapsack with capacity 50 to maximize total value.",
            "tables": {
                "items": {
                    "item1": {"weight": 10, "value": 20},
                    "item2": {"weight": 20, "value": 30},
                    "item3": {"weight": 30, "value": 40},
                    "item4": {"weight": 40, "value": 50}
                }
            }
        },
        {
            "name": "Facility Location Problem",
            "text": "Decide which facilities to open to serve customers at minimum cost.",
            "tables": {
                "fixed_costs": {"f1": 1000, "f2": 1500, "f3": 1200},
                "capacities": {"f1": 500, "f2": 700, "f3": 600},
                "demands": {"c1": 200, "c2": 300, "c3": 250, "c4": 350},
                "transport_costs": {
                    "f1": {"c1": 10, "c2": 15, "c3": 12, "c4": 18},
                    "f2": {"c1": 14, "c2": 11, "c3": 16, "c4": 13},
                    "f3": {"c1": 17, "c2": 13, "c3": 14, "c4": 11}
                }
            }
        },
        {
            "name": "Generic LP Problem",
            "text": "Decide production levels to maximize profit subject to resource limits.",
            "tables": {
                "profit": {"p1": 25, "p2": 30, "p3": 20},
                "machine_hours": {"p1": 2, "p2": 3, "p3": 1},
                "labor_hours": {"p1": 4, "p2": 3, "p3": 2},
                "max_machine_hours": 100,
                "max_labor_hours": 120
            }
        }
    ]
    
    for test_case in test_cases:
        print(f"\nTESTING: {test_case['name']}")
        print("-" * 40)
        
        result = generator.generate_from_text_and_tables(
            test_case["text"],
            test_case["tables"]
        )
        
        print(f"Success: {result.success}")
        print(f"Problem Type: {result.problem_type}")
        print(f"Confidence: {result.confidence:.2f}")
        
        if result.error_message:
            print(f"Error: {result.error_message}")
        
        print(f"Reasoning Length: {len(result.reasoning)} chars")
        print(f"GAMS Code Length: {len(result.gams_code)} chars")
        
        print("\n" + "="*50)

if __name__ == "__main__":
    test_generator()