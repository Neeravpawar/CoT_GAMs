Sets
    products  / product1, product2, product3 /
    resources / resource1, resource2, resource3 /;

Parameters
    profit(products) / product1   12
                      product2   18
                      product3   15  /
    usage(products, resources) Resource usage rates
        / product1.resource1   2
          product1.resource2   1
          product1.resource3   3
          product2.resource1   1
          product2.resource2   3
          product2.resource3   2
          product3.resource1   3
          product3.resource2   2
          product3.resource3   1  /
    available(resources) / resource1   100
                          resource2   120
                          resource3    90  /;

Positive Variables
    produce(products)  Production quantity of each product;

Variables
    z  Total profit;

Equations
    resource_limit(resources)  Resource availability constraints
    total_profit;

resource_limit(resources)..
    sum(products, usage(products, resources) * produce(products)) =l= available(resources);

total_profit..
    z =e= sum(products, profit(products) * produce(products));

Model production / all /;
Solve production using lp maximizing z;

Display produce.l, z.l;