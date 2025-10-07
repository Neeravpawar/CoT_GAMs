Sets
    plants     / seattle, san-diego /
    markets    / new-york, chicago, topeka /;

Parameters
    supply(plants)   / seattle     350
                      san-diego   600  /
    demand(markets)  / new-york    325
                      chicago     300
                      topeka      275  /
    cost(plants, markets) 
        / seattle .new-york    2.5
          seattle .chicago     1.7
          seattle .topeka      1.8
          san-diego.new-york   2.5
          san-diego.chicago    1.8
          san-diego.topeka     1.4  /;

Variables
    x(plants, markets)  Shipment quantities in cases
    z                   Total transportation costs in thousands of dollars;

Positive Variable x;

Equations
    supply_constraint(plants)   Supply limit at plant i
    demand_constraint(markets)  Demand requirement at market j
    objective_function;         Total cost minimization

supply_constraint(plants)..
    sum(markets, x(plants, markets)) =l= supply(plants);

demand_constraint(markets)..
    sum(plants, x(plants, markets)) =g= demand(markets);

objective_function..
    z =e= sum((plants, markets), cost(plants, markets) * x(plants, markets));

Model transport / all /;
Solve transport using lp minimizing z;

Display x.l, z.l;