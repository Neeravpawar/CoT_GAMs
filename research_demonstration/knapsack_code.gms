Sets
    items / item1, item2, item3, item4, item5, item6 /;

Parameters
    weight(items) / item1   2
                   item2   5
                   item3   8
                   item4   3
                   item5   6
                   item6   4  /
    value(items)  / item1  15
                   item2  30
                   item3  45
                   item4  20
                   item5  35
                   item6  25  /
    capacity      / 15 /;

Binary Variables
    select(items)  Selection decision (1 if item selected, 0 otherwise);

Variables
    z  Total value of selected items;

Equations
    weight_constraint  Total weight must not exceed capacity
    objective_function;

weight_constraint..
    sum(items, weight(items) * select(items)) =l= capacity;

objective_function..
    z =e= sum(items, value(items) * select(items));

Model knapsack / all /;
Solve knapsack using mip maximizing z;

Display select.l, z.l;