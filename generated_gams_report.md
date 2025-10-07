# Generated GAMS CoT Corpus Report

Total Problems: 200

## Problem prob_001 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 380
    - plant2: 522

- demand:
    - market1: 405
    - market2: 231
    - market3: 353

- costs:
    - plant1: {'market1': 3, 'market2': 2, 'market3': 2}
    - plant2: {'market1': 2, 'market2': 2, 'market3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 380; plant2: 522
- Demand requirements: market1: 405; market2: 231; market3: 353  
- Transportation costs: plant1 -> market1: 3, market2: 2, market3: 2; plant2 -> market1: 2, market2: 2, market3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 902 < demand 989)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / plant1 380, plant2 522 /
    b(j)    demand at node j  
        / market1 405, market2 231, market3 353 /
    c(i,j)  transportation cost from i to j
        / plant1.market1 3, plant1.market2 2, plant1.market3 2, plant2.market1 2, plant2.market2 2, plant2.market3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_002 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 280
    - factory_B: 437
    - factory_C: 595

- demand:
    - region_1: 363
    - region_2: 302
    - region_3: 354

- costs:
    - factory_A: {'region_1': 2, 'region_2': 2, 'region_3': 2}
    - factory_B: {'region_1': 3, 'region_2': 2, 'region_3': 1}
    - factory_C: {'region_1': 3, 'region_2': 2, 'region_3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 280; factory_B: 437; factory_C: 595
- Demand requirements: region_1: 363; region_2: 302; region_3: 354  
- Transportation costs: factory_A -> region_1: 2, region_2: 2, region_3: 2; factory_B -> region_1: 3, region_2: 2, region_3: 1; factory_C -> region_1: 3, region_2: 2, region_3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1312 > demand 1019)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 280, factory_B 437, factory_C 595 /
    b(j)    demand at node j  
        / region_1 363, region_2 302, region_3 354 /
    c(i,j)  transportation cost from i to j
        / factory_A.region_1 2, factory_A.region_2 2, factory_A.region_3 2, factory_B.region_1 3, factory_B.region_2 2, factory_B.region_3 1, factory_C.region_1 3, factory_C.region_2 2, factory_C.region_3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1767.0

---

## Problem prob_003 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 279
    - plant2: 607

- demand:
    - market1: 237
    - market2: 268
    - market3: 282

- costs:
    - plant1: {'market1': 2, 'market2': 2, 'market3': 2}
    - plant2: {'market1': 2, 'market2': 2, 'market3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 279; plant2: 607
- Demand requirements: market1: 237; market2: 268; market3: 282  
- Transportation costs: plant1 -> market1: 2, market2: 2, market3: 2; plant2 -> market1: 2, market2: 2, market3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 886 > demand 787)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / plant1 279, plant2 607 /
    b(j)    demand at node j  
        / market1 237, market2 268, market3 282 /
    c(i,j)  transportation cost from i to j
        / plant1.market1 2, plant1.market2 2, plant1.market3 2, plant2.market1 2, plant2.market2 2, plant2.market3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1292.0

---

## Problem prob_004 — Transport

**Description:** A manufacturing company needs to transport products from plant_east and plant_west to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant_east: 344
    - plant_west: 442

- demand:
    - warehouse_1: 321
    - warehouse_2: 361

