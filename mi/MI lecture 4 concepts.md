
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

a graph is singly connected or a poly-tree if there is at most one un-directed path between any two nodes in the graph.



##### d-separation
if two variables are conditionally independent, if more information is added to the graph, they might not be anymore. 

conditional independence with serial states slide 28 (flowing method)
conditional independence with diverging connection slide 29 (common cause)
conditional independence with converging connection slide 30 (common cause)

d-separation algorithm slide 34 

##### approximate inference

probability of evidence
Hoeffding bound = how many iterations to i have to run to get a estimate of how likely some outcome based on a Bayesian network is, based on some error chance i.e. i want to have at most 0.01 error 99% of the time.

probability of evidence given some information
likelihood weighting 




