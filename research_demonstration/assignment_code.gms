Sets
    workers / alice, bob, charlie /
    tasks   / task1, task2, task3 /;

Table cost(workers, tasks) Assignment costs
          task1   task2   task3
alice       10      12      15
bob          8      11      13
charlie      9      14      10;

Binary Variables
    assign(workers, tasks)  Assignment decision (1 if assigned, 0 otherwise);

Variables
    z  Total assignment cost;

Equations
    worker_assignment(workers)  Each worker assigned to exactly one task
    task_coverage(tasks)        Each task covered by exactly one worker
    total_cost;                 Objective function

worker_assignment(workers)..
    sum(tasks, assign(workers, tasks)) =e= 1;

task_coverage(tasks)..
    sum(workers, assign(workers, tasks)) =e= 1;

total_cost..
    z =e= sum((workers, tasks), cost(workers, tasks) * assign(workers, tasks));

Model assignment / all /;
Solve assignment using mip minimizing z;

Display assign.l, z.l;