- costs:
    - plant_east: {'warehouse_1': 2, 'warehouse_2': 2}
    - plant_west: {'warehouse_1': 3, 'warehouse_2': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant_east, plant_west (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant_east: 344; plant_west: 442
- Demand requirements: warehouse_1: 321; warehouse_2: 361  
- Transportation costs: plant_east -> warehouse_1: 2, warehouse_2: 2; plant_west -> warehouse_1: 3, warehouse_2: 2

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
- Balanced/Unbalanced: Unbalanced (supply 786 > demand 682)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant_east, plant_west /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / plant_east 344, plant_west 442 /
    b(j)    demand at node j  
        / warehouse_1 321, warehouse_2 361 /
    c(i,j)  transportation cost from i to j
        / plant_east.warehouse_1 2, plant_east.warehouse_2 2, plant_west.warehouse_1 3, plant_west.warehouse_2 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1364.0

---

## Problem prob_005 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 276
    - factory_B: 615
    - factory_C: 563

- demand:
    - city_A: 413
    - city_B: 276
    - city_C: 286

- costs:
    - factory_A: {'city_A': 2, 'city_B': 2, 'city_C': 2}
    - factory_B: {'city_A': 2, 'city_B': 2, 'city_C': 1}
    - factory_C: {'city_A': 2, 'city_B': 2, 'city_C': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 276; factory_B: 615; factory_C: 563
- Demand requirements: city_A: 413; city_B: 276; city_C: 286  
- Transportation costs: factory_A -> city_A: 2, city_B: 2, city_C: 2; factory_B -> city_A: 2, city_B: 2, city_C: 1; factory_C -> city_A: 2, city_B: 2, city_C: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1454 > demand 975)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 276, factory_B 615, factory_C 563 /
    b(j)    demand at node j  
        / city_A 413, city_B 276, city_C 286 /
    c(i,j)  transportation cost from i to j
        / factory_A.city_A 2, factory_A.city_B 2, factory_A.city_C 2, factory_B.city_A 2, factory_B.city_B 2, factory_B.city_C 1, factory_C.city_A 2, factory_C.city_B 2, factory_C.city_C 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1664.0

---

## Problem prob_006 — Transport

**Description:** A manufacturing company needs to transport products from plant_east and plant_west to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant_east: 270
    - plant_west: 582

- demand:
    - city_A: 368
    - city_B: 274
    - city_C: 328

- costs:
    - plant_east: {'city_A': 3, 'city_B': 2, 'city_C': 2}
    - plant_west: {'city_A': 2, 'city_B': 2, 'city_C': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant_east, plant_west (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant_east: 270; plant_west: 582
- Demand requirements: city_A: 368; city_B: 274; city_C: 328  
- Transportation costs: plant_east -> city_A: 3, city_B: 2, city_C: 2; plant_west -> city_A: 2, city_B: 2, city_C: 1

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
- Balanced/Unbalanced: Unbalanced (supply 852 < demand 970)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant_east, plant_west /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / plant_east 270, plant_west 582 /
    b(j)    demand at node j  
        / city_A 368, city_B 274, city_C 328 /
    c(i,j)  transportation cost from i to j
        / plant_east.city_A 3, plant_east.city_B 2, plant_east.city_C 2, plant_west.city_A 2, plant_west.city_B 2, plant_west.city_C 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_007 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 251
    - facility_2: 715

- demand:
    - market1: 230
    - market2: 273
    - market3: 267

- costs:
    - facility_1: {'market1': 3, 'market2': 2, 'market3': 2}
    - facility_2: {'market1': 2, 'market2': 2, 'market3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 251; facility_2: 715
- Demand requirements: market1: 230; market2: 273; market3: 267  
- Transportation costs: facility_1 -> market1: 3, market2: 2, market3: 2; facility_2 -> market1: 2, market2: 2, market3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 966 > demand 770)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 251, facility_2 715 /
    b(j)    demand at node j  
        / market1 230, market2 273, market3 267 /
    c(i,j)  transportation cost from i to j
        / facility_1.market1 3, facility_1.market2 2, facility_1.market3 2, facility_2.market1 2, facility_2.market2 2, facility_2.market3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1273.0

---

## Problem prob_008 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 271
    - plant2: 585

- demand:
    - market1: 231
    - market2: 215
    - market3: 205

- costs:
    - plant1: {'market1': 2, 'market2': 2, 'market3': 2}
    - plant2: {'market1': 2, 'market2': 2, 'market3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 271; plant2: 585
- Demand requirements: market1: 231; market2: 215; market3: 205  
- Transportation costs: plant1 -> market1: 2, market2: 2, market3: 2; plant2 -> market1: 2, market2: 2, market3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 856 > demand 651)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / plant1 271, plant2 585 /
    b(j)    demand at node j  
        / market1 231, market2 215, market3 205 /
    c(i,j)  transportation cost from i to j
        / plant1.market1 2, plant1.market2 2, plant1.market3 2, plant2.market1 2, plant2.market2 2, plant2.market3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1302.0

---

## Problem prob_009 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 261
    - plant2: 726

- demand:
    - region_1: 383
    - region_2: 293
    - region_3: 342

- costs:
    - plant1: {'region_1': 3, 'region_2': 2, 'region_3': 2}
    - plant2: {'region_1': 3, 'region_2': 2, 'region_3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 261; plant2: 726
- Demand requirements: region_1: 383; region_2: 293; region_3: 342  
- Transportation costs: plant1 -> region_1: 3, region_2: 2, region_3: 2; plant2 -> region_1: 3, region_2: 2, region_3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 987 < demand 1018)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / plant1 261, plant2 726 /
    b(j)    demand at node j  
        / region_1 383, region_2 293, region_3 342 /
    c(i,j)  transportation cost from i to j
        / plant1.region_1 3, plant1.region_2 2, plant1.region_3 2, plant2.region_1 3, plant2.region_2 2, plant2.region_3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_010 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 424
    - facility_2: 610

- demand:
    - market1: 258
    - market2: 384
    - market3: 241

- costs:
    - facility_1: {'market1': 2, 'market2': 2, 'market3': 2}
    - facility_2: {'market1': 3, 'market2': 2, 'market3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 424; facility_2: 610
- Demand requirements: market1: 258; market2: 384; market3: 241  
- Transportation costs: facility_1 -> market1: 2, market2: 2, market3: 2; facility_2 -> market1: 3, market2: 2, market3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 1034 > demand 883)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 424, facility_2 610 /
    b(j)    demand at node j  
        / market1 258, market2 384, market3 241 /
    c(i,j)  transportation cost from i to j
        / facility_1.market1 2, facility_1.market2 2, facility_1.market3 2, facility_2.market1 3, facility_2.market2 2, facility_2.market3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1525.0

---

## Problem prob_011 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 274
    - factory_B: 589
    - factory_C: 481

- demand:
    - city_A: 268
    - city_B: 275
    - city_C: 285

- costs:
    - factory_A: {'city_A': 2, 'city_B': 1, 'city_C': 2}
    - factory_B: {'city_A': 2, 'city_B': 2, 'city_C': 2}
    - factory_C: {'city_A': 3, 'city_B': 2, 'city_C': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 274; factory_B: 589; factory_C: 481
- Demand requirements: city_A: 268; city_B: 275; city_C: 285  
- Transportation costs: factory_A -> city_A: 2, city_B: 1, city_C: 2; factory_B -> city_A: 2, city_B: 2, city_C: 2; factory_C -> city_A: 3, city_B: 2, city_C: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1344 > demand 828)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 274, factory_B 589, factory_C 481 /
    b(j)    demand at node j  
        / city_A 268, city_B 275, city_C 285 /
    c(i,j)  transportation cost from i to j
        / factory_A.city_A 2, factory_A.city_B 1, factory_A.city_C 2, factory_B.city_A 2, factory_B.city_B 2, factory_B.city_C 2, factory_C.city_A 3, factory_C.city_B 2, factory_C.city_C 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1382.0

---

## Problem prob_012 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 438
    - facility_2: 426

- demand:
    - city_A: 279
    - city_B: 302
    - city_C: 241

- costs:
    - facility_1: {'city_A': 2, 'city_B': 2, 'city_C': 2}
    - facility_2: {'city_A': 3, 'city_B': 1, 'city_C': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 438; facility_2: 426
- Demand requirements: city_A: 279; city_B: 302; city_C: 241  
- Transportation costs: facility_1 -> city_A: 2, city_B: 2, city_C: 2; facility_2 -> city_A: 3, city_B: 1, city_C: 1

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
- Balanced/Unbalanced: Unbalanced (supply 864 > demand 822)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 438, facility_2 426 /
    b(j)    demand at node j  
        / city_A 279, city_B 302, city_C 241 /
    c(i,j)  transportation cost from i to j
        / facility_1.city_A 2, facility_1.city_B 2, facility_1.city_C 2, facility_2.city_A 3, facility_2.city_B 1, facility_2.city_C 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1218.0

---

## Problem prob_013 — Transport

**Description:** A manufacturing company needs to transport products from plant_east and plant_west to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant_east: 271
    - plant_west: 589

- demand:
    - warehouse_1: 314
    - warehouse_2: 227

- costs:
    - plant_east: {'warehouse_1': 3, 'warehouse_2': 1}
    - plant_west: {'warehouse_1': 3, 'warehouse_2': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant_east, plant_west (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant_east: 271; plant_west: 589
- Demand requirements: warehouse_1: 314; warehouse_2: 227  
- Transportation costs: plant_east -> warehouse_1: 3, warehouse_2: 1; plant_west -> warehouse_1: 3, warehouse_2: 2

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
- Balanced/Unbalanced: Unbalanced (supply 860 > demand 541)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant_east, plant_west /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / plant_east 271, plant_west 589 /
    b(j)    demand at node j  
        / warehouse_1 314, warehouse_2 227 /
    c(i,j)  transportation cost from i to j
        / plant_east.warehouse_1 3, plant_east.warehouse_2 1, plant_west.warehouse_1 3, plant_west.warehouse_2 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1169.0

---

## Problem prob_014 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 316
    - factory_B: 473
    - factory_C: 543

- demand:
    - warehouse_1: 255
    - warehouse_2: 223

- costs:
    - factory_A: {'warehouse_1': 3, 'warehouse_2': 2}
    - factory_B: {'warehouse_1': 3, 'warehouse_2': 2}
    - factory_C: {'warehouse_1': 3, 'warehouse_2': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 316; factory_B: 473; factory_C: 543
- Demand requirements: warehouse_1: 255; warehouse_2: 223  
- Transportation costs: factory_A -> warehouse_1: 3, warehouse_2: 2; factory_B -> warehouse_1: 3, warehouse_2: 2; factory_C -> warehouse_1: 3, warehouse_2: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1332 > demand 478)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 316, factory_B 473, factory_C 543 /
    b(j)    demand at node j  
        / warehouse_1 255, warehouse_2 223 /
    c(i,j)  transportation cost from i to j
        / factory_A.warehouse_1 3, factory_A.warehouse_2 2, factory_B.warehouse_1 3, factory_B.warehouse_2 2, factory_C.warehouse_1 3, factory_C.warehouse_2 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1211.0

---

## Problem prob_015 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 300
    - facility_2: 719

- demand:
    - warehouse_1: 380
    - warehouse_2: 372

- costs:
    - facility_1: {'warehouse_1': 2, 'warehouse_2': 2}
    - facility_2: {'warehouse_1': 2, 'warehouse_2': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 300; facility_2: 719
- Demand requirements: warehouse_1: 380; warehouse_2: 372  
- Transportation costs: facility_1 -> warehouse_1: 2, warehouse_2: 2; facility_2 -> warehouse_1: 2, warehouse_2: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1019 > demand 752)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 300, facility_2 719 /
    b(j)    demand at node j  
        / warehouse_1 380, warehouse_2 372 /
    c(i,j)  transportation cost from i to j
        / facility_1.warehouse_1 2, facility_1.warehouse_2 2, facility_2.warehouse_1 2, facility_2.warehouse_2 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1504.0

---

## Problem prob_016 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 437
    - plant2: 490

- demand:
    - region_1: 398
    - region_2: 243
    - region_3: 314

- costs:
    - plant1: {'region_1': 2, 'region_2': 2, 'region_3': 2}
    - plant2: {'region_1': 3, 'region_2': 2, 'region_3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 437; plant2: 490
- Demand requirements: region_1: 398; region_2: 243; region_3: 314  
- Transportation costs: plant1 -> region_1: 2, region_2: 2, region_3: 2; plant2 -> region_1: 3, region_2: 2, region_3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 927 < demand 955)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / plant1 437, plant2 490 /
    b(j)    demand at node j  
        / region_1 398, region_2 243, region_3 314 /
    c(i,j)  transportation cost from i to j
        / plant1.region_1 2, plant1.region_2 2, plant1.region_3 2, plant2.region_1 3, plant2.region_2 2, plant2.region_3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_017 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 316
    - facility_2: 608

- demand:
    - city_A: 346
    - city_B: 224
    - city_C: 317

- costs:
    - facility_1: {'city_A': 2, 'city_B': 1, 'city_C': 2}
    - facility_2: {'city_A': 3, 'city_B': 2, 'city_C': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 316; facility_2: 608
- Demand requirements: city_A: 346; city_B: 224; city_C: 317  
- Transportation costs: facility_1 -> city_A: 2, city_B: 1, city_C: 2; facility_2 -> city_A: 3, city_B: 2, city_C: 1

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
- Balanced/Unbalanced: Unbalanced (supply 924 > demand 887)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 316, facility_2 608 /
    b(j)    demand at node j  
        / city_A 346, city_B 224, city_C 317 /
    c(i,j)  transportation cost from i to j
        / facility_1.city_A 2, facility_1.city_B 1, facility_1.city_C 2, facility_2.city_A 3, facility_2.city_B 2, facility_2.city_C 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1487.0

---

## Problem prob_018 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 291
    - facility_2: 534

- demand:
    - market1: 293
    - market2: 352
    - market3: 294

- costs:
    - facility_1: {'market1': 3, 'market2': 2, 'market3': 2}
    - facility_2: {'market1': 3, 'market2': 2, 'market3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 291; facility_2: 534
- Demand requirements: market1: 293; market2: 352; market3: 294  
- Transportation costs: facility_1 -> market1: 3, market2: 2, market3: 2; facility_2 -> market1: 3, market2: 2, market3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 825 < demand 939)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 291, facility_2 534 /
    b(j)    demand at node j  
        / market1 293, market2 352, market3 294 /
    c(i,j)  transportation cost from i to j
        / facility_1.market1 3, facility_1.market2 2, facility_1.market3 2, facility_2.market1 3, facility_2.market2 2, facility_2.market3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_019 — Transport

**Description:** A manufacturing company needs to transport products from plant_east and plant_west to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant_east: 336
    - plant_west: 664

- demand:
    - region_1: 383
    - region_2: 336
    - region_3: 199

- costs:
    - plant_east: {'region_1': 3, 'region_2': 2, 'region_3': 2}
    - plant_west: {'region_1': 3, 'region_2': 2, 'region_3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant_east, plant_west (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant_east: 336; plant_west: 664
- Demand requirements: region_1: 383; region_2: 336; region_3: 199  
- Transportation costs: plant_east -> region_1: 3, region_2: 2, region_3: 2; plant_west -> region_1: 3, region_2: 2, region_3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 1000 > demand 918)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant_east, plant_west /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / plant_east 336, plant_west 664 /
    b(j)    demand at node j  
        / region_1 383, region_2 336, region_3 199 /
    c(i,j)  transportation cost from i to j
        / plant_east.region_1 3, plant_east.region_2 2, plant_east.region_3 2, plant_west.region_1 3, plant_west.region_2 2, plant_west.region_3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2020.0

---

## Problem prob_020 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 440
    - factory_B: 685
    - factory_C: 629

- demand:
    - region_1: 311
    - region_2: 223
    - region_3: 311

- costs:
    - factory_A: {'region_1': 3, 'region_2': 2, 'region_3': 2}
    - factory_B: {'region_1': 3, 'region_2': 2, 'region_3': 1}
    - factory_C: {'region_1': 2, 'region_2': 1, 'region_3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 440; factory_B: 685; factory_C: 629
- Demand requirements: region_1: 311; region_2: 223; region_3: 311  
- Transportation costs: factory_A -> region_1: 3, region_2: 2, region_3: 2; factory_B -> region_1: 3, region_2: 2, region_3: 1; factory_C -> region_1: 2, region_2: 1, region_3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1754 > demand 845)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 440, factory_B 685, factory_C 629 /
    b(j)    demand at node j  
        / region_1 311, region_2 223, region_3 311 /
    c(i,j)  transportation cost from i to j
        / factory_A.region_1 3, factory_A.region_2 2, factory_A.region_3 2, factory_B.region_1 3, factory_B.region_2 2, factory_B.region_3 1, factory_C.region_1 2, factory_C.region_2 1, factory_C.region_3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1156.0

---

## Problem prob_021 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 278
    - plant2: 604

- demand:
    - market1: 412
    - market2: 318
    - market3: 238

- costs:
    - plant1: {'market1': 3, 'market2': 2, 'market3': 2}
    - plant2: {'market1': 2, 'market2': 2, 'market3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 278; plant2: 604
- Demand requirements: market1: 412; market2: 318; market3: 238  
- Transportation costs: plant1 -> market1: 3, market2: 2, market3: 2; plant2 -> market1: 2, market2: 2, market3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 882 < demand 968)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / plant1 278, plant2 604 /
    b(j)    demand at node j  
        / market1 412, market2 318, market3 238 /
    c(i,j)  transportation cost from i to j
        / plant1.market1 3, plant1.market2 2, plant1.market3 2, plant2.market1 2, plant2.market2 2, plant2.market3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_022 — Transport

**Description:** A manufacturing company needs to transport products from plant_east and plant_west to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant_east: 298
    - plant_west: 513

- demand:
    - market1: 400
    - market2: 329
    - market3: 242

- costs:
    - plant_east: {'market1': 2, 'market2': 2, 'market3': 2}
    - plant_west: {'market1': 2, 'market2': 2, 'market3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant_east, plant_west (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant_east: 298; plant_west: 513
- Demand requirements: market1: 400; market2: 329; market3: 242  
- Transportation costs: plant_east -> market1: 2, market2: 2, market3: 2; plant_west -> market1: 2, market2: 2, market3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 811 < demand 971)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant_east, plant_west /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / plant_east 298, plant_west 513 /
    b(j)    demand at node j  
        / market1 400, market2 329, market3 242 /
    c(i,j)  transportation cost from i to j
        / plant_east.market1 2, plant_east.market2 2, plant_east.market3 2, plant_west.market1 2, plant_west.market2 2, plant_west.market3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_023 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 292
    - facility_2: 527

- demand:
    - city_A: 352
    - city_B: 219
    - city_C: 318

- costs:
    - facility_1: {'city_A': 2, 'city_B': 2, 'city_C': 2}
    - facility_2: {'city_A': 3, 'city_B': 2, 'city_C': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 292; facility_2: 527
- Demand requirements: city_A: 352; city_B: 219; city_C: 318  
- Transportation costs: facility_1 -> city_A: 2, city_B: 2, city_C: 2; facility_2 -> city_A: 3, city_B: 2, city_C: 1

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
- Balanced/Unbalanced: Unbalanced (supply 819 < demand 889)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 292, facility_2 527 /
    b(j)    demand at node j  
        / city_A 352, city_B 219, city_C 318 /
    c(i,j)  transportation cost from i to j
        / facility_1.city_A 2, facility_1.city_B 2, facility_1.city_C 2, facility_2.city_A 3, facility_2.city_B 2, facility_2.city_C 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_024 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 440
    - plant2: 447

- demand:
    - warehouse_1: 236
    - warehouse_2: 223

- costs:
    - plant1: {'warehouse_1': 2, 'warehouse_2': 2}
    - plant2: {'warehouse_1': 3, 'warehouse_2': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 440; plant2: 447
- Demand requirements: warehouse_1: 236; warehouse_2: 223  
- Transportation costs: plant1 -> warehouse_1: 2, warehouse_2: 2; plant2 -> warehouse_1: 3, warehouse_2: 2

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
- Balanced/Unbalanced: Unbalanced (supply 887 > demand 459)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / plant1 440, plant2 447 /
    b(j)    demand at node j  
        / warehouse_1 236, warehouse_2 223 /
    c(i,j)  transportation cost from i to j
        / plant1.warehouse_1 2, plant1.warehouse_2 2, plant2.warehouse_1 3, plant2.warehouse_2 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=918.0

---

## Problem prob_025 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 413
    - factory_B: 678
    - factory_C: 289

- demand:
    - region_1: 289
    - region_2: 375
    - region_3: 249

- costs:
    - factory_A: {'region_1': 2, 'region_2': 2, 'region_3': 2}
    - factory_B: {'region_1': 2, 'region_2': 2, 'region_3': 1}
    - factory_C: {'region_1': 2, 'region_2': 1, 'region_3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 413; factory_B: 678; factory_C: 289
- Demand requirements: region_1: 289; region_2: 375; region_3: 249  
- Transportation costs: factory_A -> region_1: 2, region_2: 2, region_3: 2; factory_B -> region_1: 2, region_2: 2, region_3: 1; factory_C -> region_1: 2, region_2: 1, region_3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1380 > demand 913)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 413, factory_B 678, factory_C 289 /
    b(j)    demand at node j  
        / region_1 289, region_2 375, region_3 249 /
    c(i,j)  transportation cost from i to j
        / factory_A.region_1 2, factory_A.region_2 2, factory_A.region_3 2, factory_B.region_1 2, factory_B.region_2 2, factory_B.region_3 1, factory_C.region_1 2, factory_C.region_2 1, factory_C.region_3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1288.0

---

## Problem prob_026 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 364
    - facility_2: 473

- demand:
    - warehouse_1: 228
    - warehouse_2: 324

- costs:
    - facility_1: {'warehouse_1': 3, 'warehouse_2': 2}
    - facility_2: {'warehouse_1': 2, 'warehouse_2': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 364; facility_2: 473
- Demand requirements: warehouse_1: 228; warehouse_2: 324  
- Transportation costs: facility_1 -> warehouse_1: 3, warehouse_2: 2; facility_2 -> warehouse_1: 2, warehouse_2: 2

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
- Balanced/Unbalanced: Unbalanced (supply 837 > demand 552)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 364, facility_2 473 /
    b(j)    demand at node j  
        / warehouse_1 228, warehouse_2 324 /
    c(i,j)  transportation cost from i to j
        / facility_1.warehouse_1 3, facility_1.warehouse_2 2, facility_2.warehouse_1 2, facility_2.warehouse_2 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1104.0

---

## Problem prob_027 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 346
    - factory_B: 472
    - factory_C: 342

- demand:
    - region_1: 391
    - region_2: 308
    - region_3: 298

- costs:
    - factory_A: {'region_1': 2, 'region_2': 1, 'region_3': 2}
    - factory_B: {'region_1': 2, 'region_2': 2, 'region_3': 1}
    - factory_C: {'region_1': 2, 'region_2': 2, 'region_3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 346; factory_B: 472; factory_C: 342
- Demand requirements: region_1: 391; region_2: 308; region_3: 298  
- Transportation costs: factory_A -> region_1: 2, region_2: 1, region_3: 2; factory_B -> region_1: 2, region_2: 2, region_3: 1; factory_C -> region_1: 2, region_2: 2, region_3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1160 > demand 997)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 346, factory_B 472, factory_C 342 /
    b(j)    demand at node j  
        / region_1 391, region_2 308, region_3 298 /
    c(i,j)  transportation cost from i to j
        / factory_A.region_1 2, factory_A.region_2 1, factory_A.region_3 2, factory_B.region_1 2, factory_B.region_2 2, factory_B.region_3 1, factory_C.region_1 2, factory_C.region_2 2, factory_C.region_3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1388.0

---

## Problem prob_028 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 252
    - factory_B: 510
    - factory_C: 438

- demand:
    - region_1: 321
    - region_2: 315
    - region_3: 207

- costs:
    - factory_A: {'region_1': 3, 'region_2': 2, 'region_3': 2}
    - factory_B: {'region_1': 2, 'region_2': 2, 'region_3': 2}
    - factory_C: {'region_1': 3, 'region_2': 1, 'region_3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 252; factory_B: 510; factory_C: 438
- Demand requirements: region_1: 321; region_2: 315; region_3: 207  
- Transportation costs: factory_A -> region_1: 3, region_2: 2, region_3: 2; factory_B -> region_1: 2, region_2: 2, region_3: 2; factory_C -> region_1: 3, region_2: 1, region_3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1200 > demand 843)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 252, factory_B 510, factory_C 438 /
    b(j)    demand at node j  
        / region_1 321, region_2 315, region_3 207 /
    c(i,j)  transportation cost from i to j
        / factory_A.region_1 3, factory_A.region_2 2, factory_A.region_3 2, factory_B.region_1 2, factory_B.region_2 2, factory_B.region_3 2, factory_C.region_1 3, factory_C.region_2 1, factory_C.region_3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1371.0

---

## Problem prob_029 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 291
    - factory_B: 510
    - factory_C: 420

- demand:
    - market1: 231
    - market2: 355
    - market3: 244

- costs:
    - factory_A: {'market1': 2, 'market2': 1, 'market3': 2}
    - factory_B: {'market1': 3, 'market2': 2, 'market3': 1}
    - factory_C: {'market1': 3, 'market2': 2, 'market3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 291; factory_B: 510; factory_C: 420
- Demand requirements: market1: 231; market2: 355; market3: 244  
- Transportation costs: factory_A -> market1: 2, market2: 1, market3: 2; factory_B -> market1: 3, market2: 2, market3: 1; factory_C -> market1: 3, market2: 2, market3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1221 > demand 830)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 291, factory_B 510, factory_C 420 /
    b(j)    demand at node j  
        / market1 231, market2 355, market3 244 /
    c(i,j)  transportation cost from i to j
        / factory_A.market1 2, factory_A.market2 1, factory_A.market3 2, factory_B.market1 3, factory_B.market2 2, factory_B.market3 1, factory_C.market1 3, factory_C.market2 2, factory_C.market3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1356.0

---

## Problem prob_030 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 384
    - plant2: 433

- demand:
    - warehouse_1: 275
    - warehouse_2: 264

- costs:
    - plant1: {'warehouse_1': 2, 'warehouse_2': 2}
    - plant2: {'warehouse_1': 3, 'warehouse_2': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 384; plant2: 433
- Demand requirements: warehouse_1: 275; warehouse_2: 264  
- Transportation costs: plant1 -> warehouse_1: 2, warehouse_2: 2; plant2 -> warehouse_1: 3, warehouse_2: 2

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
- Balanced/Unbalanced: Unbalanced (supply 817 > demand 539)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / plant1 384, plant2 433 /
    b(j)    demand at node j  
        / warehouse_1 275, warehouse_2 264 /
    c(i,j)  transportation cost from i to j
        / plant1.warehouse_1 2, plant1.warehouse_2 2, plant2.warehouse_1 3, plant2.warehouse_2 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1078.0

---

## Problem prob_031 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 290
    - factory_B: 587
    - factory_C: 552

- demand:
    - warehouse_1: 252
    - warehouse_2: 219

- costs:
    - factory_A: {'warehouse_1': 2, 'warehouse_2': 1}
    - factory_B: {'warehouse_1': 3, 'warehouse_2': 2}
    - factory_C: {'warehouse_1': 3, 'warehouse_2': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 290; factory_B: 587; factory_C: 552
- Demand requirements: warehouse_1: 252; warehouse_2: 219  
- Transportation costs: factory_A -> warehouse_1: 2, warehouse_2: 1; factory_B -> warehouse_1: 3, warehouse_2: 2; factory_C -> warehouse_1: 3, warehouse_2: 1

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
- Balanced/Unbalanced: Unbalanced (supply 1429 > demand 471)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 290, factory_B 587, factory_C 552 /
    b(j)    demand at node j  
        / warehouse_1 252, warehouse_2 219 /
    c(i,j)  transportation cost from i to j
        / factory_A.warehouse_1 2, factory_A.warehouse_2 1, factory_B.warehouse_1 3, factory_B.warehouse_2 2, factory_C.warehouse_1 3, factory_C.warehouse_2 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=723.0

---

## Problem prob_032 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 343
    - facility_2: 641

- demand:
    - warehouse_1: 271
    - warehouse_2: 291

- costs:
    - facility_1: {'warehouse_1': 3, 'warehouse_2': 2}
    - facility_2: {'warehouse_1': 3, 'warehouse_2': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 343; facility_2: 641
- Demand requirements: warehouse_1: 271; warehouse_2: 291  
- Transportation costs: facility_1 -> warehouse_1: 3, warehouse_2: 2; facility_2 -> warehouse_1: 3, warehouse_2: 2

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
- Balanced/Unbalanced: Unbalanced (supply 984 > demand 562)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 343, facility_2 641 /
    b(j)    demand at node j  
        / warehouse_1 271, warehouse_2 291 /
    c(i,j)  transportation cost from i to j
        / facility_1.warehouse_1 3, facility_1.warehouse_2 2, facility_2.warehouse_1 3, facility_2.warehouse_2 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1395.0

---

## Problem prob_033 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 405
    - factory_B: 594
    - factory_C: 558

- demand:
    - region_1: 406
    - region_2: 230
    - region_3: 335

- costs:
    - factory_A: {'region_1': 2, 'region_2': 2, 'region_3': 2}
    - factory_B: {'region_1': 2, 'region_2': 2, 'region_3': 2}
    - factory_C: {'region_1': 3, 'region_2': 2, 'region_3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 405; factory_B: 594; factory_C: 558
- Demand requirements: region_1: 406; region_2: 230; region_3: 335  
- Transportation costs: factory_A -> region_1: 2, region_2: 2, region_3: 2; factory_B -> region_1: 2, region_2: 2, region_3: 2; factory_C -> region_1: 3, region_2: 2, region_3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1557 > demand 971)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 405, factory_B 594, factory_C 558 /
    b(j)    demand at node j  
        / region_1 406, region_2 230, region_3 335 /
    c(i,j)  transportation cost from i to j
        / factory_A.region_1 2, factory_A.region_2 2, factory_A.region_3 2, factory_B.region_1 2, factory_B.region_2 2, factory_B.region_3 2, factory_C.region_1 3, factory_C.region_2 2, factory_C.region_3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1942.0

---

## Problem prob_034 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 400
    - facility_2: 702

- demand:
    - city_A: 359
    - city_B: 285
    - city_C: 298

- costs:
    - facility_1: {'city_A': 2, 'city_B': 2, 'city_C': 2}
    - facility_2: {'city_A': 2, 'city_B': 2, 'city_C': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 400; facility_2: 702
- Demand requirements: city_A: 359; city_B: 285; city_C: 298  
- Transportation costs: facility_1 -> city_A: 2, city_B: 2, city_C: 2; facility_2 -> city_A: 2, city_B: 2, city_C: 1

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
- Balanced/Unbalanced: Unbalanced (supply 1102 > demand 942)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 400, facility_2 702 /
    b(j)    demand at node j  
        / city_A 359, city_B 285, city_C 298 /
    c(i,j)  transportation cost from i to j
        / facility_1.city_A 2, facility_1.city_B 2, facility_1.city_C 2, facility_2.city_A 2, facility_2.city_B 2, facility_2.city_C 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1586.0

---

## Problem prob_035 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 278
    - factory_B: 497
    - factory_C: 480

- demand:
    - city_A: 326
    - city_B: 341
    - city_C: 223

- costs:
    - factory_A: {'city_A': 3, 'city_B': 1, 'city_C': 1}
    - factory_B: {'city_A': 2, 'city_B': 2, 'city_C': 2}
    - factory_C: {'city_A': 3, 'city_B': 2, 'city_C': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 278; factory_B: 497; factory_C: 480
- Demand requirements: city_A: 326; city_B: 341; city_C: 223  
- Transportation costs: factory_A -> city_A: 3, city_B: 1, city_C: 1; factory_B -> city_A: 2, city_B: 2, city_C: 2; factory_C -> city_A: 3, city_B: 2, city_C: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1255 > demand 890)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 278, factory_B 497, factory_C 480 /
    b(j)    demand at node j  
        / city_A 326, city_B 341, city_C 223 /
    c(i,j)  transportation cost from i to j
        / factory_A.city_A 3, factory_A.city_B 1, factory_A.city_C 1, factory_B.city_A 2, factory_B.city_B 2, factory_B.city_C 2, factory_C.city_A 3, factory_C.city_B 2, factory_C.city_C 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1502.0

---

## Problem prob_036 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 292
    - facility_2: 468

- demand:
    - city_A: 322
    - city_B: 212
    - city_C: 288

- costs:
    - facility_1: {'city_A': 2, 'city_B': 1, 'city_C': 2}
    - facility_2: {'city_A': 2, 'city_B': 2, 'city_C': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 292; facility_2: 468
- Demand requirements: city_A: 322; city_B: 212; city_C: 288  
- Transportation costs: facility_1 -> city_A: 2, city_B: 1, city_C: 2; facility_2 -> city_A: 2, city_B: 2, city_C: 1

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
- Balanced/Unbalanced: Unbalanced (supply 760 < demand 822)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 292, facility_2 468 /
    b(j)    demand at node j  
        / city_A 322, city_B 212, city_C 288 /
    c(i,j)  transportation cost from i to j
        / facility_1.city_A 2, facility_1.city_B 1, facility_1.city_C 2, facility_2.city_A 2, facility_2.city_B 2, facility_2.city_C 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_037 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 422
    - plant2: 713

- demand:
    - city_A: 407
    - city_B: 247
    - city_C: 193

- costs:
    - plant1: {'city_A': 2, 'city_B': 1, 'city_C': 2}
    - plant2: {'city_A': 2, 'city_B': 2, 'city_C': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 422; plant2: 713
- Demand requirements: city_A: 407; city_B: 247; city_C: 193  
- Transportation costs: plant1 -> city_A: 2, city_B: 1, city_C: 2; plant2 -> city_A: 2, city_B: 2, city_C: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1135 > demand 847)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / plant1 422, plant2 713 /
    b(j)    demand at node j  
        / city_A 407, city_B 247, city_C 193 /
    c(i,j)  transportation cost from i to j
        / plant1.city_A 2, plant1.city_B 1, plant1.city_C 2, plant2.city_A 2, plant2.city_B 2, plant2.city_C 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1447.0

---

## Problem prob_038 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 287
    - facility_2: 710

- demand:
    - region_1: 347
    - region_2: 330
    - region_3: 274

- costs:
    - facility_1: {'region_1': 3, 'region_2': 2, 'region_3': 2}
    - facility_2: {'region_1': 3, 'region_2': 2, 'region_3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 287; facility_2: 710
- Demand requirements: region_1: 347; region_2: 330; region_3: 274  
- Transportation costs: facility_1 -> region_1: 3, region_2: 2, region_3: 2; facility_2 -> region_1: 3, region_2: 2, region_3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 997 > demand 951)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 287, facility_2 710 /
    b(j)    demand at node j  
        / region_1 347, region_2 330, region_3 274 /
    c(i,j)  transportation cost from i to j
        / facility_1.region_1 3, facility_1.region_2 2, facility_1.region_3 2, facility_2.region_1 3, facility_2.region_2 2, facility_2.region_3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1975.0

---

## Problem prob_039 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to warehouse_1 and warehouse_2. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 423
    - factory_B: 687
    - factory_C: 629

- demand:
    - warehouse_1: 231
    - warehouse_2: 307

- costs:
    - factory_A: {'warehouse_1': 2, 'warehouse_2': 2}
    - factory_B: {'warehouse_1': 2, 'warehouse_2': 2}
    - factory_C: {'warehouse_1': 3, 'warehouse_2': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: warehouse_1, warehouse_2 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 423; factory_B: 687; factory_C: 629
- Demand requirements: warehouse_1: 231; warehouse_2: 307  
- Transportation costs: factory_A -> warehouse_1: 2, warehouse_2: 2; factory_B -> warehouse_1: 2, warehouse_2: 2; factory_C -> warehouse_1: 3, warehouse_2: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1739 > demand 538)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / warehouse_1, warehouse_2 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 423, factory_B 687, factory_C 629 /
    b(j)    demand at node j  
        / warehouse_1 231, warehouse_2 307 /
    c(i,j)  transportation cost from i to j
        / factory_A.warehouse_1 2, factory_A.warehouse_2 2, factory_B.warehouse_1 2, factory_B.warehouse_2 2, factory_C.warehouse_1 3, factory_C.warehouse_2 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1076.0

---

## Problem prob_040 — Transport

**Description:** A manufacturing company needs to transport products from plant_east and plant_west to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant_east: 333
    - plant_west: 555

- demand:
    - region_1: 299
    - region_2: 341
    - region_3: 200

- costs:
    - plant_east: {'region_1': 2, 'region_2': 2, 'region_3': 2}
    - plant_west: {'region_1': 2, 'region_2': 1, 'region_3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant_east, plant_west (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant_east: 333; plant_west: 555
- Demand requirements: region_1: 299; region_2: 341; region_3: 200  
- Transportation costs: plant_east -> region_1: 2, region_2: 2, region_3: 2; plant_west -> region_1: 2, region_2: 1, region_3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 888 > demand 840)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant_east, plant_west /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / plant_east 333, plant_west 555 /
    b(j)    demand at node j  
        / region_1 299, region_2 341, region_3 200 /
    c(i,j)  transportation cost from i to j
        / plant_east.region_1 2, plant_east.region_2 2, plant_east.region_3 2, plant_west.region_1 2, plant_west.region_2 1, plant_west.region_3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1139.0

---

## Problem prob_041 — Transport

**Description:** A manufacturing company needs to transport products from plant_east and plant_west to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant_east: 416
    - plant_west: 449

- demand:
    - region_1: 411
    - region_2: 274
    - region_3: 261

- costs:
    - plant_east: {'region_1': 2, 'region_2': 2, 'region_3': 2}
    - plant_west: {'region_1': 2, 'region_2': 2, 'region_3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant_east, plant_west (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant_east: 416; plant_west: 449
- Demand requirements: region_1: 411; region_2: 274; region_3: 261  
- Transportation costs: plant_east -> region_1: 2, region_2: 2, region_3: 2; plant_west -> region_1: 2, region_2: 2, region_3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 865 < demand 946)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant_east, plant_west /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / plant_east 416, plant_west 449 /
    b(j)    demand at node j  
        / region_1 411, region_2 274, region_3 261 /
    c(i,j)  transportation cost from i to j
        / plant_east.region_1 2, plant_east.region_2 2, plant_east.region_3 2, plant_west.region_1 2, plant_west.region_2 2, plant_west.region_3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_042 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 303
    - plant2: 630

- demand:
    - region_1: 352
    - region_2: 372
    - region_3: 246

- costs:
    - plant1: {'region_1': 2, 'region_2': 2, 'region_3': 2}
    - plant2: {'region_1': 2, 'region_2': 2, 'region_3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 303; plant2: 630
- Demand requirements: region_1: 352; region_2: 372; region_3: 246  
- Transportation costs: plant1 -> region_1: 2, region_2: 2, region_3: 2; plant2 -> region_1: 2, region_2: 2, region_3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 933 < demand 970)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / plant1 303, plant2 630 /
    b(j)    demand at node j  
        / region_1 352, region_2 372, region_3 246 /
    c(i,j)  transportation cost from i to j
        / plant1.region_1 2, plant1.region_2 2, plant1.region_3 2, plant2.region_1 2, plant2.region_2 2, plant2.region_3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_043 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 304
    - factory_B: 471
    - factory_C: 574

- demand:
    - market1: 326
    - market2: 326
    - market3: 242

- costs:
    - factory_A: {'market1': 2, 'market2': 2, 'market3': 1}
    - factory_B: {'market1': 2, 'market2': 2, 'market3': 2}
    - factory_C: {'market1': 3, 'market2': 2, 'market3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 304; factory_B: 471; factory_C: 574
- Demand requirements: market1: 326; market2: 326; market3: 242  
- Transportation costs: factory_A -> market1: 2, market2: 2, market3: 1; factory_B -> market1: 2, market2: 2, market3: 2; factory_C -> market1: 3, market2: 2, market3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1349 > demand 894)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 304, factory_B 471, factory_C 574 /
    b(j)    demand at node j  
        / market1 326, market2 326, market3 242 /
    c(i,j)  transportation cost from i to j
        / factory_A.market1 2, factory_A.market2 2, factory_A.market3 1, factory_B.market1 2, factory_B.market2 2, factory_B.market3 2, factory_C.market1 3, factory_C.market2 2, factory_C.market3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1546.0

---

## Problem prob_044 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 400
    - factory_B: 547
    - factory_C: 514

- demand:
    - city_A: 329
    - city_B: 368
    - city_C: 223

- costs:
    - factory_A: {'city_A': 3, 'city_B': 2, 'city_C': 1}
    - factory_B: {'city_A': 2, 'city_B': 2, 'city_C': 1}
    - factory_C: {'city_A': 2, 'city_B': 2, 'city_C': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 400; factory_B: 547; factory_C: 514
- Demand requirements: city_A: 329; city_B: 368; city_C: 223  
- Transportation costs: factory_A -> city_A: 3, city_B: 2, city_C: 1; factory_B -> city_A: 2, city_B: 2, city_C: 1; factory_C -> city_A: 2, city_B: 2, city_C: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1461 > demand 920)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 400, factory_B 547, factory_C 514 /
    b(j)    demand at node j  
        / city_A 329, city_B 368, city_C 223 /
    c(i,j)  transportation cost from i to j
        / factory_A.city_A 3, factory_A.city_B 2, factory_A.city_C 1, factory_B.city_A 2, factory_B.city_B 2, factory_B.city_C 1, factory_C.city_A 2, factory_C.city_B 2, factory_C.city_C 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1617.0

---

## Problem prob_045 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 436
    - facility_2: 717

- demand:
    - city_A: 361
    - city_B: 371
    - city_C: 317

- costs:
    - facility_1: {'city_A': 2, 'city_B': 2, 'city_C': 2}
    - facility_2: {'city_A': 3, 'city_B': 2, 'city_C': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 436; facility_2: 717
- Demand requirements: city_A: 361; city_B: 371; city_C: 317  
- Transportation costs: facility_1 -> city_A: 2, city_B: 2, city_C: 2; facility_2 -> city_A: 3, city_B: 2, city_C: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1153 > demand 1049)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 436, facility_2 717 /
    b(j)    demand at node j  
        / city_A 361, city_B 371, city_C 317 /
    c(i,j)  transportation cost from i to j
        / facility_1.city_A 2, facility_1.city_B 2, facility_1.city_C 2, facility_2.city_A 3, facility_2.city_B 2, facility_2.city_C 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2098.0

---

## Problem prob_046 — Transport

**Description:** A manufacturing company needs to transport products from plant_east and plant_west to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant_east: 443
    - plant_west: 622

- demand:
    - market1: 301
    - market2: 260
    - market3: 331

- costs:
    - plant_east: {'market1': 2, 'market2': 2, 'market3': 2}
    - plant_west: {'market1': 2, 'market2': 2, 'market3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant_east, plant_west (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant_east: 443; plant_west: 622
- Demand requirements: market1: 301; market2: 260; market3: 331  
- Transportation costs: plant_east -> market1: 2, market2: 2, market3: 2; plant_west -> market1: 2, market2: 2, market3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 1065 > demand 892)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant_east, plant_west /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / plant_east 443, plant_west 622 /
    b(j)    demand at node j  
        / market1 301, market2 260, market3 331 /
    c(i,j)  transportation cost from i to j
        / plant_east.market1 2, plant_east.market2 2, plant_east.market3 2, plant_west.market1 2, plant_west.market2 2, plant_west.market3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1453.0

---

## Problem prob_047 — Transport

**Description:** A manufacturing company needs to transport products from facility_1 and facility_2 to market1, market2 and market3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - facility_1: 405
    - facility_2: 498

- demand:
    - market1: 372
    - market2: 281
    - market3: 334

- costs:
    - facility_1: {'market1': 3, 'market2': 2, 'market3': 2}
    - facility_2: {'market1': 3, 'market2': 2, 'market3': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: facility_1, facility_2 (plants/factories)
- Demand nodes: market1, market2, market3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: facility_1: 405; facility_2: 498
- Demand requirements: market1: 372; market2: 281; market3: 334  
- Transportation costs: facility_1 -> market1: 3, market2: 2, market3: 2; facility_2 -> market1: 3, market2: 2, market3: 1

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
- Balanced/Unbalanced: Unbalanced (supply 903 < demand 987)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / facility_1, facility_2 /
    j   demand nodes    / market1, market2, market3 /;

Parameters
    a(i)    capacity of supply node i
        / facility_1 405, facility_2 498 /
    b(j)    demand at node j  
        / market1 372, market2 281, market3 334 /
    c(i,j)  transportation cost from i to j
        / facility_1.market1 3, facility_1.market2 2, facility_1.market3 2, facility_2.market1 3, facility_2.market2 2, facility_2.market3 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=False, objective=None

---

## Problem prob_048 — Transport

**Description:** A manufacturing company needs to transport products from factory_A, factory_B and factory_C to region_1, region_2 and region_3. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - factory_A: 337
    - factory_B: 505
    - factory_C: 530

- demand:
    - region_1: 327
    - region_2: 382
    - region_3: 276

- costs:
    - factory_A: {'region_1': 2, 'region_2': 2, 'region_3': 1}
    - factory_B: {'region_1': 2, 'region_2': 2, 'region_3': 1}
    - factory_C: {'region_1': 3, 'region_2': 2, 'region_3': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: factory_A, factory_B, factory_C (plants/factories)
- Demand nodes: region_1, region_2, region_3 (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: factory_A: 337; factory_B: 505; factory_C: 530
- Demand requirements: region_1: 327; region_2: 382; region_3: 276  
- Transportation costs: factory_A -> region_1: 2, region_2: 2, region_3: 1; factory_B -> region_1: 2, region_2: 2, region_3: 1; factory_C -> region_1: 3, region_2: 2, region_3: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1372 > demand 985)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / factory_A, factory_B, factory_C /
    j   demand nodes    / region_1, region_2, region_3 /;

Parameters
    a(i)    capacity of supply node i
        / factory_A 337, factory_B 505, factory_C 530 /
    b(j)    demand at node j  
        / region_1 327, region_2 382, region_3 276 /
    c(i,j)  transportation cost from i to j
        / factory_A.region_1 2, factory_A.region_2 2, factory_A.region_3 1, factory_B.region_1 2, factory_B.region_2 2, factory_B.region_3 1, factory_C.region_1 3, factory_C.region_2 2, factory_C.region_3 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1694.0

---

## Problem prob_049 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 307
    - plant2: 697

- demand:
    - city_A: 308
    - city_B: 274
    - city_C: 246

- costs:
    - plant1: {'city_A': 2, 'city_B': 2, 'city_C': 2}
    - plant2: {'city_A': 3, 'city_B': 2, 'city_C': 1}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 307; plant2: 697
- Demand requirements: city_A: 308; city_B: 274; city_C: 246  
- Transportation costs: plant1 -> city_A: 2, city_B: 2, city_C: 2; plant2 -> city_A: 3, city_B: 2, city_C: 1

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
- Balanced/Unbalanced: Unbalanced (supply 1004 > demand 828)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / plant1 307, plant2 697 /
    b(j)    demand at node j  
        / city_A 308, city_B 274, city_C 246 /
    c(i,j)  transportation cost from i to j
        / plant1.city_A 2, plant1.city_B 2, plant1.city_C 2, plant2.city_A 3, plant2.city_B 2, plant2.city_C 1 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1411.0

---

## Problem prob_050 — Transport

**Description:** A manufacturing company needs to transport products from plant1 and plant2 to city_A, city_B and city_C. Minimize total transportation cost while satisfying supply capacities and demand requirements.

**Supplementary Tables:**
- supply:
    - plant1: 378
    - plant2: 655

- demand:
    - city_A: 282
    - city_B: 244
    - city_C: 247

- costs:
    - plant1: {'city_A': 2, 'city_B': 1, 'city_C': 2}
    - plant2: {'city_A': 3, 'city_B': 2, 'city_C': 2}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Transportation Optimization

SETS IDENTIFICATION:
- Supply nodes: plant1, plant2 (plants/factories)
- Demand nodes: city_A, city_B, city_C (markets/customers)

PARAMETERS DEFINITION:
- Supply capacities: plant1: 378; plant2: 655
- Demand requirements: city_A: 282; city_B: 244; city_C: 247  
- Transportation costs: plant1 -> city_A: 2, city_B: 1, city_C: 2; plant2 -> city_A: 3, city_B: 2, city_C: 2

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
- Balanced/Unbalanced: Unbalanced (supply 1033 > demand 773)

SOLUTION APPROACH:
- Use LP solver to find optimal shipment quantities
- Ensure all constraints are satisfied
- Minimize total transportation cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   supply nodes    / plant1, plant2 /
    j   demand nodes    / city_A, city_B, city_C /;

Parameters
    a(i)    capacity of supply node i
        / plant1 378, plant2 655 /
    b(j)    demand at node j  
        / city_A 282, city_B 244, city_C 247 /
    c(i,j)  transportation cost from i to j
        / plant1.city_A 2, plant1.city_B 1, plant1.city_C 2, plant2.city_A 3, plant2.city_B 2, plant2.city_C 2 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1450.0

---

## Problem prob_051 — Assignment

**Description:** Assign w1, w2 and w3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'task_alpha': 8, 'task_beta': 12, 'task_gamma': 18}
    - w2: {'task_alpha': 10, 'task_beta': 12, 'task_gamma': 10}
    - w3: {'task_alpha': 10, 'task_beta': 13, 'task_gamma': 8}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> task_alpha: 8, task_beta: 12, task_gamma: 18; w2 -> task_alpha: 10, task_beta: 12, task_gamma: 10; w3 -> task_alpha: 10, task_beta: 13, task_gamma: 8 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.task_alpha 8, w1.task_beta 12, w1.task_gamma 18, w2.task_alpha 10, w2.task_beta 12, w2.task_gamma 10, w3.task_alpha 10, w3.task_beta 13, w3.task_gamma 8 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_052 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'t1': 12, 't2': 11, 't3': 14}
    - employee_2: {'t1': 9, 't2': 11, 't3': 12}
    - employee_3: {'t1': 10, 't2': 11, 't3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> t1: 12, t2: 11, t3: 14; employee_2 -> t1: 9, t2: 11, t3: 12; employee_3 -> t1: 10, t2: 11, t3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.t1 12, employee_1.t2 11, employee_1.t3 14, employee_2.t1 9, employee_2.t2 11, employee_2.t3 12, employee_3.t1 10, employee_3.t2 11, employee_3.t3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_053 — Assignment

**Description:** Assign w1, w2 and w3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'task_alpha': 8, 'task_beta': 10, 'task_gamma': 12}
    - w2: {'task_alpha': 10, 'task_beta': 8, 'task_gamma': 16}
    - w3: {'task_alpha': 7, 'task_beta': 13, 'task_gamma': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> task_alpha: 8, task_beta: 10, task_gamma: 12; w2 -> task_alpha: 10, task_beta: 8, task_gamma: 16; w3 -> task_alpha: 7, task_beta: 13, task_gamma: 12 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.task_alpha 8, w1.task_beta 10, w1.task_gamma 12, w2.task_alpha 10, w2.task_beta 8, w2.task_gamma 16, w3.task_alpha 7, w3.task_beta 13, w3.task_gamma 12 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_054 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'task_alpha': 11, 'task_beta': 11, 'task_gamma': 12}
    - worker_B: {'task_alpha': 8, 'task_beta': 13, 'task_gamma': 15}
    - worker_C: {'task_alpha': 10, 'task_beta': 15, 'task_gamma': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> task_alpha: 11, task_beta: 11, task_gamma: 12; worker_B -> task_alpha: 8, task_beta: 13, task_gamma: 15; worker_C -> task_alpha: 10, task_beta: 15, task_gamma: 12 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.task_alpha 11, worker_A.task_beta 11, worker_A.task_gamma 12, worker_B.task_alpha 8, worker_B.task_beta 13, worker_B.task_gamma 15, worker_C.task_alpha 10, worker_C.task_beta 15, worker_C.task_gamma 12 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_055 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'task_alpha': 11, 'task_beta': 10, 'task_gamma': 12}
    - worker_B: {'task_alpha': 9, 'task_beta': 10, 'task_gamma': 16}
    - worker_C: {'task_alpha': 9, 'task_beta': 16, 'task_gamma': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> task_alpha: 11, task_beta: 10, task_gamma: 12; worker_B -> task_alpha: 9, task_beta: 10, task_gamma: 16; worker_C -> task_alpha: 9, task_beta: 16, task_gamma: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.task_alpha 11, worker_A.task_beta 10, worker_A.task_gamma 12, worker_B.task_alpha 9, worker_B.task_beta 10, worker_B.task_gamma 16, worker_C.task_alpha 9, worker_C.task_beta 16, worker_C.task_gamma 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_056 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'task_alpha': 9, 'task_beta': 13, 'task_gamma': 14}
    - employee_2: {'task_alpha': 9, 'task_beta': 11, 'task_gamma': 10}
    - employee_3: {'task_alpha': 10, 'task_beta': 12, 'task_gamma': 8}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> task_alpha: 9, task_beta: 13, task_gamma: 14; employee_2 -> task_alpha: 9, task_beta: 11, task_gamma: 10; employee_3 -> task_alpha: 10, task_beta: 12, task_gamma: 8 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.task_alpha 9, employee_1.task_beta 13, employee_1.task_gamma 14, employee_2.task_alpha 9, employee_2.task_beta 11, employee_2.task_gamma 10, employee_3.task_alpha 10, employee_3.task_beta 12, employee_3.task_gamma 8 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_057 — Assignment

**Description:** Assign w1, w2 and w3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'job_1': 12, 'job_2': 12, 'job_3': 16}
    - w2: {'job_1': 8, 'job_2': 14, 'job_3': 16}
    - w3: {'job_1': 10, 'job_2': 17, 'job_3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> job_1: 12, job_2: 12, job_3: 16; w2 -> job_1: 8, job_2: 14, job_3: 16; w3 -> job_1: 10, job_2: 17, job_3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.job_1 12, w1.job_2 12, w1.job_3 16, w2.job_1 8, w2.job_2 14, w2.job_3 16, w3.job_1 10, w3.job_2 17, w3.job_3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_058 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'task_alpha': 10, 'task_beta': 12, 'task_gamma': 12}
    - employee_2: {'task_alpha': 7, 'task_beta': 12, 'task_gamma': 10}
    - employee_3: {'task_alpha': 9, 'task_beta': 12, 'task_gamma': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> task_alpha: 10, task_beta: 12, task_gamma: 12; employee_2 -> task_alpha: 7, task_beta: 12, task_gamma: 10; employee_3 -> task_alpha: 9, task_beta: 12, task_gamma: 11 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.task_alpha 10, employee_1.task_beta 12, employee_1.task_gamma 12, employee_2.task_alpha 7, employee_2.task_beta 12, employee_2.task_gamma 10, employee_3.task_alpha 9, employee_3.task_beta 12, employee_3.task_gamma 11 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_059 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'t1': 12, 't2': 11, 't3': 14}
    - employee_2: {'t1': 7, 't2': 12, 't3': 15}
    - employee_3: {'t1': 8, 't2': 12, 't3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> t1: 12, t2: 11, t3: 14; employee_2 -> t1: 7, t2: 12, t3: 15; employee_3 -> t1: 8, t2: 12, t3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.t1 12, employee_1.t2 11, employee_1.t3 14, employee_2.t1 7, employee_2.t2 12, employee_2.t3 15, employee_3.t1 8, employee_3.t2 12, employee_3.t3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_060 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'job_1': 11, 'job_2': 15, 'job_3': 12}
    - employee_2: {'job_1': 9, 'job_2': 13, 'job_3': 12}
    - employee_3: {'job_1': 9, 'job_2': 17, 'job_3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> job_1: 11, job_2: 15, job_3: 12; employee_2 -> job_1: 9, job_2: 13, job_3: 12; employee_3 -> job_1: 9, job_2: 17, job_3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.job_1 11, employee_1.job_2 15, employee_1.job_3 12, employee_2.job_1 9, employee_2.job_2 13, employee_2.job_3 12, employee_3.job_1 9, employee_3.job_2 17, employee_3.job_3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_061 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'task_alpha': 11, 'task_beta': 13, 'task_gamma': 17}
    - employee_2: {'task_alpha': 7, 'task_beta': 12, 'task_gamma': 11}
    - employee_3: {'task_alpha': 7, 'task_beta': 16, 'task_gamma': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> task_alpha: 11, task_beta: 13, task_gamma: 17; employee_2 -> task_alpha: 7, task_beta: 12, task_gamma: 11; employee_3 -> task_alpha: 7, task_beta: 16, task_gamma: 12 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.task_alpha 11, employee_1.task_beta 13, employee_1.task_gamma 17, employee_2.task_alpha 7, employee_2.task_beta 12, employee_2.task_gamma 11, employee_3.task_alpha 7, employee_3.task_beta 16, employee_3.task_gamma 12 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_062 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'t1': 9, 't2': 15, 't3': 18}
    - employee_2: {'t1': 6, 't2': 10, 't3': 10}
    - employee_3: {'t1': 8, 't2': 16, 't3': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> t1: 9, t2: 15, t3: 18; employee_2 -> t1: 6, t2: 10, t3: 10; employee_3 -> t1: 8, t2: 16, t3: 11 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.t1 9, employee_1.t2 15, employee_1.t3 18, employee_2.t1 6, employee_2.t2 10, employee_2.t3 10, employee_3.t1 8, employee_3.t2 16, employee_3.t3 11 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_063 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'task_alpha': 11, 'task_beta': 13, 'task_gamma': 15}
    - worker_B: {'task_alpha': 9, 'task_beta': 12, 'task_gamma': 15}
    - worker_C: {'task_alpha': 11, 'task_beta': 14, 'task_gamma': 8}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> task_alpha: 11, task_beta: 13, task_gamma: 15; worker_B -> task_alpha: 9, task_beta: 12, task_gamma: 15; worker_C -> task_alpha: 11, task_beta: 14, task_gamma: 8 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.task_alpha 11, worker_A.task_beta 13, worker_A.task_gamma 15, worker_B.task_alpha 9, worker_B.task_beta 12, worker_B.task_gamma 15, worker_C.task_alpha 11, worker_C.task_beta 14, worker_C.task_gamma 8 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_064 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'t1': 11, 't2': 10, 't3': 14}
    - employee_2: {'t1': 10, 't2': 11, 't3': 10}
    - employee_3: {'t1': 9, 't2': 14, 't3': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> t1: 11, t2: 10, t3: 14; employee_2 -> t1: 10, t2: 11, t3: 10; employee_3 -> t1: 9, t2: 14, t3: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.t1 11, employee_1.t2 10, employee_1.t3 14, employee_2.t1 10, employee_2.t2 11, employee_2.t3 10, employee_3.t1 9, employee_3.t2 14, employee_3.t3 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_065 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'job_1': 8, 'job_2': 11, 'job_3': 12}
    - employee_2: {'job_1': 9, 'job_2': 11, 'job_3': 13}
    - employee_3: {'job_1': 8, 'job_2': 15, 'job_3': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> job_1: 8, job_2: 11, job_3: 12; employee_2 -> job_1: 9, job_2: 11, job_3: 13; employee_3 -> job_1: 8, job_2: 15, job_3: 11 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.job_1 8, employee_1.job_2 11, employee_1.job_3 12, employee_2.job_1 9, employee_2.job_2 11, employee_2.job_3 13, employee_3.job_1 8, employee_3.job_2 15, employee_3.job_3 11 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_066 — Assignment

**Description:** Assign w1, w2 and w3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'task_alpha': 9, 'task_beta': 9, 'task_gamma': 18}
    - w2: {'task_alpha': 8, 'task_beta': 10, 'task_gamma': 14}
    - w3: {'task_alpha': 7, 'task_beta': 17, 'task_gamma': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> task_alpha: 9, task_beta: 9, task_gamma: 18; w2 -> task_alpha: 8, task_beta: 10, task_gamma: 14; w3 -> task_alpha: 7, task_beta: 17, task_gamma: 12 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.task_alpha 9, w1.task_beta 9, w1.task_gamma 18, w2.task_alpha 8, w2.task_beta 10, w2.task_gamma 14, w3.task_alpha 7, w3.task_beta 17, w3.task_gamma 12 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_067 — Assignment

**Description:** Assign w1, w2 and w3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'job_1': 10, 'job_2': 11, 'job_3': 16}
    - w2: {'job_1': 8, 'job_2': 12, 'job_3': 13}
    - w3: {'job_1': 7, 'job_2': 16, 'job_3': 8}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> job_1: 10, job_2: 11, job_3: 16; w2 -> job_1: 8, job_2: 12, job_3: 13; w3 -> job_1: 7, job_2: 16, job_3: 8 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.job_1 10, w1.job_2 11, w1.job_3 16, w2.job_1 8, w2.job_2 12, w2.job_3 13, w3.job_1 7, w3.job_2 16, w3.job_3 8 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_068 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'task_alpha': 8, 'task_beta': 15, 'task_gamma': 14}
    - employee_2: {'task_alpha': 8, 'task_beta': 10, 'task_gamma': 12}
    - employee_3: {'task_alpha': 11, 'task_beta': 12, 'task_gamma': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> task_alpha: 8, task_beta: 15, task_gamma: 14; employee_2 -> task_alpha: 8, task_beta: 10, task_gamma: 12; employee_3 -> task_alpha: 11, task_beta: 12, task_gamma: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.task_alpha 8, employee_1.task_beta 15, employee_1.task_gamma 14, employee_2.task_alpha 8, employee_2.task_beta 10, employee_2.task_gamma 12, employee_3.task_alpha 11, employee_3.task_beta 12, employee_3.task_gamma 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_069 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'task_alpha': 12, 'task_beta': 12, 'task_gamma': 18}
    - worker_B: {'task_alpha': 7, 'task_beta': 13, 'task_gamma': 10}
    - worker_C: {'task_alpha': 11, 'task_beta': 17, 'task_gamma': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> task_alpha: 12, task_beta: 12, task_gamma: 18; worker_B -> task_alpha: 7, task_beta: 13, task_gamma: 10; worker_C -> task_alpha: 11, task_beta: 17, task_gamma: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.task_alpha 12, worker_A.task_beta 12, worker_A.task_gamma 18, worker_B.task_alpha 7, worker_B.task_beta 13, worker_B.task_gamma 10, worker_C.task_alpha 11, worker_C.task_beta 17, worker_C.task_gamma 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_070 — Assignment

**Description:** Assign w1, w2 and w3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'task_alpha': 11, 'task_beta': 12, 'task_gamma': 17}
    - w2: {'task_alpha': 8, 'task_beta': 11, 'task_gamma': 16}
    - w3: {'task_alpha': 7, 'task_beta': 16, 'task_gamma': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> task_alpha: 11, task_beta: 12, task_gamma: 17; w2 -> task_alpha: 8, task_beta: 11, task_gamma: 16; w3 -> task_alpha: 7, task_beta: 16, task_gamma: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.task_alpha 11, w1.task_beta 12, w1.task_gamma 17, w2.task_alpha 8, w2.task_beta 11, w2.task_gamma 16, w3.task_alpha 7, w3.task_beta 16, w3.task_gamma 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_071 — Assignment

**Description:** Assign w1, w2 and w3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'task_alpha': 12, 'task_beta': 15, 'task_gamma': 14}
    - w2: {'task_alpha': 10, 'task_beta': 12, 'task_gamma': 14}
    - w3: {'task_alpha': 8, 'task_beta': 15, 'task_gamma': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> task_alpha: 12, task_beta: 15, task_gamma: 14; w2 -> task_alpha: 10, task_beta: 12, task_gamma: 14; w3 -> task_alpha: 8, task_beta: 15, task_gamma: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.task_alpha 12, w1.task_beta 15, w1.task_gamma 14, w2.task_alpha 10, w2.task_beta 12, w2.task_gamma 14, w3.task_alpha 8, w3.task_beta 15, w3.task_gamma 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_072 — Assignment

**Description:** Assign w1, w2 and w3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'job_1': 11, 'job_2': 10, 'job_3': 12}
    - w2: {'job_1': 7, 'job_2': 14, 'job_3': 10}
    - w3: {'job_1': 7, 'job_2': 15, 'job_3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> job_1: 11, job_2: 10, job_3: 12; w2 -> job_1: 7, job_2: 14, job_3: 10; w3 -> job_1: 7, job_2: 15, job_3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.job_1 11, w1.job_2 10, w1.job_3 12, w2.job_1 7, w2.job_2 14, w2.job_3 10, w3.job_1 7, w3.job_2 15, w3.job_3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_073 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'job_1': 11, 'job_2': 14, 'job_3': 14}
    - employee_2: {'job_1': 7, 'job_2': 9, 'job_3': 14}
    - employee_3: {'job_1': 8, 'job_2': 16, 'job_3': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> job_1: 11, job_2: 14, job_3: 14; employee_2 -> job_1: 7, job_2: 9, job_3: 14; employee_3 -> job_1: 8, job_2: 16, job_3: 12 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.job_1 11, employee_1.job_2 14, employee_1.job_3 14, employee_2.job_1 7, employee_2.job_2 9, employee_2.job_3 14, employee_3.job_1 8, employee_3.job_2 16, employee_3.job_3 12 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_074 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'t1': 9, 't2': 11, 't3': 11}
    - employee_2: {'t1': 8, 't2': 12, 't3': 13}
    - employee_3: {'t1': 8, 't2': 15, 't3': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> t1: 9, t2: 11, t3: 11; employee_2 -> t1: 8, t2: 12, t3: 13; employee_3 -> t1: 8, t2: 15, t3: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.t1 9, employee_1.t2 11, employee_1.t3 11, employee_2.t1 8, employee_2.t2 12, employee_2.t3 13, employee_3.t1 8, employee_3.t2 15, employee_3.t3 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_075 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'task_alpha': 9, 'task_beta': 14, 'task_gamma': 14}
    - employee_2: {'task_alpha': 8, 'task_beta': 13, 'task_gamma': 15}
    - employee_3: {'task_alpha': 8, 'task_beta': 14, 'task_gamma': 8}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> task_alpha: 9, task_beta: 14, task_gamma: 14; employee_2 -> task_alpha: 8, task_beta: 13, task_gamma: 15; employee_3 -> task_alpha: 8, task_beta: 14, task_gamma: 8 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.task_alpha 9, employee_1.task_beta 14, employee_1.task_gamma 14, employee_2.task_alpha 8, employee_2.task_beta 13, employee_2.task_gamma 15, employee_3.task_alpha 8, employee_3.task_beta 14, employee_3.task_gamma 8 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_076 — Assignment

**Description:** Assign w1, w2 and w3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'t1': 8, 't2': 12, 't3': 17}
    - w2: {'t1': 10, 't2': 14, 't3': 13}
    - w3: {'t1': 7, 't2': 12, 't3': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> t1: 8, t2: 12, t3: 17; w2 -> t1: 10, t2: 14, t3: 13; w3 -> t1: 7, t2: 12, t3: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.t1 8, w1.t2 12, w1.t3 17, w2.t1 10, w2.t2 14, w2.t3 13, w3.t1 7, w3.t2 12, w3.t3 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_077 — Assignment

**Description:** Assign w1, w2 and w3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'job_1': 8, 'job_2': 13, 'job_3': 16}
    - w2: {'job_1': 8, 'job_2': 8, 'job_3': 11}
    - w3: {'job_1': 7, 'job_2': 17, 'job_3': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> job_1: 8, job_2: 13, job_3: 16; w2 -> job_1: 8, job_2: 8, job_3: 11; w3 -> job_1: 7, job_2: 17, job_3: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.job_1 8, w1.job_2 13, w1.job_3 16, w2.job_1 8, w2.job_2 8, w2.job_3 11, w3.job_1 7, w3.job_2 17, w3.job_3 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_078 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'t1': 10, 't2': 13, 't3': 17}
    - worker_B: {'t1': 8, 't2': 10, 't3': 11}
    - worker_C: {'t1': 8, 't2': 17, 't3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> t1: 10, t2: 13, t3: 17; worker_B -> t1: 8, t2: 10, t3: 11; worker_C -> t1: 8, t2: 17, t3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.t1 10, worker_A.t2 13, worker_A.t3 17, worker_B.t1 8, worker_B.t2 10, worker_B.t3 11, worker_C.t1 8, worker_C.t2 17, worker_C.t3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_079 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'t1': 9, 't2': 14, 't3': 18}
    - employee_2: {'t1': 6, 't2': 9, 't3': 14}
    - employee_3: {'t1': 9, 't2': 11, 't3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> t1: 9, t2: 14, t3: 18; employee_2 -> t1: 6, t2: 9, t3: 14; employee_3 -> t1: 9, t2: 11, t3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.t1 9, employee_1.t2 14, employee_1.t3 18, employee_2.t1 6, employee_2.t2 9, employee_2.t3 14, employee_3.t1 9, employee_3.t2 11, employee_3.t3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_080 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'task_alpha': 9, 'task_beta': 14, 'task_gamma': 15}
    - worker_B: {'task_alpha': 7, 'task_beta': 13, 'task_gamma': 16}
    - worker_C: {'task_alpha': 8, 'task_beta': 11, 'task_gamma': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> task_alpha: 9, task_beta: 14, task_gamma: 15; worker_B -> task_alpha: 7, task_beta: 13, task_gamma: 16; worker_C -> task_alpha: 8, task_beta: 11, task_gamma: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.task_alpha 9, worker_A.task_beta 14, worker_A.task_gamma 15, worker_B.task_alpha 7, worker_B.task_beta 13, worker_B.task_gamma 16, worker_C.task_alpha 8, worker_C.task_beta 11, worker_C.task_gamma 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_081 — Assignment

**Description:** Assign w1, w2 and w3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'t1': 8, 't2': 13, 't3': 12}
    - w2: {'t1': 9, 't2': 11, 't3': 13}
    - w3: {'t1': 7, 't2': 15, 't3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> t1: 8, t2: 13, t3: 12; w2 -> t1: 9, t2: 11, t3: 13; w3 -> t1: 7, t2: 15, t3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.t1 8, w1.t2 13, w1.t3 12, w2.t1 9, w2.t2 11, w2.t3 13, w3.t1 7, w3.t2 15, w3.t3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_082 — Assignment

**Description:** Assign w1, w2 and w3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'job_1': 10, 'job_2': 11, 'job_3': 16}
    - w2: {'job_1': 7, 'job_2': 11, 'job_3': 16}
    - w3: {'job_1': 10, 'job_2': 15, 'job_3': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> job_1: 10, job_2: 11, job_3: 16; w2 -> job_1: 7, job_2: 11, job_3: 16; w3 -> job_1: 10, job_2: 15, job_3: 12 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.job_1 10, w1.job_2 11, w1.job_3 16, w2.job_1 7, w2.job_2 11, w2.job_3 16, w3.job_1 10, w3.job_2 15, w3.job_3 12 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_083 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'t1': 9, 't2': 13, 't3': 16}
    - worker_B: {'t1': 8, 't2': 11, 't3': 12}
    - worker_C: {'t1': 9, 't2': 13, 't3': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> t1: 9, t2: 13, t3: 16; worker_B -> t1: 8, t2: 11, t3: 12; worker_C -> t1: 9, t2: 13, t3: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.t1 9, worker_A.t2 13, worker_A.t3 16, worker_B.t1 8, worker_B.t2 11, worker_B.t3 12, worker_C.t1 9, worker_C.t2 13, worker_C.t3 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_084 — Assignment

**Description:** Assign w1, w2 and w3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'task_alpha': 9, 'task_beta': 13, 'task_gamma': 12}
    - w2: {'task_alpha': 8, 'task_beta': 11, 'task_gamma': 12}
    - w3: {'task_alpha': 8, 'task_beta': 15, 'task_gamma': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> task_alpha: 9, task_beta: 13, task_gamma: 12; w2 -> task_alpha: 8, task_beta: 11, task_gamma: 12; w3 -> task_alpha: 8, task_beta: 15, task_gamma: 11 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.task_alpha 9, w1.task_beta 13, w1.task_gamma 12, w2.task_alpha 8, w2.task_beta 11, w2.task_gamma 12, w3.task_alpha 8, w3.task_beta 15, w3.task_gamma 11 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_085 — Assignment

**Description:** Assign w1, w2 and w3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'task_alpha': 10, 'task_beta': 11, 'task_gamma': 15}
    - w2: {'task_alpha': 7, 'task_beta': 14, 'task_gamma': 11}
    - w3: {'task_alpha': 8, 'task_beta': 11, 'task_gamma': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> task_alpha: 10, task_beta: 11, task_gamma: 15; w2 -> task_alpha: 7, task_beta: 14, task_gamma: 11; w3 -> task_alpha: 8, task_beta: 11, task_gamma: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.task_alpha 10, w1.task_beta 11, w1.task_gamma 15, w2.task_alpha 7, w2.task_beta 14, w2.task_gamma 11, w3.task_alpha 8, w3.task_beta 11, w3.task_gamma 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_086 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'task_alpha': 8, 'task_beta': 9, 'task_gamma': 17}
    - worker_B: {'task_alpha': 10, 'task_beta': 13, 'task_gamma': 11}
    - worker_C: {'task_alpha': 8, 'task_beta': 17, 'task_gamma': 8}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> task_alpha: 8, task_beta: 9, task_gamma: 17; worker_B -> task_alpha: 10, task_beta: 13, task_gamma: 11; worker_C -> task_alpha: 8, task_beta: 17, task_gamma: 8 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.task_alpha 8, worker_A.task_beta 9, worker_A.task_gamma 17, worker_B.task_alpha 10, worker_B.task_beta 13, worker_B.task_gamma 11, worker_C.task_alpha 8, worker_C.task_beta 17, worker_C.task_gamma 8 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_087 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'t1': 12, 't2': 12, 't3': 19}
    - worker_B: {'t1': 9, 't2': 12, 't3': 12}
    - worker_C: {'t1': 8, 't2': 16, 't3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> t1: 12, t2: 12, t3: 19; worker_B -> t1: 9, t2: 12, t3: 12; worker_C -> t1: 8, t2: 16, t3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.t1 12, worker_A.t2 12, worker_A.t3 19, worker_B.t1 9, worker_B.t2 12, worker_B.t3 12, worker_C.t1 8, worker_C.t2 16, worker_C.t3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_088 — Assignment

**Description:** Assign employee_1, employee_2 and employee_3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - employee_1: {'job_1': 9, 'job_2': 12, 'job_3': 12}
    - employee_2: {'job_1': 7, 'job_2': 13, 'job_3': 10}
    - employee_3: {'job_1': 9, 'job_2': 16, 'job_3': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: employee_1, employee_2, employee_3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: employee_1 -> job_1: 9, job_2: 12, job_3: 12; employee_2 -> job_1: 7, job_2: 13, job_3: 10; employee_3 -> job_1: 9, job_2: 16, job_3: 12 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / employee_1, employee_2, employee_3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / employee_1.job_1 9, employee_1.job_2 12, employee_1.job_3 12, employee_2.job_1 7, employee_2.job_2 13, employee_2.job_3 10, employee_3.job_1 9, employee_3.job_2 16, employee_3.job_3 12 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_089 — Assignment

**Description:** Assign w1, w2 and w3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'task_alpha': 9, 'task_beta': 15, 'task_gamma': 16}
    - w2: {'task_alpha': 8, 'task_beta': 10, 'task_gamma': 13}
    - w3: {'task_alpha': 8, 'task_beta': 12, 'task_gamma': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> task_alpha: 9, task_beta: 15, task_gamma: 16; w2 -> task_alpha: 8, task_beta: 10, task_gamma: 13; w3 -> task_alpha: 8, task_beta: 12, task_gamma: 12 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.task_alpha 9, w1.task_beta 15, w1.task_gamma 16, w2.task_alpha 8, w2.task_beta 10, w2.task_gamma 13, w3.task_alpha 8, w3.task_beta 12, w3.task_gamma 12 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_090 — Assignment

**Description:** Assign w1, w2 and w3 to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'task_alpha': 10, 'task_beta': 9, 'task_gamma': 12}
    - w2: {'task_alpha': 7, 'task_beta': 13, 'task_gamma': 14}
    - w3: {'task_alpha': 7, 'task_beta': 14, 'task_gamma': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> task_alpha: 10, task_beta: 9, task_gamma: 12; w2 -> task_alpha: 7, task_beta: 13, task_gamma: 14; w3 -> task_alpha: 7, task_beta: 14, task_gamma: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.task_alpha 10, w1.task_beta 9, w1.task_gamma 12, w2.task_alpha 7, w2.task_beta 13, w2.task_gamma 14, w3.task_alpha 7, w3.task_beta 14, w3.task_gamma 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_091 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'job_1': 8, 'job_2': 12, 'job_3': 19}
    - worker_B: {'job_1': 8, 'job_2': 12, 'job_3': 16}
    - worker_C: {'job_1': 10, 'job_2': 15, 'job_3': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> job_1: 8, job_2: 12, job_3: 19; worker_B -> job_1: 8, job_2: 12, job_3: 16; worker_C -> job_1: 10, job_2: 15, job_3: 12 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.job_1 8, worker_A.job_2 12, worker_A.job_3 19, worker_B.job_1 8, worker_B.job_2 12, worker_B.job_3 16, worker_C.job_1 10, worker_C.job_2 15, worker_C.job_3 12 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_092 — Assignment

**Description:** Assign w1, w2 and w3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'t1': 8, 't2': 12, 't3': 15}
    - w2: {'t1': 9, 't2': 9, 't3': 11}
    - w3: {'t1': 9, 't2': 15, 't3': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> t1: 8, t2: 12, t3: 15; w2 -> t1: 9, t2: 9, t3: 11; w3 -> t1: 9, t2: 15, t3: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.t1 8, w1.t2 12, w1.t3 15, w2.t1 9, w2.t2 9, w2.t3 11, w3.t1 9, w3.t2 15, w3.t3 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_093 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'t1': 8, 't2': 15, 't3': 15}
    - worker_B: {'t1': 8, 't2': 13, 't3': 14}
    - worker_C: {'t1': 9, 't2': 12, 't3': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> t1: 8, t2: 15, t3: 15; worker_B -> t1: 8, t2: 13, t3: 14; worker_C -> t1: 9, t2: 12, t3: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.t1 8, worker_A.t2 15, worker_A.t3 15, worker_B.t1 8, worker_B.t2 13, worker_B.t3 14, worker_C.t1 9, worker_C.t2 12, worker_C.t3 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_094 — Assignment

**Description:** Assign w1, w2 and w3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'job_1': 10, 'job_2': 9, 'job_3': 17}
    - w2: {'job_1': 7, 'job_2': 14, 'job_3': 13}
    - w3: {'job_1': 8, 'job_2': 14, 'job_3': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> job_1: 10, job_2: 9, job_3: 17; w2 -> job_1: 7, job_2: 14, job_3: 13; w3 -> job_1: 8, job_2: 14, job_3: 11 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.job_1 10, w1.job_2 9, w1.job_3 17, w2.job_1 7, w2.job_2 14, w2.job_3 13, w3.job_1 8, w3.job_2 14, w3.job_3 11 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_095 — Assignment

**Description:** Assign w1, w2 and w3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'job_1': 10, 'job_2': 15, 'job_3': 19}
    - w2: {'job_1': 9, 'job_2': 11, 'job_3': 13}
    - w3: {'job_1': 8, 'job_2': 15, 'job_3': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> job_1: 10, job_2: 15, job_3: 19; w2 -> job_1: 9, job_2: 11, job_3: 13; w3 -> job_1: 8, job_2: 15, job_3: 9 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.job_1 10, w1.job_2 15, w1.job_3 19, w2.job_1 9, w2.job_2 11, w2.job_3 13, w3.job_1 8, w3.job_2 15, w3.job_3 9 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_096 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'task_alpha': 11, 'task_beta': 13, 'task_gamma': 18}
    - worker_B: {'task_alpha': 9, 'task_beta': 11, 'task_gamma': 16}
    - worker_C: {'task_alpha': 11, 'task_beta': 12, 'task_gamma': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> task_alpha: 11, task_beta: 13, task_gamma: 18; worker_B -> task_alpha: 9, task_beta: 11, task_gamma: 16; worker_C -> task_alpha: 11, task_beta: 12, task_gamma: 10 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.task_alpha 11, worker_A.task_beta 13, worker_A.task_gamma 18, worker_B.task_alpha 9, worker_B.task_beta 11, worker_B.task_gamma 16, worker_C.task_alpha 11, worker_C.task_beta 12, worker_C.task_gamma 10 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_097 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'job_1': 9, 'job_2': 11, 'job_3': 14}
    - worker_B: {'job_1': 8, 'job_2': 13, 'job_3': 11}
    - worker_C: {'job_1': 10, 'job_2': 16, 'job_3': 8}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> job_1: 9, job_2: 11, job_3: 14; worker_B -> job_1: 8, job_2: 13, job_3: 11; worker_C -> job_1: 10, job_2: 16, job_3: 8 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.job_1 9, worker_A.job_2 11, worker_A.job_3 14, worker_B.job_1 8, worker_B.job_2 13, worker_B.job_3 11, worker_C.job_1 10, worker_C.job_2 16, worker_C.job_3 8 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_098 — Assignment

**Description:** Assign w1, w2 and w3 to t1, t2 and t3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'t1': 12, 't2': 11, 't3': 17}
    - w2: {'t1': 7, 't2': 12, 't3': 12}
    - w3: {'t1': 9, 't2': 16, 't3': 8}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: t1, t2, t3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> t1: 12, t2: 11, t3: 17; w2 -> t1: 7, t2: 12, t3: 12; w3 -> t1: 9, t2: 16, t3: 8 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / t1, t2, t3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.t1 12, w1.t2 11, w1.t3 17, w2.t1 7, w2.t2 12, w2.t3 12, w3.t1 9, w3.t2 16, w3.t3 8 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_099 — Assignment

**Description:** Assign w1, w2 and w3 to job_1, job_2 and job_3 to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - w1: {'job_1': 12, 'job_2': 14, 'job_3': 12}
    - w2: {'job_1': 7, 'job_2': 13, 'job_3': 11}
    - w3: {'job_1': 11, 'job_2': 17, 'job_3': 8}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: w1, w2, w3 (available resources)
- Tasks: job_1, job_2, job_3 (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: w1 -> job_1: 12, job_2: 14, job_3: 12; w2 -> job_1: 7, job_2: 13, job_3: 11; w3 -> job_1: 11, job_2: 17, job_3: 8 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / w1, w2, w3 /
    j   tasks      / job_1, job_2, job_3 /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / w1.job_1 12, w1.job_2 14, w1.job_3 12, w2.job_1 7, w2.job_2 13, w2.job_3 11, w3.job_1 11, w3.job_2 17, w3.job_3 8 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_100 — Assignment

**Description:** Assign worker_A, worker_B and worker_C to task_alpha, task_beta and task_gamma to minimize total assignment cost. Each worker can be assigned to exactly one task and each task must be completed by exactly one worker.

**Supplementary Tables:**
- cost_matrix:
    - worker_A: {'task_alpha': 10, 'task_beta': 9, 'task_gamma': 15}
    - worker_B: {'task_alpha': 6, 'task_beta': 12, 'task_gamma': 15}
    - worker_C: {'task_alpha': 10, 'task_beta': 14, 'task_gamma': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Optimal Assignment

SETS IDENTIFICATION:
- Workers: worker_A, worker_B, worker_C (available resources)
- Tasks: task_alpha, task_beta, task_gamma (jobs to be completed)

PARAMETERS DEFINITION:
- Cost matrix: worker_A -> task_alpha: 10, task_beta: 9, task_gamma: 15; worker_B -> task_alpha: 6, task_beta: 12, task_gamma: 15; worker_C -> task_alpha: 10, task_beta: 14, task_gamma: 11 (cost of each worker-task assignment)

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
- Minimize total assignment cost
```

**Generated GAMS Program:**

```GAMS
Sets
    i   workers    / worker_A, worker_B, worker_C /
    j   tasks      / task_alpha, task_beta, task_gamma /;

Parameters
    c(i,j)  cost of assigning worker i to task j
        / worker_A.task_alpha 10, worker_A.task_beta 9, worker_A.task_gamma 15, worker_B.task_alpha 6, worker_B.task_beta 12, worker_B.task_gamma 15, worker_C.task_alpha 10, worker_C.task_beta 14, worker_C.task_gamma 11 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=30.0

---

## Problem prob_101 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 9, 'value': 24}
    - laptop: {'weight': 17, 'value': 30}
    - camera: {'weight': 32, 'value': 26}
    - phone: {'weight': 37, 'value': 68}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 9; laptop: 17; camera: 32; phone: 37
- Values: book: 24; laptop: 30; camera: 26; phone: 68  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 9, laptop 17, camera 32, phone 37 /
    v(i)    value of item i
        / book 24, laptop 30, camera 26, phone 68 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=98.0

---

## Problem prob_102 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 12, 'value': 12}
    - item2: {'weight': 21, 'value': 42}
    - item3: {'weight': 21, 'value': 41}
    - item4: {'weight': 38, 'value': 31}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 12; item2: 21; item3: 21; item4: 38
- Values: item1: 12; item2: 42; item3: 41; item4: 31  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 12, item2 21, item3 21, item4 38 /
    v(i)    value of item i
        / item1 12, item2 42, item3 41, item4 31 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=114.0

---

## Problem prob_103 — Knapsack

**Description:** Select items from tool_A, tool_B, tool_C and tool_D for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - tool_A: {'weight': 12, 'value': 25}
    - tool_B: {'weight': 16, 'value': 26}
    - tool_C: {'weight': 31, 'value': 32}
    - tool_D: {'weight': 31, 'value': 38}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: tool_A, tool_B, tool_C, tool_D (available items for selection)

PARAMETERS DEFINITION:
- Weights: tool_A: 12; tool_B: 16; tool_C: 31; tool_D: 31
- Values: tool_A: 25; tool_B: 26; tool_C: 32; tool_D: 38  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / tool_A, tool_B, tool_C, tool_D /;

Parameters
    w(i)    weight of item i
        / tool_A 12, tool_B 16, tool_C 31, tool_D 31 /
    v(i)    value of item i
        / tool_A 25, tool_B 26, tool_C 32, tool_D 38 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=96.0

---

## Problem prob_104 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 7, 'value': 21}
    - laptop: {'weight': 19, 'value': 42}
    - camera: {'weight': 24, 'value': 25}
    - phone: {'weight': 35, 'value': 47}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 7; laptop: 19; camera: 24; phone: 35
- Values: book: 21; laptop: 42; camera: 25; phone: 47  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 7, laptop 19, camera 24, phone 35 /
    v(i)    value of item i
        / book 21, laptop 42, camera 25, phone 47 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=89.0

---

## Problem prob_105 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 50 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 12, 'value': 23}
    - item2: {'weight': 21, 'value': 40}
    - item3: {'weight': 29, 'value': 42}
    - item4: {'weight': 42, 'value': 37}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 12; item2: 21; item3: 29; item4: 42
- Values: item1: 23; item2: 40; item3: 42; item4: 37  
- Capacity: 50 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 12, item2 21, item3 29, item4 42 /
    v(i)    value of item i
        / item1 23, item2 40, item3 42, item4 37 /;

Scalar capacity / 50 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=82.0

---

## Problem prob_106 — Knapsack

**Description:** Select items from tool_A, tool_B, tool_C and tool_D for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - tool_A: {'weight': 11, 'value': 24}
    - tool_B: {'weight': 20, 'value': 19}
    - tool_C: {'weight': 29, 'value': 49}
    - tool_D: {'weight': 30, 'value': 57}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: tool_A, tool_B, tool_C, tool_D (available items for selection)

PARAMETERS DEFINITION:
- Weights: tool_A: 11; tool_B: 20; tool_C: 29; tool_D: 30
- Values: tool_A: 24; tool_B: 19; tool_C: 49; tool_D: 57  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / tool_A, tool_B, tool_C, tool_D /;

Parameters
    w(i)    weight of item i
        / tool_A 11, tool_B 20, tool_C 29, tool_D 30 /
    v(i)    value of item i
        / tool_A 24, tool_B 19, tool_C 49, tool_D 57 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=106.0

---

## Problem prob_107 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 70 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 11, 'value': 13}
    - laptop: {'weight': 17, 'value': 32}
    - camera: {'weight': 29, 'value': 27}
    - phone: {'weight': 48, 'value': 40}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 11; laptop: 17; camera: 29; phone: 48
- Values: book: 13; laptop: 32; camera: 27; phone: 40  
- Capacity: 70 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 11, laptop 17, camera 29, phone 48 /
    v(i)    value of item i
        / book 13, laptop 32, camera 27, phone 40 /;

Scalar capacity / 70 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=72.0

---

## Problem prob_108 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 8, 'value': 20}
    - laptop: {'weight': 25, 'value': 39}
    - camera: {'weight': 34, 'value': 48}
    - phone: {'weight': 47, 'value': 61}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 8; laptop: 25; camera: 34; phone: 47
- Values: book: 20; laptop: 39; camera: 48; phone: 61  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 8, laptop 25, camera 34, phone 47 /
    v(i)    value of item i
        / book 20, laptop 39, camera 48, phone 61 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=87.0

---

## Problem prob_109 — Knapsack

**Description:** Select items from tool_A, tool_B, tool_C and tool_D for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - tool_A: {'weight': 11, 'value': 27}
    - tool_B: {'weight': 25, 'value': 23}
    - tool_C: {'weight': 33, 'value': 40}
    - tool_D: {'weight': 40, 'value': 61}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: tool_A, tool_B, tool_C, tool_D (available items for selection)

PARAMETERS DEFINITION:
- Weights: tool_A: 11; tool_B: 25; tool_C: 33; tool_D: 40
- Values: tool_A: 27; tool_B: 23; tool_C: 40; tool_D: 61  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / tool_A, tool_B, tool_C, tool_D /;

Parameters
    w(i)    weight of item i
        / tool_A 11, tool_B 25, tool_C 33, tool_D 40 /
    v(i)    value of item i
        / tool_A 27, tool_B 23, tool_C 40, tool_D 61 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=88.0

---

## Problem prob_110 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 50 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 8, 'value': 27}
    - laptop: {'weight': 23, 'value': 19}
    - camera: {'weight': 22, 'value': 31}
    - phone: {'weight': 36, 'value': 50}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 8; laptop: 23; camera: 22; phone: 36
- Values: book: 27; laptop: 19; camera: 31; phone: 50  
- Capacity: 50 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 8, laptop 23, camera 22, phone 36 /
    v(i)    value of item i
        / book 27, laptop 19, camera 31, phone 50 /;

Scalar capacity / 50 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=77.0

---

## Problem prob_111 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 8, 'value': 28}
    - item2: {'weight': 16, 'value': 28}
    - item3: {'weight': 22, 'value': 25}
    - item4: {'weight': 42, 'value': 31}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 8; item2: 16; item3: 22; item4: 42
- Values: item1: 28; item2: 28; item3: 25; item4: 31  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 8, item2 16, item3 22, item4 42 /
    v(i)    value of item i
        / item1 28, item2 28, item3 25, item4 31 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=87.0

---

## Problem prob_112 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 9, 'value': 21}
    - item2: {'weight': 22, 'value': 35}
    - item3: {'weight': 28, 'value': 28}
    - item4: {'weight': 50, 'value': 62}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 9; item2: 22; item3: 28; item4: 50
- Values: item1: 21; item2: 35; item3: 28; item4: 62  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 9, item2 22, item3 28, item4 50 /
    v(i)    value of item i
        / item1 21, item2 35, item3 28, item4 62 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=84.0

---

## Problem prob_113 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 8, 'value': 12}
    - item2: {'weight': 14, 'value': 21}
    - item3: {'weight': 26, 'value': 25}
    - item4: {'weight': 40, 'value': 63}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 8; item2: 14; item3: 26; item4: 40
- Values: item1: 12; item2: 21; item3: 25; item4: 63  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 8, item2 14, item3 26, item4 40 /
    v(i)    value of item i
        / item1 12, item2 21, item3 25, item4 63 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=84.0

---

## Problem prob_114 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 50 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 13, 'value': 25}
    - laptop: {'weight': 19, 'value': 33}
    - camera: {'weight': 38, 'value': 29}
    - phone: {'weight': 51, 'value': 59}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 13; laptop: 19; camera: 38; phone: 51
- Values: book: 25; laptop: 33; camera: 29; phone: 59  
- Capacity: 50 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 13, laptop 19, camera 38, phone 51 /
    v(i)    value of item i
        / book 25, laptop 33, camera 29, phone 59 /;

Scalar capacity / 50 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=58.0

---

## Problem prob_115 — Knapsack

**Description:** Select items from tool_A, tool_B, tool_C and tool_D for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - tool_A: {'weight': 11, 'value': 25}
    - tool_B: {'weight': 25, 'value': 42}
    - tool_C: {'weight': 38, 'value': 27}
    - tool_D: {'weight': 33, 'value': 66}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: tool_A, tool_B, tool_C, tool_D (available items for selection)

PARAMETERS DEFINITION:
- Weights: tool_A: 11; tool_B: 25; tool_C: 38; tool_D: 33
- Values: tool_A: 25; tool_B: 42; tool_C: 27; tool_D: 66  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / tool_A, tool_B, tool_C, tool_D /;

Parameters
    w(i)    weight of item i
        / tool_A 11, tool_B 25, tool_C 38, tool_D 33 /
    v(i)    value of item i
        / tool_A 25, tool_B 42, tool_C 27, tool_D 66 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=133.0

---

## Problem prob_116 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 70 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 13, 'value': 21}
    - laptop: {'weight': 20, 'value': 33}
    - camera: {'weight': 30, 'value': 41}
    - phone: {'weight': 33, 'value': 37}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 13; laptop: 20; camera: 30; phone: 33
- Values: book: 21; laptop: 33; camera: 41; phone: 37  
- Capacity: 70 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 13, laptop 20, camera 30, phone 33 /
    v(i)    value of item i
        / book 21, laptop 33, camera 41, phone 37 /;

Scalar capacity / 70 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=95.0

---

## Problem prob_117 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 50 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 7, 'value': 15}
    - item2: {'weight': 25, 'value': 34}
    - item3: {'weight': 25, 'value': 52}
    - item4: {'weight': 31, 'value': 53}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 7; item2: 25; item3: 25; item4: 31
- Values: item1: 15; item2: 34; item3: 52; item4: 53  
- Capacity: 50 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 7, item2 25, item3 25, item4 31 /
    v(i)    value of item i
        / item1 15, item2 34, item3 52, item4 53 /;

Scalar capacity / 50 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=86.0

---

## Problem prob_118 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 11, 'value': 20}
    - item2: {'weight': 15, 'value': 21}
    - item3: {'weight': 28, 'value': 42}
    - item4: {'weight': 49, 'value': 55}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 11; item2: 15; item3: 28; item4: 49
- Values: item1: 20; item2: 21; item3: 42; item4: 55  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 11, item2 15, item3 28, item4 49 /
    v(i)    value of item i
        / item1 20, item2 21, item3 42, item4 55 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=97.0

---

## Problem prob_119 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 13, 'value': 22}
    - laptop: {'weight': 15, 'value': 33}
    - camera: {'weight': 23, 'value': 27}
    - phone: {'weight': 40, 'value': 49}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 13; laptop: 15; camera: 23; phone: 40
- Values: book: 22; laptop: 33; camera: 27; phone: 49  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 13, laptop 15, camera 23, phone 40 /
    v(i)    value of item i
        / book 22, laptop 33, camera 27, phone 49 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=109.0

---

## Problem prob_120 — Knapsack

**Description:** Select items from tool_A, tool_B, tool_C and tool_D for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - tool_A: {'weight': 9, 'value': 22}
    - tool_B: {'weight': 17, 'value': 20}
    - tool_C: {'weight': 24, 'value': 31}
    - tool_D: {'weight': 30, 'value': 40}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: tool_A, tool_B, tool_C, tool_D (available items for selection)

PARAMETERS DEFINITION:
- Weights: tool_A: 9; tool_B: 17; tool_C: 24; tool_D: 30
- Values: tool_A: 22; tool_B: 20; tool_C: 31; tool_D: 40  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / tool_A, tool_B, tool_C, tool_D /;

Parameters
    w(i)    weight of item i
        / tool_A 9, tool_B 17, tool_C 24, tool_D 30 /
    v(i)    value of item i
        / tool_A 22, tool_B 20, tool_C 31, tool_D 40 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=82.0

---

## Problem prob_121 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 70 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 7, 'value': 21}
    - laptop: {'weight': 14, 'value': 26}
    - camera: {'weight': 28, 'value': 52}
    - phone: {'weight': 41, 'value': 62}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 7; laptop: 14; camera: 28; phone: 41
- Values: book: 21; laptop: 26; camera: 52; phone: 62  
- Capacity: 70 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 7, laptop 14, camera 28, phone 41 /
    v(i)    value of item i
        / book 21, laptop 26, camera 52, phone 62 /;

Scalar capacity / 70 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=114.0

---

## Problem prob_122 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 12, 'value': 20}
    - item2: {'weight': 15, 'value': 27}
    - item3: {'weight': 27, 'value': 40}
    - item4: {'weight': 42, 'value': 67}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 12; item2: 15; item3: 27; item4: 42
- Values: item1: 20; item2: 27; item3: 40; item4: 67  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 12, item2 15, item3 27, item4 42 /
    v(i)    value of item i
        / item1 20, item2 27, item3 40, item4 67 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=94.0

---

## Problem prob_123 — Knapsack

**Description:** Select items from tool_A, tool_B, tool_C and tool_D for a knapsack with capacity 50 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - tool_A: {'weight': 8, 'value': 27}
    - tool_B: {'weight': 21, 'value': 20}
    - tool_C: {'weight': 37, 'value': 45}
    - tool_D: {'weight': 47, 'value': 63}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: tool_A, tool_B, tool_C, tool_D (available items for selection)

PARAMETERS DEFINITION:
- Weights: tool_A: 8; tool_B: 21; tool_C: 37; tool_D: 47
- Values: tool_A: 27; tool_B: 20; tool_C: 45; tool_D: 63  
- Capacity: 50 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / tool_A, tool_B, tool_C, tool_D /;

Parameters
    w(i)    weight of item i
        / tool_A 8, tool_B 21, tool_C 37, tool_D 47 /
    v(i)    value of item i
        / tool_A 27, tool_B 20, tool_C 45, tool_D 63 /;

Scalar capacity / 50 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=72.0

---

## Problem prob_124 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 9, 'value': 19}
    - laptop: {'weight': 22, 'value': 37}
    - camera: {'weight': 29, 'value': 24}
    - phone: {'weight': 37, 'value': 49}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 9; laptop: 22; camera: 29; phone: 37
- Values: book: 19; laptop: 37; camera: 24; phone: 49  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 9, laptop 22, camera 29, phone 37 /
    v(i)    value of item i
        / book 19, laptop 37, camera 24, phone 49 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=86.0

---

## Problem prob_125 — Knapsack

**Description:** Select items from tool_A, tool_B, tool_C and tool_D for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - tool_A: {'weight': 11, 'value': 26}
    - tool_B: {'weight': 15, 'value': 23}
    - tool_C: {'weight': 23, 'value': 40}
    - tool_D: {'weight': 39, 'value': 68}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: tool_A, tool_B, tool_C, tool_D (available items for selection)

PARAMETERS DEFINITION:
- Weights: tool_A: 11; tool_B: 15; tool_C: 23; tool_D: 39
- Values: tool_A: 26; tool_B: 23; tool_C: 40; tool_D: 68  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / tool_A, tool_B, tool_C, tool_D /;

Parameters
    w(i)    weight of item i
        / tool_A 11, tool_B 15, tool_C 23, tool_D 39 /
    v(i)    value of item i
        / tool_A 26, tool_B 23, tool_C 40, tool_D 68 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=94.0

---

## Problem prob_126 — Knapsack

**Description:** Select items from tool_A, tool_B, tool_C and tool_D for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - tool_A: {'weight': 9, 'value': 21}
    - tool_B: {'weight': 17, 'value': 19}
    - tool_C: {'weight': 32, 'value': 56}
    - tool_D: {'weight': 46, 'value': 51}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: tool_A, tool_B, tool_C, tool_D (available items for selection)

PARAMETERS DEFINITION:
- Weights: tool_A: 9; tool_B: 17; tool_C: 32; tool_D: 46
- Values: tool_A: 21; tool_B: 19; tool_C: 56; tool_D: 51  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / tool_A, tool_B, tool_C, tool_D /;

Parameters
    w(i)    weight of item i
        / tool_A 9, tool_B 17, tool_C 32, tool_D 46 /
    v(i)    value of item i
        / tool_A 21, tool_B 19, tool_C 56, tool_D 51 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=107.0

---

## Problem prob_127 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 11, 'value': 24}
    - item2: {'weight': 21, 'value': 39}
    - item3: {'weight': 32, 'value': 32}
    - item4: {'weight': 42, 'value': 60}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 11; item2: 21; item3: 32; item4: 42
- Values: item1: 24; item2: 39; item3: 32; item4: 60  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 11, item2 21, item3 32, item4 42 /
    v(i)    value of item i
        / item1 24, item2 39, item3 32, item4 60 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=84.0

---

## Problem prob_128 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 70 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 7, 'value': 16}
    - item2: {'weight': 14, 'value': 20}
    - item3: {'weight': 29, 'value': 52}
    - item4: {'weight': 40, 'value': 62}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 7; item2: 14; item3: 29; item4: 40
- Values: item1: 16; item2: 20; item3: 52; item4: 62  
- Capacity: 70 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 7, item2 14, item3 29, item4 40 /
    v(i)    value of item i
        / item1 16, item2 20, item3 52, item4 62 /;

Scalar capacity / 70 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=114.0

---

## Problem prob_129 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 11, 'value': 21}
    - item2: {'weight': 19, 'value': 22}
    - item3: {'weight': 37, 'value': 50}
    - item4: {'weight': 46, 'value': 31}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 11; item2: 19; item3: 37; item4: 46
- Values: item1: 21; item2: 22; item3: 50; item4: 31  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 11, item2 19, item3 37, item4 46 /
    v(i)    value of item i
        / item1 21, item2 22, item3 50, item4 31 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=93.0

---

## Problem prob_130 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 8, 'value': 19}
    - laptop: {'weight': 25, 'value': 27}
    - camera: {'weight': 28, 'value': 38}
    - phone: {'weight': 47, 'value': 65}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 8; laptop: 25; camera: 28; phone: 47
- Values: book: 19; laptop: 27; camera: 38; phone: 65  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 8, laptop 25, camera 28, phone 47 /
    v(i)    value of item i
        / book 19, laptop 27, camera 38, phone 65 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=84.0

---

## Problem prob_131 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 50 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 10, 'value': 24}
    - item2: {'weight': 21, 'value': 23}
    - item3: {'weight': 31, 'value': 46}
    - item4: {'weight': 34, 'value': 52}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 10; item2: 21; item3: 31; item4: 34
- Values: item1: 24; item2: 23; item3: 46; item4: 52  
- Capacity: 50 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 10, item2 21, item3 31, item4 34 /
    v(i)    value of item i
        / item1 24, item2 23, item3 46, item4 52 /;

Scalar capacity / 50 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=76.0

---

## Problem prob_132 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 12, 'value': 16}
    - laptop: {'weight': 14, 'value': 21}
    - camera: {'weight': 22, 'value': 30}
    - phone: {'weight': 36, 'value': 40}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 12; laptop: 14; camera: 22; phone: 36
- Values: book: 16; laptop: 21; camera: 30; phone: 40  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 12, laptop 14, camera 22, phone 36 /
    v(i)    value of item i
        / book 16, laptop 21, camera 30, phone 40 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=91.0

---

## Problem prob_133 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 70 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 7, 'value': 13}
    - item2: {'weight': 26, 'value': 27}
    - item3: {'weight': 38, 'value': 54}
    - item4: {'weight': 34, 'value': 39}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 7; item2: 26; item3: 38; item4: 34
- Values: item1: 13; item2: 27; item3: 54; item4: 39  
- Capacity: 70 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 7, item2 26, item3 38, item4 34 /
    v(i)    value of item i
        / item1 13, item2 27, item3 54, item4 39 /;

Scalar capacity / 70 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=81.0

---

## Problem prob_134 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 70 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 12, 'value': 20}
    - item2: {'weight': 25, 'value': 42}
    - item3: {'weight': 33, 'value': 37}
    - item4: {'weight': 31, 'value': 66}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 12; item2: 25; item3: 33; item4: 31
- Values: item1: 20; item2: 42; item3: 37; item4: 66  
- Capacity: 70 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 12, item2 25, item3 33, item4 31 /
    v(i)    value of item i
        / item1 20, item2 42, item3 37, item4 66 /;

Scalar capacity / 70 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=128.0

---

## Problem prob_135 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 9, 'value': 24}
    - laptop: {'weight': 22, 'value': 37}
    - camera: {'weight': 30, 'value': 47}
    - phone: {'weight': 39, 'value': 38}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 9; laptop: 22; camera: 30; phone: 39
- Values: book: 24; laptop: 37; camera: 47; phone: 38  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 9, laptop 22, camera 30, phone 39 /
    v(i)    value of item i
        / book 24, laptop 37, camera 47, phone 38 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=84.0

---

## Problem prob_136 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 9, 'value': 15}
    - laptop: {'weight': 25, 'value': 38}
    - camera: {'weight': 35, 'value': 31}
    - phone: {'weight': 30, 'value': 41}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 9; laptop: 25; camera: 35; phone: 30
- Values: book: 15; laptop: 38; camera: 31; phone: 41  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 9, laptop 25, camera 35, phone 30 /
    v(i)    value of item i
        / book 15, laptop 38, camera 31, phone 41 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=94.0

---

## Problem prob_137 — Knapsack

**Description:** Select items from book, laptop, camera and phone for a knapsack with capacity 60 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - book: {'weight': 9, 'value': 13}
    - laptop: {'weight': 15, 'value': 41}
    - camera: {'weight': 33, 'value': 31}
    - phone: {'weight': 34, 'value': 53}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: book, laptop, camera, phone (available items for selection)

PARAMETERS DEFINITION:
- Weights: book: 9; laptop: 15; camera: 33; phone: 34
- Values: book: 13; laptop: 41; camera: 31; phone: 53  
- Capacity: 60 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / book, laptop, camera, phone /;

Parameters
    w(i)    weight of item i
        / book 9, laptop 15, camera 33, phone 34 /
    v(i)    value of item i
        / book 13, laptop 41, camera 31, phone 53 /;

Scalar capacity / 60 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=107.0

---

## Problem prob_138 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 50 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 10, 'value': 21}
    - item2: {'weight': 18, 'value': 38}
    - item3: {'weight': 26, 'value': 28}
    - item4: {'weight': 43, 'value': 66}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 10; item2: 18; item3: 26; item4: 43
- Values: item1: 21; item2: 38; item3: 28; item4: 66  
- Capacity: 50 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 10, item2 18, item3 26, item4 43 /
    v(i)    value of item i
        / item1 21, item2 38, item3 28, item4 66 /;

Scalar capacity / 50 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=66.0

---

## Problem prob_139 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 70 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 12, 'value': 13}
    - item2: {'weight': 21, 'value': 41}
    - item3: {'weight': 39, 'value': 29}
    - item4: {'weight': 49, 'value': 30}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 12; item2: 21; item3: 39; item4: 49
- Values: item1: 13; item2: 41; item3: 29; item4: 30  
- Capacity: 70 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 12, item2 21, item3 39, item4 49 /
    v(i)    value of item i
        / item1 13, item2 41, item3 29, item4 30 /;

Scalar capacity / 70 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=71.0

---

## Problem prob_140 — Knapsack

**Description:** Select items from item1, item2, item3 and item4 for a knapsack with capacity 80 to maximize total value without exceeding the weight limit.

**Supplementary Tables:**
- items:
    - item1: {'weight': 12, 'value': 23}
    - item2: {'weight': 18, 'value': 27}
    - item3: {'weight': 39, 'value': 49}
    - item4: {'weight': 40, 'value': 42}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Knapsack Selection

SETS IDENTIFICATION:
- Items: item1, item2, item3, item4 (available items for selection)

PARAMETERS DEFINITION:
- Weights: item1: 12; item2: 18; item3: 39; item4: 40
- Values: item1: 23; item2: 27; item3: 49; item4: 42  
- Capacity: 80 (maximum weight limit)

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
- Binary selection decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   items   / item1, item2, item3, item4 /;

Parameters
    w(i)    weight of item i
        / item1 12, item2 18, item3 39, item4 40 /
    v(i)    value of item i
        / item1 23, item2 27, item3 49, item4 42 /;

Scalar capacity / 80 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=99.0

---

## Problem prob_141 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 1090
    - f2: 1233
    - f3: 1387

- capacities:
    - f1: 324
    - f2: 447
    - f3: 861

- demands:
    - city_1: 248
    - city_2: 321
    - city_3: 385

- transport_costs:
    - f1: {'city_1': 19, 'city_2': 12, 'city_3': 11}
    - f2: {'city_1': 20, 'city_2': 20, 'city_3': 10}
    - f3: {'city_1': 13, 'city_2': 12, 'city_3': 18}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 1090; f2: 1233; f3: 1387 (cost to open each facility)
- Capacities: f1: 324; f2: 447; f3: 861 (maximum output per facility)
- Customer demands: city_1: 248; city_2: 321; city_3: 385
- Transportation costs: f1 -> city_1: 19, city_2: 12, city_3: 11; f2 -> city_1: 20, city_2: 20, city_3: 10; f3 -> city_1: 13, city_2: 12, city_3: 18

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 1090, f2 1233, f3 1387 /
    cap(i)  capacity of facility i
        / f1 324, f2 447, f3 861 /
    d(j)    demand of customer j
        / city_1 248, city_2 321, city_3 385 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.city_1 19, f1.city_2 12, f1.city_3 11, f2.city_1 20, f2.city_2 20, f2.city_3 10, f3.city_1 13, f3.city_2 12, f3.city_3 18 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1750.0

---

## Problem prob_142 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 969
    - plant_B: 852
    - plant_C: 1173

- capacities:
    - plant_A: 355
    - plant_B: 391
    - plant_C: 933

- demands:
    - c1: 194
    - c2: 258
    - c3: 241
    - c4: 439

- transport_costs:
    - plant_A: {'c1': 19, 'c2': 9, 'c3': 16, 'c4': 9}
    - plant_B: {'c1': 21, 'c2': 13, 'c3': 18, 'c4': 16}
    - plant_C: {'c1': 11, 'c2': 17, 'c3': 9, 'c4': 19}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 969; plant_B: 852; plant_C: 1173 (cost to open each facility)
- Capacities: plant_A: 355; plant_B: 391; plant_C: 933 (maximum output per facility)
- Customer demands: c1: 194; c2: 258; c3: 241; c4: 439
- Transportation costs: plant_A -> c1: 19, c2: 9, c3: 16, c4: 9; plant_B -> c1: 21, c2: 13, c3: 18, c4: 16; plant_C -> c1: 11, c2: 17, c3: 9, c4: 19

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 969, plant_B 852, plant_C 1173 /
    cap(i)  capacity of facility i
        / plant_A 355, plant_B 391, plant_C 933 /
    d(j)    demand of customer j
        / c1 194, c2 258, c3 241, c4 439 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.c1 19, plant_A.c2 9, plant_A.c3 16, plant_A.c4 9, plant_B.c1 21, plant_B.c2 13, plant_B.c3 18, plant_B.c4 16, plant_C.c1 11, plant_C.c2 17, plant_C.c3 9, plant_C.c4 19 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1900.0

---

## Problem prob_143 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 1022
    - hub_2: 1024
    - hub_3: 1096

- capacities:
    - hub_1: 577
    - hub_2: 781
    - hub_3: 516

- demands:
    - city_1: 213
    - city_2: 249
    - city_3: 273

- transport_costs:
    - hub_1: {'city_1': 19, 'city_2': 15, 'city_3': 16}
    - hub_2: {'city_1': 21, 'city_2': 11, 'city_3': 10}
    - hub_3: {'city_1': 17, 'city_2': 19, 'city_3': 16}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 1022; hub_2: 1024; hub_3: 1096 (cost to open each facility)
- Capacities: hub_1: 577; hub_2: 781; hub_3: 516 (maximum output per facility)
- Customer demands: city_1: 213; city_2: 249; city_3: 273
- Transportation costs: hub_1 -> city_1: 19, city_2: 15, city_3: 16; hub_2 -> city_1: 21, city_2: 11, city_3: 10; hub_3 -> city_1: 17, city_2: 19, city_3: 16

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 1022, hub_2 1024, hub_3 1096 /
    cap(i)  capacity of facility i
        / hub_1 577, hub_2 781, hub_3 516 /
    d(j)    demand of customer j
        / city_1 213, city_2 249, city_3 273 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.city_1 19, hub_1.city_2 15, hub_1.city_3 16, hub_2.city_1 21, hub_2.city_2 11, hub_2.city_3 10, hub_3.city_1 17, hub_3.city_2 19, hub_3.city_3 16 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1900.0

---

## Problem prob_144 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 1016
    - f2: 993
    - f3: 1520

- capacities:
    - f1: 359
    - f2: 448
    - f3: 536

- demands:
    - c1: 178
    - c2: 309
    - c3: 312
    - c4: 296

- transport_costs:
    - f1: {'c1': 19, 'c2': 14, 'c3': 15, 'c4': 13}
    - f2: {'c1': 9, 'c2': 11, 'c3': 15, 'c4': 17}
    - f3: {'c1': 17, 'c2': 14, 'c3': 16, 'c4': 14}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 1016; f2: 993; f3: 1520 (cost to open each facility)
- Capacities: f1: 359; f2: 448; f3: 536 (maximum output per facility)
- Customer demands: c1: 178; c2: 309; c3: 312; c4: 296
- Transportation costs: f1 -> c1: 19, c2: 14, c3: 15, c4: 13; f2 -> c1: 9, c2: 11, c3: 15, c4: 17; f3 -> c1: 17, c2: 14, c3: 16, c4: 14

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 1016, f2 993, f3 1520 /
    cap(i)  capacity of facility i
        / f1 359, f2 448, f3 536 /
    d(j)    demand of customer j
        / c1 178, c2 309, c3 312, c4 296 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.c1 19, f1.c2 14, f1.c3 15, f1.c4 13, f2.c1 9, f2.c2 11, f2.c3 15, f2.c4 17, f3.c1 17, f3.c2 14, f3.c3 16, f3.c4 14 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2400.0

---

## Problem prob_145 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 1038
    - plant_B: 1096
    - plant_C: 1131

- capacities:
    - plant_A: 517
    - plant_B: 629
    - plant_C: 758

- demands:
    - city_1: 222
    - city_2: 243
    - city_3: 336

- transport_costs:
    - plant_A: {'city_1': 18, 'city_2': 14, 'city_3': 17}
    - plant_B: {'city_1': 15, 'city_2': 18, 'city_3': 17}
    - plant_C: {'city_1': 16, 'city_2': 19, 'city_3': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 1038; plant_B: 1096; plant_C: 1131 (cost to open each facility)
- Capacities: plant_A: 517; plant_B: 629; plant_C: 758 (maximum output per facility)
- Customer demands: city_1: 222; city_2: 243; city_3: 336
- Transportation costs: plant_A -> city_1: 18, city_2: 14, city_3: 17; plant_B -> city_1: 15, city_2: 18, city_3: 17; plant_C -> city_1: 16, city_2: 19, city_3: 9

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 1038, plant_B 1096, plant_C 1131 /
    cap(i)  capacity of facility i
        / plant_A 517, plant_B 629, plant_C 758 /
    d(j)    demand of customer j
        / city_1 222, city_2 243, city_3 336 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.city_1 18, plant_A.city_2 14, plant_A.city_3 17, plant_B.city_1 15, plant_B.city_2 18, plant_B.city_3 17, plant_C.city_1 16, plant_C.city_2 19, plant_C.city_3 9 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1900.0

---

## Problem prob_146 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 763
    - hub_2: 1028
    - hub_3: 1059

- capacities:
    - hub_1: 475
    - hub_2: 485
    - hub_3: 819

- demands:
    - city_1: 140
    - city_2: 192
    - city_3: 380

- transport_costs:
    - hub_1: {'city_1': 13, 'city_2': 15, 'city_3': 12}
    - hub_2: {'city_1': 13, 'city_2': 9, 'city_3': 18}
    - hub_3: {'city_1': 16, 'city_2': 18, 'city_3': 19}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 763; hub_2: 1028; hub_3: 1059 (cost to open each facility)
- Capacities: hub_1: 475; hub_2: 485; hub_3: 819 (maximum output per facility)
- Customer demands: city_1: 140; city_2: 192; city_3: 380
- Transportation costs: hub_1 -> city_1: 13, city_2: 15, city_3: 12; hub_2 -> city_1: 13, city_2: 9, city_3: 18; hub_3 -> city_1: 16, city_2: 18, city_3: 19

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 763, hub_2 1028, hub_3 1059 /
    cap(i)  capacity of facility i
        / hub_1 475, hub_2 485, hub_3 819 /
    d(j)    demand of customer j
        / city_1 140, city_2 192, city_3 380 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.city_1 13, hub_1.city_2 15, hub_1.city_3 12, hub_2.city_1 13, hub_2.city_2 9, hub_2.city_3 18, hub_3.city_1 16, hub_3.city_2 18, hub_3.city_3 19 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1700.0

---

## Problem prob_147 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 891
    - hub_2: 1472
    - hub_3: 1478

- capacities:
    - hub_1: 653
    - hub_2: 562
    - hub_3: 974

- demands:
    - c1: 215
    - c2: 213
    - c3: 262
    - c4: 319

- transport_costs:
    - hub_1: {'c1': 19, 'c2': 16, 'c3': 12, 'c4': 20}
    - hub_2: {'c1': 17, 'c2': 16, 'c3': 19, 'c4': 18}
    - hub_3: {'c1': 19, 'c2': 21, 'c3': 18, 'c4': 17}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 891; hub_2: 1472; hub_3: 1478 (cost to open each facility)
- Capacities: hub_1: 653; hub_2: 562; hub_3: 974 (maximum output per facility)
- Customer demands: c1: 215; c2: 213; c3: 262; c4: 319
- Transportation costs: hub_1 -> c1: 19, c2: 16, c3: 12, c4: 20; hub_2 -> c1: 17, c2: 16, c3: 19, c4: 18; hub_3 -> c1: 19, c2: 21, c3: 18, c4: 17

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 891, hub_2 1472, hub_3 1478 /
    cap(i)  capacity of facility i
        / hub_1 653, hub_2 562, hub_3 974 /
    d(j)    demand of customer j
        / c1 215, c2 213, c3 262, c4 319 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.c1 19, hub_1.c2 16, hub_1.c3 12, hub_1.c4 20, hub_2.c1 17, hub_2.c2 16, hub_2.c3 19, hub_2.c4 18, hub_3.c1 19, hub_3.c2 21, hub_3.c3 18, hub_3.c4 17 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=3100.0

---

## Problem prob_148 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 1278
    - f2: 1429
    - f3: 1393

- capacities:
    - f1: 667
    - f2: 816
    - f3: 961

- demands:
    - c1: 259
    - c2: 198
    - c3: 386
    - c4: 248

- transport_costs:
    - f1: {'c1': 18, 'c2': 12, 'c3': 13, 'c4': 16}
    - f2: {'c1': 11, 'c2': 18, 'c3': 11, 'c4': 16}
    - f3: {'c1': 12, 'c2': 13, 'c3': 20, 'c4': 18}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 1278; f2: 1429; f3: 1393 (cost to open each facility)
- Capacities: f1: 667; f2: 816; f3: 961 (maximum output per facility)
- Customer demands: c1: 259; c2: 198; c3: 386; c4: 248
- Transportation costs: f1 -> c1: 18, c2: 12, c3: 13, c4: 16; f2 -> c1: 11, c2: 18, c3: 11, c4: 16; f3 -> c1: 12, c2: 13, c3: 20, c4: 18

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 1278, f2 1429, f3 1393 /
    cap(i)  capacity of facility i
        / f1 667, f2 816, f3 961 /
    d(j)    demand of customer j
        / c1 259, c2 198, c3 386, c4 248 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.c1 18, f1.c2 12, f1.c3 13, f1.c4 16, f2.c1 11, f2.c2 18, f2.c3 11, f2.c4 16, f3.c1 12, f3.c2 13, f3.c3 20, f3.c4 18 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2500.0

---

## Problem prob_149 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 1043
    - f2: 1091
    - f3: 1593

- capacities:
    - f1: 495
    - f2: 445
    - f3: 726

- demands:
    - region_A: 237
    - region_B: 308
    - region_C: 284

- transport_costs:
    - f1: {'region_A': 10, 'region_B': 17, 'region_C': 14}
    - f2: {'region_A': 13, 'region_B': 16, 'region_C': 19}
    - f3: {'region_A': 16, 'region_B': 12, 'region_C': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 1043; f2: 1091; f3: 1593 (cost to open each facility)
- Capacities: f1: 495; f2: 445; f3: 726 (maximum output per facility)
- Customer demands: region_A: 237; region_B: 308; region_C: 284
- Transportation costs: f1 -> region_A: 10, region_B: 17, region_C: 14; f2 -> region_A: 13, region_B: 16, region_C: 19; f3 -> region_A: 16, region_B: 12, region_C: 11

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 1043, f2 1091, f3 1593 /
    cap(i)  capacity of facility i
        / f1 495, f2 445, f3 726 /
    d(j)    demand of customer j
        / region_A 237, region_B 308, region_C 284 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.region_A 10, f1.region_B 17, f1.region_C 14, f2.region_A 13, f2.region_B 16, f2.region_C 19, f3.region_A 16, f3.region_B 12, f3.region_C 11 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1650.0

---

## Problem prob_150 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 826
    - hub_2: 870
    - hub_3: 1108

- capacities:
    - hub_1: 692
    - hub_2: 797
    - hub_3: 543

- demands:
    - city_1: 222
    - city_2: 206
    - city_3: 269

- transport_costs:
    - hub_1: {'city_1': 9, 'city_2': 12, 'city_3': 17}
    - hub_2: {'city_1': 9, 'city_2': 19, 'city_3': 18}
    - hub_3: {'city_1': 14, 'city_2': 10, 'city_3': 14}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 826; hub_2: 870; hub_3: 1108 (cost to open each facility)
- Capacities: hub_1: 692; hub_2: 797; hub_3: 543 (maximum output per facility)
- Customer demands: city_1: 222; city_2: 206; city_3: 269
- Transportation costs: hub_1 -> city_1: 9, city_2: 12, city_3: 17; hub_2 -> city_1: 9, city_2: 19, city_3: 18; hub_3 -> city_1: 14, city_2: 10, city_3: 14

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 826, hub_2 870, hub_3 1108 /
    cap(i)  capacity of facility i
        / hub_1 692, hub_2 797, hub_3 543 /
    d(j)    demand of customer j
        / city_1 222, city_2 206, city_3 269 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.city_1 9, hub_1.city_2 12, hub_1.city_3 17, hub_2.city_1 9, hub_2.city_2 19, hub_2.city_3 18, hub_3.city_1 14, hub_3.city_2 10, hub_3.city_3 14 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1650.0

---

## Problem prob_151 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 1151
    - plant_B: 1301
    - plant_C: 1134

- capacities:
    - plant_A: 572
    - plant_B: 507
    - plant_C: 791

- demands:
    - region_A: 214
    - region_B: 270
    - region_C: 347

- transport_costs:
    - plant_A: {'region_A': 16, 'region_B': 16, 'region_C': 12}
    - plant_B: {'region_A': 19, 'region_B': 16, 'region_C': 13}
    - plant_C: {'region_A': 15, 'region_B': 16, 'region_C': 18}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 1151; plant_B: 1301; plant_C: 1134 (cost to open each facility)
- Capacities: plant_A: 572; plant_B: 507; plant_C: 791 (maximum output per facility)
- Customer demands: region_A: 214; region_B: 270; region_C: 347
- Transportation costs: plant_A -> region_A: 16, region_B: 16, region_C: 12; plant_B -> region_A: 19, region_B: 16, region_C: 13; plant_C -> region_A: 15, region_B: 16, region_C: 18

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 1151, plant_B 1301, plant_C 1134 /
    cap(i)  capacity of facility i
        / plant_A 572, plant_B 507, plant_C 791 /
    d(j)    demand of customer j
        / region_A 214, region_B 270, region_C 347 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.region_A 16, plant_A.region_B 16, plant_A.region_C 12, plant_B.region_A 19, plant_B.region_B 16, plant_B.region_C 13, plant_C.region_A 15, plant_C.region_B 16, plant_C.region_C 18 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2150.0

---

## Problem prob_152 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 1152
    - plant_B: 918
    - plant_C: 1261

- capacities:
    - plant_A: 681
    - plant_B: 788
    - plant_C: 644

- demands:
    - c1: 189
    - c2: 284
    - c3: 377
    - c4: 341

- transport_costs:
    - plant_A: {'c1': 17, 'c2': 10, 'c3': 15, 'c4': 16}
    - plant_B: {'c1': 12, 'c2': 16, 'c3': 11, 'c4': 16}
    - plant_C: {'c1': 16, 'c2': 20, 'c3': 17, 'c4': 19}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 1152; plant_B: 918; plant_C: 1261 (cost to open each facility)
- Capacities: plant_A: 681; plant_B: 788; plant_C: 644 (maximum output per facility)
- Customer demands: c1: 189; c2: 284; c3: 377; c4: 341
- Transportation costs: plant_A -> c1: 17, c2: 10, c3: 15, c4: 16; plant_B -> c1: 12, c2: 16, c3: 11, c4: 16; plant_C -> c1: 16, c2: 20, c3: 17, c4: 19

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 1152, plant_B 918, plant_C 1261 /
    cap(i)  capacity of facility i
        / plant_A 681, plant_B 788, plant_C 644 /
    d(j)    demand of customer j
        / c1 189, c2 284, c3 377, c4 341 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.c1 17, plant_A.c2 10, plant_A.c3 15, plant_A.c4 16, plant_B.c1 12, plant_B.c2 16, plant_B.c3 11, plant_B.c4 16, plant_C.c1 16, plant_C.c2 20, plant_C.c3 17, plant_C.c4 19 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2450.0

---

## Problem prob_153 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 938
    - hub_2: 892
    - hub_3: 1468

- capacities:
    - hub_1: 339
    - hub_2: 659
    - hub_3: 713

- demands:
    - region_A: 143
    - region_B: 237
    - region_C: 316

- transport_costs:
    - hub_1: {'region_A': 19, 'region_B': 16, 'region_C': 13}
    - hub_2: {'region_A': 11, 'region_B': 9, 'region_C': 10}
    - hub_3: {'region_A': 12, 'region_B': 15, 'region_C': 9}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 938; hub_2: 892; hub_3: 1468 (cost to open each facility)
- Capacities: hub_1: 339; hub_2: 659; hub_3: 713 (maximum output per facility)
- Customer demands: region_A: 143; region_B: 237; region_C: 316
- Transportation costs: hub_1 -> region_A: 19, region_B: 16, region_C: 13; hub_2 -> region_A: 11, region_B: 9, region_C: 10; hub_3 -> region_A: 12, region_B: 15, region_C: 9

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 938, hub_2 892, hub_3 1468 /
    cap(i)  capacity of facility i
        / hub_1 339, hub_2 659, hub_3 713 /
    d(j)    demand of customer j
        / region_A 143, region_B 237, region_C 316 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.region_A 19, hub_1.region_B 16, hub_1.region_C 13, hub_2.region_A 11, hub_2.region_B 9, hub_2.region_C 10, hub_3.region_A 12, hub_3.region_B 15, hub_3.region_C 9 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1450.0

---

## Problem prob_154 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 1257
    - hub_2: 1331
    - hub_3: 1271

- capacities:
    - hub_1: 547
    - hub_2: 523
    - hub_3: 877

- demands:
    - c1: 238
    - c2: 176
    - c3: 310
    - c4: 299

- transport_costs:
    - hub_1: {'c1': 14, 'c2': 9, 'c3': 20, 'c4': 17}
    - hub_2: {'c1': 9, 'c2': 19, 'c3': 12, 'c4': 17}
    - hub_3: {'c1': 16, 'c2': 11, 'c3': 14, 'c4': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 1257; hub_2: 1331; hub_3: 1271 (cost to open each facility)
- Capacities: hub_1: 547; hub_2: 523; hub_3: 877 (maximum output per facility)
- Customer demands: c1: 238; c2: 176; c3: 310; c4: 299
- Transportation costs: hub_1 -> c1: 14, c2: 9, c3: 20, c4: 17; hub_2 -> c1: 9, c2: 19, c3: 12, c4: 17; hub_3 -> c1: 16, c2: 11, c3: 14, c4: 11

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 1257, hub_2 1331, hub_3 1271 /
    cap(i)  capacity of facility i
        / hub_1 547, hub_2 523, hub_3 877 /
    d(j)    demand of customer j
        / c1 238, c2 176, c3 310, c4 299 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.c1 14, hub_1.c2 9, hub_1.c3 20, hub_1.c4 17, hub_2.c1 9, hub_2.c2 19, hub_2.c3 12, hub_2.c4 17, hub_3.c1 16, hub_3.c2 11, hub_3.c3 14, hub_3.c4 11 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2050.0

---

## Problem prob_155 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 718
    - hub_2: 969
    - hub_3: 1568

- capacities:
    - hub_1: 567
    - hub_2: 543
    - hub_3: 647

- demands:
    - region_A: 170
    - region_B: 219
    - region_C: 314

- transport_costs:
    - hub_1: {'region_A': 10, 'region_B': 21, 'region_C': 16}
    - hub_2: {'region_A': 14, 'region_B': 20, 'region_C': 18}
    - hub_3: {'region_A': 17, 'region_B': 15, 'region_C': 20}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 718; hub_2: 969; hub_3: 1568 (cost to open each facility)
- Capacities: hub_1: 567; hub_2: 543; hub_3: 647 (maximum output per facility)
- Customer demands: region_A: 170; region_B: 219; region_C: 314
- Transportation costs: hub_1 -> region_A: 10, region_B: 21, region_C: 16; hub_2 -> region_A: 14, region_B: 20, region_C: 18; hub_3 -> region_A: 17, region_B: 15, region_C: 20

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 718, hub_2 969, hub_3 1568 /
    cap(i)  capacity of facility i
        / hub_1 567, hub_2 543, hub_3 647 /
    d(j)    demand of customer j
        / region_A 170, region_B 219, region_C 314 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.region_A 10, hub_1.region_B 21, hub_1.region_C 16, hub_2.region_A 14, hub_2.region_B 20, hub_2.region_C 18, hub_3.region_A 17, hub_3.region_B 15, hub_3.region_C 20 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2050.0

---

## Problem prob_156 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 1240
    - plant_B: 1209
    - plant_C: 1022

- capacities:
    - plant_A: 302
    - plant_B: 728
    - plant_C: 739

- demands:
    - region_A: 205
    - region_B: 268
    - region_C: 272

- transport_costs:
    - plant_A: {'region_A': 17, 'region_B': 15, 'region_C': 15}
    - plant_B: {'region_A': 12, 'region_B': 10, 'region_C': 14}
    - plant_C: {'region_A': 13, 'region_B': 17, 'region_C': 14}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 1240; plant_B: 1209; plant_C: 1022 (cost to open each facility)
- Capacities: plant_A: 302; plant_B: 728; plant_C: 739 (maximum output per facility)
- Customer demands: region_A: 205; region_B: 268; region_C: 272
- Transportation costs: plant_A -> region_A: 17, region_B: 15, region_C: 15; plant_B -> region_A: 12, region_B: 10, region_C: 14; plant_C -> region_A: 13, region_B: 17, region_C: 14

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 1240, plant_B 1209, plant_C 1022 /
    cap(i)  capacity of facility i
        / plant_A 302, plant_B 728, plant_C 739 /
    d(j)    demand of customer j
        / region_A 205, region_B 268, region_C 272 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.region_A 17, plant_A.region_B 15, plant_A.region_C 15, plant_B.region_A 12, plant_B.region_B 10, plant_B.region_C 14, plant_C.region_A 13, plant_C.region_B 17, plant_C.region_C 14 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1800.0

---

## Problem prob_157 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 839
    - f2: 1410
    - f3: 1496

- capacities:
    - f1: 630
    - f2: 804
    - f3: 659

- demands:
    - city_1: 169
    - city_2: 280
    - city_3: 306

- transport_costs:
    - f1: {'city_1': 13, 'city_2': 14, 'city_3': 15}
    - f2: {'city_1': 9, 'city_2': 14, 'city_3': 17}
    - f3: {'city_1': 9, 'city_2': 17, 'city_3': 18}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 839; f2: 1410; f3: 1496 (cost to open each facility)
- Capacities: f1: 630; f2: 804; f3: 659 (maximum output per facility)
- Customer demands: city_1: 169; city_2: 280; city_3: 306
- Transportation costs: f1 -> city_1: 13, city_2: 14, city_3: 15; f2 -> city_1: 9, city_2: 14, city_3: 17; f3 -> city_1: 9, city_2: 17, city_3: 18

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 839, f2 1410, f3 1496 /
    cap(i)  capacity of facility i
        / f1 630, f2 804, f3 659 /
    d(j)    demand of customer j
        / city_1 169, city_2 280, city_3 306 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.city_1 13, f1.city_2 14, f1.city_3 15, f2.city_1 9, f2.city_2 14, f2.city_3 17, f3.city_1 9, f3.city_2 17, f3.city_3 18 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1900.0

---

## Problem prob_158 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 914
    - f2: 1102
    - f3: 1138

- capacities:
    - f1: 604
    - f2: 518
    - f3: 940

- demands:
    - city_1: 149
    - city_2: 202
    - city_3: 319

- transport_costs:
    - f1: {'city_1': 10, 'city_2': 12, 'city_3': 18}
    - f2: {'city_1': 15, 'city_2': 18, 'city_3': 9}
    - f3: {'city_1': 10, 'city_2': 10, 'city_3': 16}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 914; f2: 1102; f3: 1138 (cost to open each facility)
- Capacities: f1: 604; f2: 518; f3: 940 (maximum output per facility)
- Customer demands: city_1: 149; city_2: 202; city_3: 319
- Transportation costs: f1 -> city_1: 10, city_2: 12, city_3: 18; f2 -> city_1: 15, city_2: 18, city_3: 9; f3 -> city_1: 10, city_2: 10, city_3: 16

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 914, f2 1102, f3 1138 /
    cap(i)  capacity of facility i
        / f1 604, f2 518, f3 940 /
    d(j)    demand of customer j
        / city_1 149, city_2 202, city_3 319 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.city_1 10, f1.city_2 12, f1.city_3 18, f2.city_1 15, f2.city_2 18, f2.city_3 9, f3.city_1 10, f3.city_2 10, f3.city_3 16 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1450.0

---

## Problem prob_159 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 806
    - plant_B: 875
    - plant_C: 1817

- capacities:
    - plant_A: 409
    - plant_B: 513
    - plant_C: 458

- demands:
    - c1: 259
    - c2: 188
    - c3: 256
    - c4: 386

- transport_costs:
    - plant_A: {'c1': 11, 'c2': 15, 'c3': 11, 'c4': 15}
    - plant_B: {'c1': 11, 'c2': 18, 'c3': 15, 'c4': 17}
    - plant_C: {'c1': 18, 'c2': 19, 'c3': 14, 'c4': 16}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 806; plant_B: 875; plant_C: 1817 (cost to open each facility)
- Capacities: plant_A: 409; plant_B: 513; plant_C: 458 (maximum output per facility)
- Customer demands: c1: 259; c2: 188; c3: 256; c4: 386
- Transportation costs: plant_A -> c1: 11, c2: 15, c3: 11, c4: 15; plant_B -> c1: 11, c2: 18, c3: 15, c4: 17; plant_C -> c1: 18, c2: 19, c3: 14, c4: 16

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 806, plant_B 875, plant_C 1817 /
    cap(i)  capacity of facility i
        / plant_A 409, plant_B 513, plant_C 458 /
    d(j)    demand of customer j
        / c1 259, c2 188, c3 256, c4 386 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.c1 11, plant_A.c2 15, plant_A.c3 11, plant_A.c4 15, plant_B.c1 11, plant_B.c2 18, plant_B.c3 15, plant_B.c4 17, plant_C.c1 18, plant_C.c2 19, plant_C.c3 14, plant_C.c4 16 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2650.0

---

## Problem prob_160 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 1190
    - f2: 1049
    - f3: 1443

- capacities:
    - f1: 378
    - f2: 815
    - f3: 432

- demands:
    - c1: 165
    - c2: 190
    - c3: 268
    - c4: 259

- transport_costs:
    - f1: {'c1': 16, 'c2': 20, 'c3': 11, 'c4': 18}
    - f2: {'c1': 20, 'c2': 20, 'c3': 11, 'c4': 17}
    - f3: {'c1': 18, 'c2': 16, 'c3': 12, 'c4': 19}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 1190; f2: 1049; f3: 1443 (cost to open each facility)
- Capacities: f1: 378; f2: 815; f3: 432 (maximum output per facility)
- Customer demands: c1: 165; c2: 190; c3: 268; c4: 259
- Transportation costs: f1 -> c1: 16, c2: 20, c3: 11, c4: 18; f2 -> c1: 20, c2: 20, c3: 11, c4: 17; f3 -> c1: 18, c2: 16, c3: 12, c4: 19

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 1190, f2 1049, f3 1443 /
    cap(i)  capacity of facility i
        / f1 378, f2 815, f3 432 /
    d(j)    demand of customer j
        / c1 165, c2 190, c3 268, c4 259 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.c1 16, f1.c2 20, f1.c3 11, f1.c4 18, f2.c1 20, f2.c2 20, f2.c3 11, f2.c4 17, f3.c1 18, f3.c2 16, f3.c3 12, f3.c4 19 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=3000.0

---

## Problem prob_161 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 1297
    - hub_2: 1512
    - hub_3: 1587

- capacities:
    - hub_1: 381
    - hub_2: 436
    - hub_3: 846

- demands:
    - city_1: 237
    - city_2: 297
    - city_3: 233

- transport_costs:
    - hub_1: {'city_1': 13, 'city_2': 10, 'city_3': 13}
    - hub_2: {'city_1': 14, 'city_2': 16, 'city_3': 16}
    - hub_3: {'city_1': 10, 'city_2': 9, 'city_3': 20}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 1297; hub_2: 1512; hub_3: 1587 (cost to open each facility)
- Capacities: hub_1: 381; hub_2: 436; hub_3: 846 (maximum output per facility)
- Customer demands: city_1: 237; city_2: 297; city_3: 233
- Transportation costs: hub_1 -> city_1: 13, city_2: 10, city_3: 13; hub_2 -> city_1: 14, city_2: 16, city_3: 16; hub_3 -> city_1: 10, city_2: 9, city_3: 20

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 1297, hub_2 1512, hub_3 1587 /
    cap(i)  capacity of facility i
        / hub_1 381, hub_2 436, hub_3 846 /
    d(j)    demand of customer j
        / city_1 237, city_2 297, city_3 233 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.city_1 13, hub_1.city_2 10, hub_1.city_3 13, hub_2.city_1 14, hub_2.city_2 16, hub_2.city_3 16, hub_3.city_1 10, hub_3.city_2 9, hub_3.city_3 20 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1600.0

---

## Problem prob_162 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 837
    - plant_B: 973
    - plant_C: 1810

- capacities:
    - plant_A: 561
    - plant_B: 634
    - plant_C: 428

- demands:
    - city_1: 194
    - city_2: 239
    - city_3: 386

- transport_costs:
    - plant_A: {'city_1': 20, 'city_2': 13, 'city_3': 17}
    - plant_B: {'city_1': 12, 'city_2': 12, 'city_3': 12}
    - plant_C: {'city_1': 9, 'city_2': 19, 'city_3': 19}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 837; plant_B: 973; plant_C: 1810 (cost to open each facility)
- Capacities: plant_A: 561; plant_B: 634; plant_C: 428 (maximum output per facility)
- Customer demands: city_1: 194; city_2: 239; city_3: 386
- Transportation costs: plant_A -> city_1: 20, city_2: 13, city_3: 17; plant_B -> city_1: 12, city_2: 12, city_3: 12; plant_C -> city_1: 9, city_2: 19, city_3: 19

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 837, plant_B 973, plant_C 1810 /
    cap(i)  capacity of facility i
        / plant_A 561, plant_B 634, plant_C 428 /
    d(j)    demand of customer j
        / city_1 194, city_2 239, city_3 386 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.city_1 20, plant_A.city_2 13, plant_A.city_3 17, plant_B.city_1 12, plant_B.city_2 12, plant_B.city_3 12, plant_C.city_1 9, plant_C.city_2 19, plant_C.city_3 19 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1650.0

---

## Problem prob_163 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 752
    - f2: 1515
    - f3: 1084

- capacities:
    - f1: 520
    - f2: 782
    - f3: 871

- demands:
    - region_A: 213
    - region_B: 293
    - region_C: 264

- transport_costs:
    - f1: {'region_A': 12, 'region_B': 9, 'region_C': 9}
    - f2: {'region_A': 20, 'region_B': 21, 'region_C': 15}
    - f3: {'region_A': 16, 'region_B': 13, 'region_C': 15}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 752; f2: 1515; f3: 1084 (cost to open each facility)
- Capacities: f1: 520; f2: 782; f3: 871 (maximum output per facility)
- Customer demands: region_A: 213; region_B: 293; region_C: 264
- Transportation costs: f1 -> region_A: 12, region_B: 9, region_C: 9; f2 -> region_A: 20, region_B: 21, region_C: 15; f3 -> region_A: 16, region_B: 13, region_C: 15

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 752, f2 1515, f3 1084 /
    cap(i)  capacity of facility i
        / f1 520, f2 782, f3 871 /
    d(j)    demand of customer j
        / region_A 213, region_B 293, region_C 264 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.region_A 12, f1.region_B 9, f1.region_C 9, f2.region_A 20, f2.region_B 21, f2.region_C 15, f3.region_A 16, f3.region_B 13, f3.region_C 15 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1700.0

---

## Problem prob_164 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 1163
    - plant_B: 1508
    - plant_C: 1591

- capacities:
    - plant_A: 677
    - plant_B: 649
    - plant_C: 891

- demands:
    - region_A: 255
    - region_B: 219
    - region_C: 326

- transport_costs:
    - plant_A: {'region_A': 14, 'region_B': 20, 'region_C': 10}
    - plant_B: {'region_A': 17, 'region_B': 14, 'region_C': 20}
    - plant_C: {'region_A': 15, 'region_B': 10, 'region_C': 13}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 1163; plant_B: 1508; plant_C: 1591 (cost to open each facility)
- Capacities: plant_A: 677; plant_B: 649; plant_C: 891 (maximum output per facility)
- Customer demands: region_A: 255; region_B: 219; region_C: 326
- Transportation costs: plant_A -> region_A: 14, region_B: 20, region_C: 10; plant_B -> region_A: 17, region_B: 14, region_C: 20; plant_C -> region_A: 15, region_B: 10, region_C: 13

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 1163, plant_B 1508, plant_C 1591 /
    cap(i)  capacity of facility i
        / plant_A 677, plant_B 649, plant_C 891 /
    d(j)    demand of customer j
        / region_A 255, region_B 219, region_C 326 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.region_A 14, plant_A.region_B 20, plant_A.region_C 10, plant_B.region_A 17, plant_B.region_B 14, plant_B.region_C 20, plant_C.region_A 15, plant_C.region_B 10, plant_C.region_C 13 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1700.0

---

## Problem prob_165 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 1245
    - plant_B: 1147
    - plant_C: 1356

- capacities:
    - plant_A: 645
    - plant_B: 592
    - plant_C: 849

- demands:
    - city_1: 152
    - city_2: 181
    - city_3: 278

- transport_costs:
    - plant_A: {'city_1': 16, 'city_2': 18, 'city_3': 14}
    - plant_B: {'city_1': 12, 'city_2': 20, 'city_3': 12}
    - plant_C: {'city_1': 17, 'city_2': 17, 'city_3': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 1245; plant_B: 1147; plant_C: 1356 (cost to open each facility)
- Capacities: plant_A: 645; plant_B: 592; plant_C: 849 (maximum output per facility)
- Customer demands: city_1: 152; city_2: 181; city_3: 278
- Transportation costs: plant_A -> city_1: 16, city_2: 18, city_3: 14; plant_B -> city_1: 12, city_2: 20, city_3: 12; plant_C -> city_1: 17, city_2: 17, city_3: 11

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 1245, plant_B 1147, plant_C 1356 /
    cap(i)  capacity of facility i
        / plant_A 645, plant_B 592, plant_C 849 /
    d(j)    demand of customer j
        / city_1 152, city_2 181, city_3 278 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.city_1 16, plant_A.city_2 18, plant_A.city_3 14, plant_B.city_1 12, plant_B.city_2 20, plant_B.city_3 12, plant_C.city_1 17, plant_C.city_2 17, plant_C.city_3 11 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2000.0

---

## Problem prob_166 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 964
    - f2: 1202
    - f3: 1728

- capacities:
    - f1: 423
    - f2: 668
    - f3: 683

- demands:
    - city_1: 245
    - city_2: 218
    - city_3: 253

- transport_costs:
    - f1: {'city_1': 17, 'city_2': 12, 'city_3': 14}
    - f2: {'city_1': 14, 'city_2': 14, 'city_3': 16}
    - f3: {'city_1': 16, 'city_2': 12, 'city_3': 18}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 964; f2: 1202; f3: 1728 (cost to open each facility)
- Capacities: f1: 423; f2: 668; f3: 683 (maximum output per facility)
- Customer demands: city_1: 245; city_2: 218; city_3: 253
- Transportation costs: f1 -> city_1: 17, city_2: 12, city_3: 14; f2 -> city_1: 14, city_2: 14, city_3: 16; f3 -> city_1: 16, city_2: 12, city_3: 18

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 964, f2 1202, f3 1728 /
    cap(i)  capacity of facility i
        / f1 423, f2 668, f3 683 /
    d(j)    demand of customer j
        / city_1 245, city_2 218, city_3 253 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.city_1 17, f1.city_2 12, f1.city_3 14, f2.city_1 14, f2.city_2 14, f2.city_3 16, f3.city_1 16, f3.city_2 12, f3.city_3 18 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2000.0

---

## Problem prob_167 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 937
    - plant_B: 1484
    - plant_C: 1784

- capacities:
    - plant_A: 667
    - plant_B: 519
    - plant_C: 973

- demands:
    - c1: 144
    - c2: 227
    - c3: 299
    - c4: 308

- transport_costs:
    - plant_A: {'c1': 11, 'c2': 18, 'c3': 20, 'c4': 11}
    - plant_B: {'c1': 18, 'c2': 10, 'c3': 9, 'c4': 16}
    - plant_C: {'c1': 16, 'c2': 19, 'c3': 17, 'c4': 17}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 937; plant_B: 1484; plant_C: 1784 (cost to open each facility)
- Capacities: plant_A: 667; plant_B: 519; plant_C: 973 (maximum output per facility)
- Customer demands: c1: 144; c2: 227; c3: 299; c4: 308
- Transportation costs: plant_A -> c1: 11, c2: 18, c3: 20, c4: 11; plant_B -> c1: 18, c2: 10, c3: 9, c4: 16; plant_C -> c1: 16, c2: 19, c3: 17, c4: 17

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 937, plant_B 1484, plant_C 1784 /
    cap(i)  capacity of facility i
        / plant_A 667, plant_B 519, plant_C 973 /
    d(j)    demand of customer j
        / c1 144, c2 227, c3 299, c4 308 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.c1 11, plant_A.c2 18, plant_A.c3 20, plant_A.c4 11, plant_B.c1 18, plant_B.c2 10, plant_B.c3 9, plant_B.c4 16, plant_C.c1 16, plant_C.c2 19, plant_C.c3 17, plant_C.c4 17 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2050.0

---

## Problem prob_168 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 1210
    - hub_2: 1433
    - hub_3: 1058

- capacities:
    - hub_1: 407
    - hub_2: 589
    - hub_3: 942

- demands:
    - city_1: 177
    - city_2: 233
    - city_3: 253

- transport_costs:
    - hub_1: {'city_1': 15, 'city_2': 20, 'city_3': 19}
    - hub_2: {'city_1': 15, 'city_2': 14, 'city_3': 14}
    - hub_3: {'city_1': 16, 'city_2': 16, 'city_3': 17}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 1210; hub_2: 1433; hub_3: 1058 (cost to open each facility)
- Capacities: hub_1: 407; hub_2: 589; hub_3: 942 (maximum output per facility)
- Customer demands: city_1: 177; city_2: 233; city_3: 253
- Transportation costs: hub_1 -> city_1: 15, city_2: 20, city_3: 19; hub_2 -> city_1: 15, city_2: 14, city_3: 14; hub_3 -> city_1: 16, city_2: 16, city_3: 17

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 1210, hub_2 1433, hub_3 1058 /
    cap(i)  capacity of facility i
        / hub_1 407, hub_2 589, hub_3 942 /
    d(j)    demand of customer j
        / city_1 177, city_2 233, city_3 253 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.city_1 15, hub_1.city_2 20, hub_1.city_3 19, hub_2.city_1 15, hub_2.city_2 14, hub_2.city_3 14, hub_3.city_1 16, hub_3.city_2 16, hub_3.city_3 17 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2150.0

---

## Problem prob_169 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 778
    - f2: 1223
    - f3: 1750

- capacities:
    - f1: 485
    - f2: 754
    - f3: 760

- demands:
    - region_A: 223
    - region_B: 250
    - region_C: 323

- transport_costs:
    - f1: {'region_A': 18, 'region_B': 18, 'region_C': 17}
    - f2: {'region_A': 10, 'region_B': 12, 'region_C': 15}
    - f3: {'region_A': 10, 'region_B': 14, 'region_C': 19}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 778; f2: 1223; f3: 1750 (cost to open each facility)
- Capacities: f1: 485; f2: 754; f3: 760 (maximum output per facility)
- Customer demands: region_A: 223; region_B: 250; region_C: 323
- Transportation costs: f1 -> region_A: 18, region_B: 18, region_C: 17; f2 -> region_A: 10, region_B: 12, region_C: 15; f3 -> region_A: 10, region_B: 14, region_C: 19

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 778, f2 1223, f3 1750 /
    cap(i)  capacity of facility i
        / f1 485, f2 754, f3 760 /
    d(j)    demand of customer j
        / region_A 223, region_B 250, region_C 323 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.region_A 18, f1.region_B 18, f1.region_C 17, f2.region_A 10, f2.region_B 12, f2.region_C 15, f3.region_A 10, f3.region_B 14, f3.region_C 19 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1850.0

---

## Problem prob_170 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 797
    - hub_2: 1332
    - hub_3: 1185

- capacities:
    - hub_1: 677
    - hub_2: 502
    - hub_3: 630

- demands:
    - c1: 166
    - c2: 263
    - c3: 228
    - c4: 278

- transport_costs:
    - hub_1: {'c1': 10, 'c2': 14, 'c3': 12, 'c4': 13}
    - hub_2: {'c1': 10, 'c2': 12, 'c3': 15, 'c4': 14}
    - hub_3: {'c1': 14, 'c2': 19, 'c3': 11, 'c4': 15}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 797; hub_2: 1332; hub_3: 1185 (cost to open each facility)
- Capacities: hub_1: 677; hub_2: 502; hub_3: 630 (maximum output per facility)
- Customer demands: c1: 166; c2: 263; c3: 228; c4: 278
- Transportation costs: hub_1 -> c1: 10, c2: 14, c3: 12, c4: 13; hub_2 -> c1: 10, c2: 12, c3: 15, c4: 14; hub_3 -> c1: 14, c2: 19, c3: 11, c4: 15

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 797, hub_2 1332, hub_3 1185 /
    cap(i)  capacity of facility i
        / hub_1 677, hub_2 502, hub_3 630 /
    d(j)    demand of customer j
        / c1 166, c2 263, c3 228, c4 278 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.c1 10, hub_1.c2 14, hub_1.c3 12, hub_1.c4 13, hub_2.c1 10, hub_2.c2 12, hub_2.c3 15, hub_2.c4 14, hub_3.c1 14, hub_3.c2 19, hub_3.c3 11, hub_3.c4 15 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2300.0

---

## Problem prob_171 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 1229
    - plant_B: 964
    - plant_C: 1046

- capacities:
    - plant_A: 645
    - plant_B: 641
    - plant_C: 492

- demands:
    - city_1: 178
    - city_2: 305
    - city_3: 264

- transport_costs:
    - plant_A: {'city_1': 16, 'city_2': 18, 'city_3': 19}
    - plant_B: {'city_1': 14, 'city_2': 11, 'city_3': 14}
    - plant_C: {'city_1': 19, 'city_2': 14, 'city_3': 17}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 1229; plant_B: 964; plant_C: 1046 (cost to open each facility)
- Capacities: plant_A: 645; plant_B: 641; plant_C: 492 (maximum output per facility)
- Customer demands: city_1: 178; city_2: 305; city_3: 264
- Transportation costs: plant_A -> city_1: 16, city_2: 18, city_3: 19; plant_B -> city_1: 14, city_2: 11, city_3: 14; plant_C -> city_1: 19, city_2: 14, city_3: 17

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 1229, plant_B 964, plant_C 1046 /
    cap(i)  capacity of facility i
        / plant_A 645, plant_B 641, plant_C 492 /
    d(j)    demand of customer j
        / city_1 178, city_2 305, city_3 264 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.city_1 16, plant_A.city_2 18, plant_A.city_3 19, plant_B.city_1 14, plant_B.city_2 11, plant_B.city_3 14, plant_C.city_1 19, plant_C.city_2 14, plant_C.city_3 17 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2050.0

---

## Problem prob_172 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 901
    - hub_2: 1000
    - hub_3: 1225

- capacities:
    - hub_1: 486
    - hub_2: 401
    - hub_3: 599

- demands:
    - city_1: 217
    - city_2: 280
    - city_3: 315

- transport_costs:
    - hub_1: {'city_1': 13, 'city_2': 12, 'city_3': 12}
    - hub_2: {'city_1': 12, 'city_2': 18, 'city_3': 17}
    - hub_3: {'city_1': 19, 'city_2': 17, 'city_3': 20}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 901; hub_2: 1000; hub_3: 1225 (cost to open each facility)
- Capacities: hub_1: 486; hub_2: 401; hub_3: 599 (maximum output per facility)
- Customer demands: city_1: 217; city_2: 280; city_3: 315
- Transportation costs: hub_1 -> city_1: 13, city_2: 12, city_3: 12; hub_2 -> city_1: 12, city_2: 18, city_3: 17; hub_3 -> city_1: 19, city_2: 17, city_3: 20

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 901, hub_2 1000, hub_3 1225 /
    cap(i)  capacity of facility i
        / hub_1 486, hub_2 401, hub_3 599 /
    d(j)    demand of customer j
        / city_1 217, city_2 280, city_3 315 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.city_1 13, hub_1.city_2 12, hub_1.city_3 12, hub_2.city_1 12, hub_2.city_2 18, hub_2.city_3 17, hub_3.city_1 19, hub_3.city_2 17, hub_3.city_3 20 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1800.0

---

## Problem prob_173 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 1022
    - hub_2: 1190
    - hub_3: 1319

- capacities:
    - hub_1: 552
    - hub_2: 548
    - hub_3: 582

- demands:
    - city_1: 217
    - city_2: 260
    - city_3: 284

- transport_costs:
    - hub_1: {'city_1': 16, 'city_2': 12, 'city_3': 11}
    - hub_2: {'city_1': 13, 'city_2': 17, 'city_3': 9}
    - hub_3: {'city_1': 13, 'city_2': 16, 'city_3': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 1022; hub_2: 1190; hub_3: 1319 (cost to open each facility)
- Capacities: hub_1: 552; hub_2: 548; hub_3: 582 (maximum output per facility)
- Customer demands: city_1: 217; city_2: 260; city_3: 284
- Transportation costs: hub_1 -> city_1: 16, city_2: 12, city_3: 11; hub_2 -> city_1: 13, city_2: 17, city_3: 9; hub_3 -> city_1: 13, city_2: 16, city_3: 12

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 1022, hub_2 1190, hub_3 1319 /
    cap(i)  capacity of facility i
        / hub_1 552, hub_2 548, hub_3 582 /
    d(j)    demand of customer j
        / city_1 217, city_2 260, city_3 284 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.city_1 16, hub_1.city_2 12, hub_1.city_3 11, hub_2.city_1 13, hub_2.city_2 17, hub_2.city_3 9, hub_3.city_1 13, hub_3.city_2 16, hub_3.city_3 12 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1700.0

---

## Problem prob_174 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 1055
    - plant_B: 969
    - plant_C: 1011

- capacities:
    - plant_A: 420
    - plant_B: 686
    - plant_C: 805

- demands:
    - c1: 169
    - c2: 298
    - c3: 273
    - c4: 437

- transport_costs:
    - plant_A: {'c1': 13, 'c2': 15, 'c3': 10, 'c4': 20}
    - plant_B: {'c1': 10, 'c2': 10, 'c3': 12, 'c4': 19}
    - plant_C: {'c1': 16, 'c2': 15, 'c3': 14, 'c4': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 1055; plant_B: 969; plant_C: 1011 (cost to open each facility)
- Capacities: plant_A: 420; plant_B: 686; plant_C: 805 (maximum output per facility)
- Customer demands: c1: 169; c2: 298; c3: 273; c4: 437
- Transportation costs: plant_A -> c1: 13, c2: 15, c3: 10, c4: 20; plant_B -> c1: 10, c2: 10, c3: 12, c4: 19; plant_C -> c1: 16, c2: 15, c3: 14, c4: 10

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 1055, plant_B 969, plant_C 1011 /
    cap(i)  capacity of facility i
        / plant_A 420, plant_B 686, plant_C 805 /
    d(j)    demand of customer j
        / c1 169, c2 298, c3 273, c4 437 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.c1 13, plant_A.c2 15, plant_A.c3 10, plant_A.c4 20, plant_B.c1 10, plant_B.c2 10, plant_B.c3 12, plant_B.c4 19, plant_C.c1 16, plant_C.c2 15, plant_C.c3 14, plant_C.c4 10 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2000.0

---

## Problem prob_175 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 1035
    - hub_2: 1214
    - hub_3: 1382

- capacities:
    - hub_1: 606
    - hub_2: 677
    - hub_3: 671

- demands:
    - c1: 206
    - c2: 291
    - c3: 332
    - c4: 434

- transport_costs:
    - hub_1: {'c1': 17, 'c2': 21, 'c3': 13, 'c4': 19}
    - hub_2: {'c1': 10, 'c2': 20, 'c3': 21, 'c4': 13}
    - hub_3: {'c1': 11, 'c2': 16, 'c3': 11, 'c4': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 1035; hub_2: 1214; hub_3: 1382 (cost to open each facility)
- Capacities: hub_1: 606; hub_2: 677; hub_3: 671 (maximum output per facility)
- Customer demands: c1: 206; c2: 291; c3: 332; c4: 434
- Transportation costs: hub_1 -> c1: 17, c2: 21, c3: 13, c4: 19; hub_2 -> c1: 10, c2: 20, c3: 21, c4: 13; hub_3 -> c1: 11, c2: 16, c3: 11, c4: 12

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 1035, hub_2 1214, hub_3 1382 /
    cap(i)  capacity of facility i
        / hub_1 606, hub_2 677, hub_3 671 /
    d(j)    demand of customer j
        / c1 206, c2 291, c3 332, c4 434 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.c1 17, hub_1.c2 21, hub_1.c3 13, hub_1.c4 19, hub_2.c1 10, hub_2.c2 20, hub_2.c3 21, hub_2.c4 13, hub_3.c1 11, hub_3.c2 16, hub_3.c3 11, hub_3.c4 12 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2500.0

---

## Problem prob_176 — Facility_Location

**Description:** Decide which facilities from plant_A, plant_B and plant_C to open to serve customers at c1, c2, c3 and c4 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - plant_A: 1214
    - plant_B: 1344
    - plant_C: 1331

- capacities:
    - plant_A: 529
    - plant_B: 556
    - plant_C: 870

- demands:
    - c1: 217
    - c2: 185
    - c3: 247
    - c4: 336

- transport_costs:
    - plant_A: {'c1': 20, 'c2': 14, 'c3': 10, 'c4': 19}
    - plant_B: {'c1': 10, 'c2': 15, 'c3': 18, 'c4': 20}
    - plant_C: {'c1': 15, 'c2': 16, 'c3': 16, 'c4': 10}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: plant_A, plant_B, plant_C (potential locations)
- Customers: c1, c2, c3, c4 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: plant_A: 1214; plant_B: 1344; plant_C: 1331 (cost to open each facility)
- Capacities: plant_A: 529; plant_B: 556; plant_C: 870 (maximum output per facility)
- Customer demands: c1: 217; c2: 185; c3: 247; c4: 336
- Transportation costs: plant_A -> c1: 20, c2: 14, c3: 10, c4: 19; plant_B -> c1: 10, c2: 15, c3: 18, c4: 20; plant_C -> c1: 15, c2: 16, c3: 16, c4: 10

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / plant_A, plant_B, plant_C /
    j   customers    / c1, c2, c3, c4 /;

Parameters
    f(i)    fixed cost of opening facility i
        / plant_A 1214, plant_B 1344, plant_C 1331 /
    cap(i)  capacity of facility i
        / plant_A 529, plant_B 556, plant_C 870 /
    d(j)    demand of customer j
        / c1 217, c2 185, c3 247, c4 336 /
    c(i,j)  transportation cost from facility i to customer j
        / plant_A.c1 20, plant_A.c2 14, plant_A.c3 10, plant_A.c4 19, plant_B.c1 10, plant_B.c2 15, plant_B.c3 18, plant_B.c4 20, plant_C.c1 15, plant_C.c2 16, plant_C.c3 16, plant_C.c4 10 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2200.0

---

## Problem prob_177 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 953
    - f2: 991
    - f3: 1559

- capacities:
    - f1: 678
    - f2: 541
    - f3: 868

- demands:
    - region_A: 180
    - region_B: 218
    - region_C: 257

- transport_costs:
    - f1: {'region_A': 9, 'region_B': 9, 'region_C': 18}
    - f2: {'region_A': 9, 'region_B': 15, 'region_C': 16}
    - f3: {'region_A': 14, 'region_B': 17, 'region_C': 12}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 953; f2: 991; f3: 1559 (cost to open each facility)
- Capacities: f1: 678; f2: 541; f3: 868 (maximum output per facility)
- Customer demands: region_A: 180; region_B: 218; region_C: 257
- Transportation costs: f1 -> region_A: 9, region_B: 9, region_C: 18; f2 -> region_A: 9, region_B: 15, region_C: 16; f3 -> region_A: 14, region_B: 17, region_C: 12

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 953, f2 991, f3 1559 /
    cap(i)  capacity of facility i
        / f1 678, f2 541, f3 868 /
    d(j)    demand of customer j
        / region_A 180, region_B 218, region_C 257 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.region_A 9, f1.region_B 9, f1.region_C 18, f2.region_A 9, f2.region_B 15, f2.region_C 16, f3.region_A 14, f3.region_B 17, f3.region_C 12 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1500.0

---

## Problem prob_178 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at city_1, city_2 and city_3 at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 1091
    - hub_2: 1351
    - hub_3: 1482

- capacities:
    - hub_1: 698
    - hub_2: 560
    - hub_3: 459

- demands:
    - city_1: 152
    - city_2: 293
    - city_3: 325

- transport_costs:
    - hub_1: {'city_1': 15, 'city_2': 16, 'city_3': 10}
    - hub_2: {'city_1': 11, 'city_2': 19, 'city_3': 19}
    - hub_3: {'city_1': 16, 'city_2': 18, 'city_3': 11}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: city_1, city_2, city_3 (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 1091; hub_2: 1351; hub_3: 1482 (cost to open each facility)
- Capacities: hub_1: 698; hub_2: 560; hub_3: 459 (maximum output per facility)
- Customer demands: city_1: 152; city_2: 293; city_3: 325
- Transportation costs: hub_1 -> city_1: 15, city_2: 16, city_3: 10; hub_2 -> city_1: 11, city_2: 19, city_3: 19; hub_3 -> city_1: 16, city_2: 18, city_3: 11

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / city_1, city_2, city_3 /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 1091, hub_2 1351, hub_3 1482 /
    cap(i)  capacity of facility i
        / hub_1 698, hub_2 560, hub_3 459 /
    d(j)    demand of customer j
        / city_1 152, city_2 293, city_3 325 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.city_1 15, hub_1.city_2 16, hub_1.city_3 10, hub_2.city_1 11, hub_2.city_2 19, hub_2.city_3 19, hub_3.city_1 16, hub_3.city_2 18, hub_3.city_3 11 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1850.0

---

## Problem prob_179 — Facility_Location

**Description:** Decide which facilities from f1, f2 and f3 to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - f1: 1140
    - f2: 1220
    - f3: 1655

- capacities:
    - f1: 364
    - f2: 788
    - f3: 743

- demands:
    - region_A: 237
    - region_B: 315
    - region_C: 344

- transport_costs:
    - f1: {'region_A': 19, 'region_B': 11, 'region_C': 14}
    - f2: {'region_A': 16, 'region_B': 13, 'region_C': 16}
    - f3: {'region_A': 21, 'region_B': 13, 'region_C': 19}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: f1, f2, f3 (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: f1: 1140; f2: 1220; f3: 1655 (cost to open each facility)
- Capacities: f1: 364; f2: 788; f3: 743 (maximum output per facility)
- Customer demands: region_A: 237; region_B: 315; region_C: 344
- Transportation costs: f1 -> region_A: 19, region_B: 11, region_C: 14; f2 -> region_A: 16, region_B: 13, region_C: 16; f3 -> region_A: 21, region_B: 13, region_C: 19

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / f1, f2, f3 /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / f1 1140, f2 1220, f3 1655 /
    cap(i)  capacity of facility i
        / f1 364, f2 788, f3 743 /
    d(j)    demand of customer j
        / region_A 237, region_B 315, region_C 344 /
    c(i,j)  transportation cost from facility i to customer j
        / f1.region_A 19, f1.region_B 11, f1.region_C 14, f2.region_A 16, f2.region_B 13, f2.region_C 16, f3.region_A 21, f3.region_B 13, f3.region_C 19 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=2050.0

---

## Problem prob_180 — Facility_Location

**Description:** Decide which facilities from hub_1, hub_2 and hub_3 to open to serve customers at region_A, region_B and region_C at minimum cost, considering fixed costs and transport costs.

**Supplementary Tables:**
- fixed_costs:
    - hub_1: 927
    - hub_2: 1075
    - hub_3: 1267

- capacities:
    - hub_1: 555
    - hub_2: 395
    - hub_3: 566

- demands:
    - region_A: 185
    - region_B: 270
    - region_C: 311

- transport_costs:
    - hub_1: {'region_A': 12, 'region_B': 21, 'region_C': 18}
    - hub_2: {'region_A': 16, 'region_B': 16, 'region_C': 15}
    - hub_3: {'region_A': 16, 'region_B': 10, 'region_C': 13}

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Facility Location

SETS IDENTIFICATION:
- Facilities: hub_1, hub_2, hub_3 (potential locations)
- Customers: region_A, region_B, region_C (demand points)

PARAMETERS DEFINITION:
- Fixed costs: hub_1: 927; hub_2: 1075; hub_3: 1267 (cost to open each facility)
- Capacities: hub_1: 555; hub_2: 395; hub_3: 566 (maximum output per facility)
- Customer demands: region_A: 185; region_B: 270; region_C: 311
- Transportation costs: hub_1 -> region_A: 12, region_B: 21, region_C: 18; hub_2 -> region_A: 16, region_B: 16, region_C: 15; hub_3 -> region_A: 16, region_B: 10, region_C: 13

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
- Balance fixed costs vs transportation costs
```

**Generated GAMS Program:**

```GAMS
Sets
    i   facilities   / hub_1, hub_2, hub_3 /
    j   customers    / region_A, region_B, region_C /;

Parameters
    f(i)    fixed cost of opening facility i
        / hub_1 927, hub_2 1075, hub_3 1267 /
    cap(i)  capacity of facility i
        / hub_1 555, hub_2 395, hub_3 566 /
    d(j)    demand of customer j
        / region_A 185, region_B 270, region_C 311 /
    c(i,j)  transportation cost from facility i to customer j
        / hub_1.region_A 12, hub_1.region_B 21, hub_1.region_C 18, hub_2.region_A 16, hub_2.region_B 16, hub_2.region_C 15, hub_3.region_A 16, hub_3.region_B 10, hub_3.region_C 13 /;

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
display z.l, y.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=1750.0

---

## Problem prob_181 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 22
    - item_Y: 36
    - item_Z: 44

- machine_hours:
    - item_X: 2
    - item_Y: 2
    - item_Z: 3

- labor_hours:
    - item_X: 3
    - item_Y: 4
    - item_Z: 4

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 22; item_Y: 36; item_Z: 44
- Machine requirements: item_X: 2; item_Y: 2; item_Z: 3
- Labor requirements: item_X: 3; item_Y: 4; item_Z: 4
- Resource limits: Machine hours: 104, Labor hours: 108

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 22, item_Y 36, item_Z 44 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 2, item_Z 3 /
    labor(i)    labor hours required per unit of product i
        / item_X 3, item_Y 4, item_Z 4 /;

Scalars
    max_machine   maximum machine hours available / 104 /
    max_labor     maximum labor hours available / 108 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_182 — Generic_Lp

**Description:** Decide production levels of p1, p2 and p3 to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - p1: 18
    - p2: 29
    - p3: 26

- machine_hours:
    - p1: 2
    - p2: 2
    - p3: 5

- labor_hours:
    - p1: 3
    - p2: 4
    - p3: 4

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: p1, p2, p3 (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: p1: 18; p2: 29; p3: 26
- Machine requirements: p1: 2; p2: 2; p3: 5
- Labor requirements: p1: 3; p2: 4; p3: 4
- Resource limits: Machine hours: 91, Labor hours: 118

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / p1, p2, p3 /;

Parameters
    profit(i)   profit per unit of product i
        / p1 18, p2 29, p3 26 /
    machine(i)  machine hours required per unit of product i
        / p1 2, p2 2, p3 5 /
    labor(i)    labor hours required per unit of product i
        / p1 3, p2 4, p3 4 /;

Scalars
    max_machine   maximum machine hours available / 91 /
    max_labor     maximum labor hours available / 118 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_183 — Generic_Lp

**Description:** Decide production levels of product_A, product_B and product_C to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - product_A: 27
    - product_B: 34
    - product_C: 39

- machine_hours:
    - product_A: 2
    - product_B: 3
    - product_C: 5

- labor_hours:
    - product_A: 3
    - product_B: 4
    - product_C: 6

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: product_A, product_B, product_C (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: product_A: 27; product_B: 34; product_C: 39
- Machine requirements: product_A: 2; product_B: 3; product_C: 5
- Labor requirements: product_A: 3; product_B: 4; product_C: 6
- Resource limits: Machine hours: 108, Labor hours: 113

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / product_A, product_B, product_C /;

Parameters
    profit(i)   profit per unit of product i
        / product_A 27, product_B 34, product_C 39 /
    machine(i)  machine hours required per unit of product i
        / product_A 2, product_B 3, product_C 5 /
    labor(i)    labor hours required per unit of product i
        / product_A 3, product_B 4, product_C 6 /;

Scalars
    max_machine   maximum machine hours available / 108 /
    max_labor     maximum labor hours available / 113 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_184 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 30
    - item_Y: 26
    - item_Z: 40

- machine_hours:
    - item_X: 2
    - item_Y: 3
    - item_Z: 5

- labor_hours:
    - item_X: 3
    - item_Y: 4
    - item_Z: 5

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 30; item_Y: 26; item_Z: 40
- Machine requirements: item_X: 2; item_Y: 3; item_Z: 5
- Labor requirements: item_X: 3; item_Y: 4; item_Z: 5
- Resource limits: Machine hours: 92, Labor hours: 127

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 30, item_Y 26, item_Z 40 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 3, item_Z 5 /
    labor(i)    labor hours required per unit of product i
        / item_X 3, item_Y 4, item_Z 5 /;

Scalars
    max_machine   maximum machine hours available / 92 /
    max_labor     maximum labor hours available / 127 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_185 — Generic_Lp

**Description:** Decide production levels of p1, p2 and p3 to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - p1: 31
    - p2: 27
    - p3: 35

- machine_hours:
    - p1: 2
    - p2: 3
    - p3: 4

- labor_hours:
    - p1: 3
    - p2: 4
    - p3: 6

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: p1, p2, p3 (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: p1: 31; p2: 27; p3: 35
- Machine requirements: p1: 2; p2: 3; p3: 4
- Labor requirements: p1: 3; p2: 4; p3: 6
- Resource limits: Machine hours: 106, Labor hours: 124

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / p1, p2, p3 /;

Parameters
    profit(i)   profit per unit of product i
        / p1 31, p2 27, p3 35 /
    machine(i)  machine hours required per unit of product i
        / p1 2, p2 3, p3 4 /
    labor(i)    labor hours required per unit of product i
        / p1 3, p2 4, p3 6 /;

Scalars
    max_machine   maximum machine hours available / 106 /
    max_labor     maximum labor hours available / 124 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_186 — Generic_Lp

**Description:** Decide production levels of product_A, product_B and product_C to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - product_A: 31
    - product_B: 33
    - product_C: 31

- machine_hours:
    - product_A: 2
    - product_B: 3
    - product_C: 5

- labor_hours:
    - product_A: 3
    - product_B: 4
    - product_C: 6

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: product_A, product_B, product_C (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: product_A: 31; product_B: 33; product_C: 31
- Machine requirements: product_A: 2; product_B: 3; product_C: 5
- Labor requirements: product_A: 3; product_B: 4; product_C: 6
- Resource limits: Machine hours: 104, Labor hours: 128

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / product_A, product_B, product_C /;

Parameters
    profit(i)   profit per unit of product i
        / product_A 31, product_B 33, product_C 31 /
    machine(i)  machine hours required per unit of product i
        / product_A 2, product_B 3, product_C 5 /
    labor(i)    labor hours required per unit of product i
        / product_A 3, product_B 4, product_C 6 /;

Scalars
    max_machine   maximum machine hours available / 104 /
    max_labor     maximum labor hours available / 128 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_187 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 19
    - item_Y: 25
    - item_Z: 40

- machine_hours:
    - item_X: 2
    - item_Y: 3
    - item_Z: 4

- labor_hours:
    - item_X: 2
    - item_Y: 4
    - item_Z: 4

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 19; item_Y: 25; item_Z: 40
- Machine requirements: item_X: 2; item_Y: 3; item_Z: 4
- Labor requirements: item_X: 2; item_Y: 4; item_Z: 4
- Resource limits: Machine hours: 96, Labor hours: 110

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 19, item_Y 25, item_Z 40 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 3, item_Z 4 /
    labor(i)    labor hours required per unit of product i
        / item_X 2, item_Y 4, item_Z 4 /;

Scalars
    max_machine   maximum machine hours available / 96 /
    max_labor     maximum labor hours available / 110 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_188 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 26
    - item_Y: 35
    - item_Z: 25

- machine_hours:
    - item_X: 2
    - item_Y: 3
    - item_Z: 5

- labor_hours:
    - item_X: 3
    - item_Y: 5
    - item_Z: 5

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 26; item_Y: 35; item_Z: 25
- Machine requirements: item_X: 2; item_Y: 3; item_Z: 5
- Labor requirements: item_X: 3; item_Y: 5; item_Z: 5
- Resource limits: Machine hours: 107, Labor hours: 127

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 26, item_Y 35, item_Z 25 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 3, item_Z 5 /
    labor(i)    labor hours required per unit of product i
        / item_X 3, item_Y 5, item_Z 5 /;

Scalars
    max_machine   maximum machine hours available / 107 /
    max_labor     maximum labor hours available / 127 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_189 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 26
    - item_Y: 31
    - item_Z: 41

- machine_hours:
    - item_X: 2
    - item_Y: 3
    - item_Z: 4

- labor_hours:
    - item_X: 3
    - item_Y: 4
    - item_Z: 5

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 26; item_Y: 31; item_Z: 41
- Machine requirements: item_X: 2; item_Y: 3; item_Z: 4
- Labor requirements: item_X: 3; item_Y: 4; item_Z: 5
- Resource limits: Machine hours: 90, Labor hours: 124

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 26, item_Y 31, item_Z 41 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 3, item_Z 4 /
    labor(i)    labor hours required per unit of product i
        / item_X 3, item_Y 4, item_Z 5 /;

Scalars
    max_machine   maximum machine hours available / 90 /
    max_labor     maximum labor hours available / 124 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_190 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 28
    - item_Y: 27
    - item_Z: 42

- machine_hours:
    - item_X: 2
    - item_Y: 3
    - item_Z: 3

- labor_hours:
    - item_X: 3
    - item_Y: 4
    - item_Z: 5

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 28; item_Y: 27; item_Z: 42
- Machine requirements: item_X: 2; item_Y: 3; item_Z: 3
- Labor requirements: item_X: 3; item_Y: 4; item_Z: 5
- Resource limits: Machine hours: 104, Labor hours: 120

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 28, item_Y 27, item_Z 42 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 3, item_Z 3 /
    labor(i)    labor hours required per unit of product i
        / item_X 3, item_Y 4, item_Z 5 /;

Scalars
    max_machine   maximum machine hours available / 104 /
    max_labor     maximum labor hours available / 120 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_191 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 18
    - item_Y: 23
    - item_Z: 29

- machine_hours:
    - item_X: 2
    - item_Y: 2
    - item_Z: 4

- labor_hours:
    - item_X: 4
    - item_Y: 4
    - item_Z: 5

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 18; item_Y: 23; item_Z: 29
- Machine requirements: item_X: 2; item_Y: 2; item_Z: 4
- Labor requirements: item_X: 4; item_Y: 4; item_Z: 5
- Resource limits: Machine hours: 110, Labor hours: 110

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 18, item_Y 23, item_Z 29 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 2, item_Z 4 /
    labor(i)    labor hours required per unit of product i
        / item_X 4, item_Y 4, item_Z 5 /;

Scalars
    max_machine   maximum machine hours available / 110 /
    max_labor     maximum labor hours available / 110 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_192 — Generic_Lp

**Description:** Decide production levels of product_A, product_B and product_C to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - product_A: 26
    - product_B: 34
    - product_C: 37

- machine_hours:
    - product_A: 2
    - product_B: 3
    - product_C: 4

- labor_hours:
    - product_A: 3
    - product_B: 4
    - product_C: 5

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: product_A, product_B, product_C (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: product_A: 26; product_B: 34; product_C: 37
- Machine requirements: product_A: 2; product_B: 3; product_C: 4
- Labor requirements: product_A: 3; product_B: 4; product_C: 5
- Resource limits: Machine hours: 107, Labor hours: 131

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / product_A, product_B, product_C /;

Parameters
    profit(i)   profit per unit of product i
        / product_A 26, product_B 34, product_C 37 /
    machine(i)  machine hours required per unit of product i
        / product_A 2, product_B 3, product_C 4 /
    labor(i)    labor hours required per unit of product i
        / product_A 3, product_B 4, product_C 5 /;

Scalars
    max_machine   maximum machine hours available / 107 /
    max_labor     maximum labor hours available / 131 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_193 — Generic_Lp

**Description:** Decide production levels of product_A, product_B and product_C to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - product_A: 22
    - product_B: 30
    - product_C: 37

- machine_hours:
    - product_A: 2
    - product_B: 3
    - product_C: 4

- labor_hours:
    - product_A: 4
    - product_B: 4
    - product_C: 4

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: product_A, product_B, product_C (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: product_A: 22; product_B: 30; product_C: 37
- Machine requirements: product_A: 2; product_B: 3; product_C: 4
- Labor requirements: product_A: 4; product_B: 4; product_C: 4
- Resource limits: Machine hours: 96, Labor hours: 115

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / product_A, product_B, product_C /;

Parameters
    profit(i)   profit per unit of product i
        / product_A 22, product_B 30, product_C 37 /
    machine(i)  machine hours required per unit of product i
        / product_A 2, product_B 3, product_C 4 /
    labor(i)    labor hours required per unit of product i
        / product_A 4, product_B 4, product_C 4 /;

Scalars
    max_machine   maximum machine hours available / 96 /
    max_labor     maximum labor hours available / 115 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_194 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 25
    - item_Y: 28
    - item_Z: 34

- machine_hours:
    - item_X: 2
    - item_Y: 3
    - item_Z: 5

- labor_hours:
    - item_X: 3
    - item_Y: 4
    - item_Z: 6

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 25; item_Y: 28; item_Z: 34
- Machine requirements: item_X: 2; item_Y: 3; item_Z: 5
- Labor requirements: item_X: 3; item_Y: 4; item_Z: 6
- Resource limits: Machine hours: 106, Labor hours: 112

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 25, item_Y 28, item_Z 34 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 3, item_Z 5 /
    labor(i)    labor hours required per unit of product i
        / item_X 3, item_Y 4, item_Z 6 /;

Scalars
    max_machine   maximum machine hours available / 106 /
    max_labor     maximum labor hours available / 112 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_195 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 29
    - item_Y: 22
    - item_Z: 25

- machine_hours:
    - item_X: 2
    - item_Y: 3
    - item_Z: 3

- labor_hours:
    - item_X: 3
    - item_Y: 4
    - item_Z: 5

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 29; item_Y: 22; item_Z: 25
- Machine requirements: item_X: 2; item_Y: 3; item_Z: 3
- Labor requirements: item_X: 3; item_Y: 4; item_Z: 5
- Resource limits: Machine hours: 99, Labor hours: 121

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 29, item_Y 22, item_Z 25 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 3, item_Z 3 /
    labor(i)    labor hours required per unit of product i
        / item_X 3, item_Y 4, item_Z 5 /;

Scalars
    max_machine   maximum machine hours available / 99 /
    max_labor     maximum labor hours available / 121 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_196 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 31
    - item_Y: 25
    - item_Z: 28

- machine_hours:
    - item_X: 2
    - item_Y: 3
    - item_Z: 3

- labor_hours:
    - item_X: 3
    - item_Y: 4
    - item_Z: 4

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 31; item_Y: 25; item_Z: 28
- Machine requirements: item_X: 2; item_Y: 3; item_Z: 3
- Labor requirements: item_X: 3; item_Y: 4; item_Z: 4
- Resource limits: Machine hours: 109, Labor hours: 113

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 31, item_Y 25, item_Z 28 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 3, item_Z 3 /
    labor(i)    labor hours required per unit of product i
        / item_X 3, item_Y 4, item_Z 4 /;

Scalars
    max_machine   maximum machine hours available / 109 /
    max_labor     maximum labor hours available / 113 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_197 — Generic_Lp

**Description:** Decide production levels of product_A, product_B and product_C to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - product_A: 32
    - product_B: 32
    - product_C: 43

- machine_hours:
    - product_A: 2
    - product_B: 4
    - product_C: 4

- labor_hours:
    - product_A: 2
    - product_B: 5
    - product_C: 5

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: product_A, product_B, product_C (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: product_A: 32; product_B: 32; product_C: 43
- Machine requirements: product_A: 2; product_B: 4; product_C: 4
- Labor requirements: product_A: 2; product_B: 5; product_C: 5
- Resource limits: Machine hours: 94, Labor hours: 121

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / product_A, product_B, product_C /;

Parameters
    profit(i)   profit per unit of product i
        / product_A 32, product_B 32, product_C 43 /
    machine(i)  machine hours required per unit of product i
        / product_A 2, product_B 4, product_C 4 /
    labor(i)    labor hours required per unit of product i
        / product_A 2, product_B 5, product_C 5 /;

Scalars
    max_machine   maximum machine hours available / 94 /
    max_labor     maximum labor hours available / 121 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_198 — Generic_Lp

**Description:** Decide production levels of product_A, product_B and product_C to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - product_A: 21
    - product_B: 28
    - product_C: 34

- machine_hours:
    - product_A: 2
    - product_B: 3
    - product_C: 4

- labor_hours:
    - product_A: 3
    - product_B: 4
    - product_C: 5

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: product_A, product_B, product_C (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: product_A: 21; product_B: 28; product_C: 34
- Machine requirements: product_A: 2; product_B: 3; product_C: 4
- Labor requirements: product_A: 3; product_B: 4; product_C: 5
- Resource limits: Machine hours: 101, Labor hours: 120

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / product_A, product_B, product_C /;

Parameters
    profit(i)   profit per unit of product i
        / product_A 21, product_B 28, product_C 34 /
    machine(i)  machine hours required per unit of product i
        / product_A 2, product_B 3, product_C 4 /
    labor(i)    labor hours required per unit of product i
        / product_A 3, product_B 4, product_C 5 /;

Scalars
    max_machine   maximum machine hours available / 101 /
    max_labor     maximum labor hours available / 120 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_199 — Generic_Lp

**Description:** Decide production levels of p1, p2 and p3 to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - p1: 30
    - p2: 27
    - p3: 34

- machine_hours:
    - p1: 2
    - p2: 2
    - p3: 4

- labor_hours:
    - p1: 3
    - p2: 3
    - p3: 4

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: p1, p2, p3 (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: p1: 30; p2: 27; p3: 34
- Machine requirements: p1: 2; p2: 2; p3: 4
- Labor requirements: p1: 3; p2: 3; p3: 4
- Resource limits: Machine hours: 104, Labor hours: 125

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / p1, p2, p3 /;

Parameters
    profit(i)   profit per unit of product i
        / p1 30, p2 27, p3 34 /
    machine(i)  machine hours required per unit of product i
        / p1 2, p2 2, p3 4 /
    labor(i)    labor hours required per unit of product i
        / p1 3, p2 3, p3 4 /;

Scalars
    max_machine   maximum machine hours available / 104 /
    max_labor     maximum labor hours available / 125 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

## Problem prob_200 — Generic_Lp

**Description:** Decide production levels of item_X, item_Y and item_Z to maximize profit subject to machine and labor capacity limits.

**Supplementary Tables:**
- profit:
    - item_X: 32
    - item_Y: 37
    - item_Z: 31

- machine_hours:
    - item_X: 2
    - item_Y: 3
    - item_Z: 3

- labor_hours:
    - item_X: 2
    - item_Y: 5
    - item_Z: 4

- max_machine_hours:

- max_labor_hours:

**Chain-of-Thought Reasoning:**

```
PROBLEM ANALYSIS: Production Planning

SETS IDENTIFICATION:
- Products: item_X, item_Y, item_Z (items to be produced)

PARAMETERS DEFINITION:
- Profit margins: item_X: 32; item_Y: 37; item_Z: 31
- Machine requirements: item_X: 2; item_Y: 3; item_Z: 3
- Labor requirements: item_X: 2; item_Y: 5; item_Z: 4
- Resource limits: Machine hours: 109, Labor hours: 115

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
- Continuous production decisions
```

**Generated GAMS Program:**

```GAMS
Sets
    i   products   / item_X, item_Y, item_Z /;

Parameters
    profit(i)   profit per unit of product i
        / item_X 32, item_Y 37, item_Z 31 /
    machine(i)  machine hours required per unit of product i
        / item_X 2, item_Y 3, item_Z 3 /
    labor(i)    labor hours required per unit of product i
        / item_X 2, item_Y 5, item_Z 4 /;

Scalars
    max_machine   maximum machine hours available / 109 /
    max_labor     maximum labor hours available / 115 /;

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
display z.l, x.l;
```

**Verification:** static_valid=True, solver_success=True, objective=180.0

---

