from typing import Dict, List, Optional, Any
import random
import json
from dataclasses import dataclass
from generator import GAMSGenerator, GenerationResult

@dataclass
class CorpusProblem:
    id: str
    problem_type: str
    text_description: str
    tables: Dict[str, Any]
    reasoning: str = ""
    gams_code: str = ""
    verified: bool = False
    objective_value: Optional[float] = None

class CorpusGenerator:
    """
    Generates a diverse corpus of optimization problems with variations
    """
    
    def __init__(self):
        self.generator = GAMSGenerator()
        self.problem_seeds = self._initialize_problem_seeds()
        
    def _initialize_problem_seeds(self) -> Dict[str, List[Dict]]:
        """Initialize seed problems for each problem type"""
        return {
            "transport": [
                {
                    "base_text": "A manufacturing company needs to transport products from {supply_nodes} to {demand_nodes}. Minimize total transportation cost while satisfying supply capacities and demand requirements.",
                    "base_tables": {
                        "supply": {"plant1": 350, "plant2": 600},
                        "demand": {"market1": 325, "market2": 300, "market3": 275},
                        "costs": {
                            "plant1": {"market1": 2.5, "market2": 1.7, "market3": 1.8},
                            "plant2": {"market1": 2.5, "market2": 1.8, "market3": 1.4}
                        }
                    },
                    "variations": {
                        "supply_nodes": [
                            ["plant1", "plant2"],
                            ["factory_A", "factory_B", "factory_C"],
                            ["plant_east", "plant_west"],
                            ["facility_1", "facility_2"]
                        ],
                        "demand_nodes": [
                            ["market1", "market2", "market3"],
                            ["region_1", "region_2", "region_3"],
                            ["city_A", "city_B", "city_C"],
                            ["warehouse_1", "warehouse_2"]
                        ]
                    }
                }
            ],
            
            "assignment": [
                {
                    "base_text": "Assign {workers} to {tasks} to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.",
                    "base_tables": {
                        "cost_matrix": {
                            "w1": {"t1": 10, "t2": 12, "t3": 15},
                            "w2": {"t1": 8, "t2": 11, "t3": 13},
                            "w3": {"t1": 9, "t2": 14, "t3": 10}
                        }
                    },
                    "variations": {
                        "workers": [
                            ["w1", "w2", "w3"],
                            ["worker_A", "worker_B", "worker_C"],
                            ["employee_1", "employee_2", "employee_3"]
                        ],
                        "tasks": [
                            ["t1", "t2", "t3"],
                            ["job_1", "job_2", "job_3"],
                            ["task_alpha", "task_beta", "task_gamma"]
                        ]
                    }
                }
            ],
            
            "knapsack": [
                {
                    "base_text": "Select items from {items} for a knapsack with capacity {capacity} to maximize total value without exceeding the weight limit.",
                    "base_tables": {
                        "items": {
                            "item1": {"weight": 10, "value": 20},
                            "item2": {"weight": 20, "value": 30},
                            "item3": {"weight": 30, "value": 40},
                            "item4": {"weight": 40, "value": 50}
                        }
                    },
                    "variations": {
                        "items": [
                            ["item1", "item2", "item3", "item4"],
                            ["book", "laptop", "camera", "phone"],
                            ["tool_A", "tool_B", "tool_C", "tool_D"]
                        ],
                        "capacity": [50, 60, 70, 80]
                    }
                }
            ],
            
            "facility_location": [
                {
                    "base_text": "Decide which facilities from {facilities} to open to serve customers at {customers} at minimum cost, considering fixed costs and transport costs.",
                    "base_tables": {
                        "fixed_costs": {"f1": 1000, "f2": 1500, "f3": 1200},
                        "capacities": {"f1": 500, "f2": 700, "f3": 600},
                        "demands": {"c1": 200, "c2": 300, "c3": 250, "c4": 350},
                        "transport_costs": {
                            "f1": {"c1": 10, "c2": 15, "c3": 12, "c4": 18},
                            "f2": {"c1": 14, "c2": 11, "c3": 16, "c4": 13},
                            "f3": {"c1": 17, "c2": 13, "c3": 14, "c4": 11}
                        }
                    },
                    "variations": {
                        "facilities": [
                            ["f1", "f2", "f3"],
                            ["plant_A", "plant_B", "plant_C"],
                            ["hub_1", "hub_2", "hub_3"]
                        ],
                        "customers": [
                            ["c1", "c2", "c3", "c4"],
                            ["city_1", "city_2", "city_3"],
                            ["region_A", "region_B", "region_C"]
                        ]
                    }
                }
            ],
            
            "generic_lp": [
                {
                    "base_text": "Decide production levels of {products} to maximize profit subject to machine and labor capacity limits.",
                    "base_tables": {
                        "profit": {"p1": 25, "p2": 30, "p3": 20},
                        "machine_hours": {"p1": 2, "p2": 3, "p3": 1},
                        "labor_hours": {"p1": 4, "p2": 3, "p3": 2},
                        "max_machine_hours": 100,
                        "max_labor_hours": 120
                    },
                    "variations": {
                        "products": [
                            ["p1", "p2", "p3"],
                            ["product_A", "product_B", "product_C"],
                            ["item_X", "item_Y", "item_Z"]
                        ]
                    }
                }
            ]
        }
      
    def generate_corpus(self, 
                       total_problems: int = 30,
                       problem_distribution: Optional[Dict[str, float]] = None) -> List[CorpusProblem]:
        """
        Generate a diverse corpus of optimization problems
        """
        if problem_distribution is None:
            problem_distribution = {
                "transport": 0.25,
                "assignment": 0.25,
                "knapsack": 0.20,
                "facility_location": 0.20,
                "generic_lp": 0.10,
            }
        
        # Calculate number of problems per type
        problems_per_type = {}
        remaining = total_problems
        
        for prob_type, percentage in problem_distribution.items():
            count = int(total_problems * percentage)
            problems_per_type[prob_type] = count
            remaining -= count
        
        # Distribute remaining problems
        prob_types = list(problems_per_type.keys())
        for i in range(remaining):
            problems_per_type[prob_types[i % len(prob_types)]] += 1
        
        print(f"Generating corpus with distribution: {problems_per_type}")
        
        corpus = []
        problem_id = 1
        
        for prob_type, count in problems_per_type.items():
            print(f"Generating {count} {prob_type} problems...")
            
            for i in range(count):
                problem = self._generate_single_problem(prob_type, problem_id)
                if problem:
                    corpus.append(problem)
                    problem_id += 1
                else:
                    print(f"Failed to generate problem {problem_id} of type {prob_type}")
        
        print(f"Corpus generation complete: {len(corpus)} problems created")
        return corpus
    
    def _generate_single_problem(self, problem_type: str, problem_id: int) -> Optional[CorpusProblem]:
        """Generate a single problem with variations"""
        if problem_type not in self.problem_seeds:
            print(f"Unknown problem type: {problem_type}")
            return None
        
        # Select a random seed for this problem type
        seed = random.choice(self.problem_seeds[problem_type])
        
        # Apply variations
        varied_text, varied_tables = self._apply_variations(seed, problem_type)
        
        if not varied_text or not varied_tables:
            print(f"Variation failed for problem type: {problem_type}")
            return None
        
        # Generate CoT and GAMS code
        gen_result = self.generator.generate_from_text_and_tables(varied_text, varied_tables)
        
        if not gen_result.success:
            print(f"Generation failed for problem {problem_id}: {gen_result.error_message}")
            return None
        
        return CorpusProblem(
            id=f"prob_{problem_id:03d}",
            problem_type=problem_type,
            text_description=varied_text,
            tables=varied_tables,
            reasoning=gen_result.reasoning,
            gams_code=gen_result.gams_code,
            verified=False,
            objective_value=None
        )
    
    def _apply_variations(self, seed: Dict, problem_type: str) -> tuple:
        """Apply variations to create diverse problem instances"""
        base_text = seed["base_text"]
        base_tables = self._deep_copy_tables(seed["base_tables"])
        variations = seed.get("variations", {})
        
        try:
            if problem_type == "transport":
                return self._apply_transport_variations(base_text, base_tables, variations)
            elif problem_type == "assignment":
                return self._apply_assignment_variations(base_text, base_tables, variations)
            elif problem_type == "knapsack":
                return self._apply_knapsack_variations(base_text, base_tables, variations)
            elif problem_type == "facility_location":
                return self._apply_facility_location_variations(base_text, base_tables, variations)
            elif problem_type == "generic_lp":
                return self._apply_generic_lp_variations(base_text, base_tables, variations)
            else:
                return base_text, base_tables
                
        except Exception as e:
            print(f"Error applying variations for {problem_type}: {e}")
            return base_text, base_tables
    
    def _apply_transport_variations(self, base_text: str, base_tables: Dict, variations: Dict) -> tuple:
        """Apply variations for transport problems"""
        supply_nodes = random.choice(variations["supply_nodes"])
        demand_nodes = random.choice(variations["demand_nodes"])
        
        # Format text with node names
        final_text = base_text.format(
            supply_nodes=", ".join(supply_nodes[:-1]) + " and " + supply_nodes[-1],
            demand_nodes=", ".join(demand_nodes[:-1]) + " and " + demand_nodes[-1]
        )
        
        # Create new supply data - use original values with variation
        original_supply_values = list(base_tables["supply"].values())
        new_supply = {}
        for i, node in enumerate(supply_nodes):
            if i < len(original_supply_values):
                new_supply[node] = self._vary_value(original_supply_values[i], 0.3)
            else:
                # If more nodes than original, use average of existing values
                avg_value = sum(original_supply_values) / len(original_supply_values)
                new_supply[node] = self._vary_value(avg_value, 0.4)
        
        # Create new demand data
        original_demand_values = list(base_tables["demand"].values())
        new_demand = {}
        for i, node in enumerate(demand_nodes):
            if i < len(original_demand_values):
                new_demand[node] = self._vary_value(original_demand_values[i], 0.3)
            else:
                avg_value = sum(original_demand_values) / len(original_demand_values)
                new_demand[node] = self._vary_value(avg_value, 0.4)
        
        # Create new cost matrix
        original_costs = base_tables["costs"]
        original_supply_keys = list(original_costs.keys())
        original_demand_keys = list(original_costs[original_supply_keys[0]].keys())
        
        new_costs = {}
        for i, supply_node in enumerate(supply_nodes):
            new_costs[supply_node] = {}
            original_supply_idx = i % len(original_supply_keys)
            
            for j, demand_node in enumerate(demand_nodes):
                original_demand_idx = j % len(original_demand_keys)
                original_cost = original_costs[original_supply_keys[original_supply_idx]][original_demand_keys[original_demand_idx]]
                new_costs[supply_node][demand_node] = self._vary_value(original_cost, 0.2)
        
        base_tables["supply"] = new_supply
        base_tables["demand"] = new_demand
        base_tables["costs"] = new_costs
        
        return final_text, base_tables
    
    def _apply_assignment_variations(self, base_text: str, base_tables: Dict, variations: Dict) -> tuple:
        """Apply variations for assignment problems"""
        workers = random.choice(variations["workers"])
        tasks = random.choice(variations["tasks"])
        
        # Format text
        final_text = base_text.format(
            workers=", ".join(workers[:-1]) + " and " + workers[-1],
            tasks=", ".join(tasks[:-1]) + " and " + tasks[-1]
        )
        
        # Create new cost matrix
        original_costs = base_tables["cost_matrix"]
        original_worker_keys = list(original_costs.keys())
        original_task_keys = list(original_costs[original_worker_keys[0]].keys())
        
        new_cost_matrix = {}
        for i, worker in enumerate(workers):
            new_cost_matrix[worker] = {}
            original_worker_idx = i % len(original_worker_keys)
            
            for j, task in enumerate(tasks):
                original_task_idx = j % len(original_task_keys)
                original_cost = original_costs[original_worker_keys[original_worker_idx]][original_task_keys[original_task_idx]]
                new_cost_matrix[worker][task] = self._vary_value(original_cost, 0.25)
        
        base_tables["cost_matrix"] = new_cost_matrix
        return final_text, base_tables
    
    def _apply_knapsack_variations(self, base_text: str, base_tables: Dict, variations: Dict) -> tuple:
        """Apply variations for knapsack problems"""
        items = random.choice(variations["items"])
        capacity = random.choice(variations["capacity"])
        
        # Format text
        final_text = base_text.format(
            items=", ".join(items[:-1]) + " and " + items[-1],
            capacity=capacity
        )
        
        # Create new items table
        original_items = base_tables["items"]
        original_item_keys = list(original_items.keys())
        
        new_items = {}
        for i, item in enumerate(items):
            original_item_idx = i % len(original_item_keys)
            original_specs = original_items[original_item_keys[original_item_idx]]
            
            new_items[item] = {
                "weight": self._vary_value(original_specs["weight"], 0.3),
                "value": self._vary_value(original_specs["value"], 0.4)
            }
        
        base_tables["items"] = new_items
        return final_text, base_tables
    
    def _apply_facility_location_variations(self, base_text: str, base_tables: Dict, variations: Dict) -> tuple:
        """Apply variations for facility location problems"""
        facilities = random.choice(variations["facilities"])
        customers = random.choice(variations["customers"])
        
        final_text = base_text.format(
            facilities=", ".join(facilities[:-1]) + " and " + facilities[-1],
            customers=", ".join(customers[:-1]) + " and " + customers[-1]
        )
        
        # Vary fixed costs and capacities
        new_fixed_costs = {}
        new_capacities = {}
        for i, facility in enumerate(facilities):
            new_fixed_costs[facility] = self._vary_value(1000 + i*200, 0.3)
            new_capacities[facility] = self._vary_value(500 + i*100, 0.4)
        
        base_tables["fixed_costs"] = new_fixed_costs
        base_tables["capacities"] = new_capacities
        
        # Vary demands
        new_demands = {}
        for i, customer in enumerate(customers):
            new_demands[customer] = self._vary_value(200 + i*50, 0.3)
        base_tables["demands"] = new_demands
        
        # Create new transport cost matrix
        new_costs = {}
        for facility in facilities:
            new_costs[facility] = {}
            for customer in customers:
                new_costs[facility][customer] = self._vary_value(15, 0.4)
        base_tables["transport_costs"] = new_costs
        
        return final_text, base_tables
    
    def _apply_generic_lp_variations(self, base_text: str, base_tables: Dict, variations: Dict) -> tuple:
        """Apply variations for generic LP problems"""
        products = random.choice(variations["products"])
        
        final_text = base_text.format(
            products=", ".join(products[:-1]) + " and " + products[-1]
        )
        
        # Adjust profit and resource parameters
        new_profit = {p: self._vary_value(25 + i*5, 0.3) for i, p in enumerate(products)}
        new_machine = {p: self._vary_value(2 + i, 0.2) for i, p in enumerate(products)}
        new_labor = {p: self._vary_value(3 + i, 0.2) for i, p in enumerate(products)}
        
        base_tables["profit"] = new_profit
        base_tables["machine_hours"] = new_machine
        base_tables["labor_hours"] = new_labor
        base_tables["max_machine_hours"] = self._vary_value(100, 0.1)
        base_tables["max_labor_hours"] = self._vary_value(120, 0.1)
        
        return final_text, base_tables
    
    def _deep_copy_tables(self, tables: Dict) -> Dict:
        """Create a deep copy of tables dictionary"""
        if isinstance(tables, dict):
            return {k: self._deep_copy_tables(v) for k, v in tables.items()}
        elif isinstance(tables, list):
            return [self._deep_copy_tables(v) for v in tables]
        else:
            return tables
    
    def _vary_value(self, base_value: float, variation_factor: float) -> int:
        """Apply random variation to a value while keeping it reasonable"""
        variation = random.uniform(-variation_factor, variation_factor)
        new_value = base_value * (1 + variation)
        return max(1, int(round(new_value)))  # Ensure positive integer values
    
    def save_corpus(self, corpus: List[CorpusProblem], filename: str):
        """Save corpus to JSON file"""
        corpus_dict = []
        for problem in corpus:
            problem_dict = {
                "id": problem.id,
                "problem_type": problem.problem_type,
                "text_description": problem.text_description,
                "tables": problem.tables,
                "reasoning": problem.reasoning,
                "gams_code": problem.gams_code,
                "verified": problem.verified,
                "objective_value": problem.objective_value
            }
            corpus_dict.append(problem_dict)
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(corpus_dict, f, indent=2, ensure_ascii=False)
        
        print(f"Corpus saved to {filename} with {len(corpus)} problems")
    
    def load_corpus(self, filename: str) -> List[CorpusProblem]:
        """Load corpus from JSON file"""
        with open(filename, 'r', encoding='utf-8') as f:
            corpus_dict = json.load(f)
        
        corpus = []
        for problem_dict in corpus_dict:
            problem = CorpusProblem(
                id=problem_dict["id"],
                problem_type=problem_dict["problem_type"],
                text_description=problem_dict["text_description"],
                tables=problem_dict["tables"],
                reasoning=problem_dict.get("reasoning", ""),
                gams_code=problem_dict.get("gams_code", ""),
                verified=problem_dict.get("verified", False),
                objective_value=problem_dict.get("objective_value")
            )
            corpus.append(problem)
        
        print(f"Corpus loaded from {filename} with {len(corpus)} problems")
        return corpus


