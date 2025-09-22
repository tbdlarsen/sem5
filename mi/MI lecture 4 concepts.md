
##### Probabilistic inference
sort variables in 3 categories

// the 'given variables' (lower-case)
Evidence variables
P(Burglary | _johncalls_)

//the variables to find out (upper-case)
query variables
P(_Johncalls_)

the rest (hidden variables)
value unknown - it is not important to the solution

use normalization 
see slide 9 

inference by enumeration 

a graph is singly connected or a polytree if there is at most one undirected path between any two nodes in the graph.

if two variables are conditionally independent, if more information is added to the graph, they might not be anymore. 

conditional independence with hidden states slide 28 (flowing method)
conditional independence with diverging connection slide 29 (common cause)
conditional independence with converging connection slide 30 (common cause)