def test_corpus_generator():
    """Test the corpus generator"""
    print(" CORPUS GENERATOR TEST")
    print("=" * 60)
    
    corpus_gen = CorpusGenerator()
    
    # Generate a test corpus with new problem types
    print("Generating test corpus with 10 problems...")
    corpus = corpus_gen.generate_corpus(total_problems=10)
    
    # Display summary
    type_count = {}
    for problem in corpus:
        prob_type = problem.problem_type
        type_count[prob_type] = type_count.get(prob_type, 0) + 1
    
    print(f"\nCorpus Summary:")
    print(f"Total problems: {len(corpus)}")
    print(f"Problem types: {type_count}")
    
    # Show sample problems from all types
    print(f"\nSample Problems:")
    shown_types = set()
    for i, problem in enumerate(corpus):
        if problem.problem_type not in shown_types:
            print(f"\n{i+1}. {problem.id} - {problem.problem_type}")
            print(f"   Text: {problem.text_description[:80]}...")
            print(f"   Tables keys: {list(problem.tables.keys())}")
            
            # Show sample data from tables
            if problem.tables:
                first_key = list(problem.tables.keys())[0]
                sample_data = list(problem.tables[first_key].items())[:2]  # First 2 items
                print(f"   Sample data: {sample_data}")
            
            print(f"   Reasoning length: {len(problem.reasoning)} chars")
            print(f"   GAMS code length: {len(problem.gams_code)} chars")
            shown_types.add(problem.problem_type)
        
        if len(shown_types) >= 5:  # Show one of each type
            break
    
    # Save corpus
    if corpus:
        corpus_gen.save_corpus(corpus, "test_corpus.json")
        
        # Test loading
        loaded_corpus = corpus_gen.load_corpus("test_corpus.json")
        print(f"\nVerified load: {len(loaded_corpus)} problems loaded successfully")
        
        # Show distribution of loaded corpus
        loaded_types = {}
        for problem in loaded_corpus:
            loaded_types[problem.problem_type] = loaded_types.get(problem.problem_type, 0) + 1
        print(f"Loaded corpus distribution: {loaded_types}")
    else:
        print("No problems generated - cannot save corpus")


if __name__ == "__main__":
    test_corpus_generator()