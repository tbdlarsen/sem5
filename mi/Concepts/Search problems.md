In search problems we assume the following things: 

* There is a finite discrete number of states and actions
* It is a single agent environment 
* The state space is fully observable
* The state space is deterministic 
* It is Static

## State space
The formal definition of a search problem, State spaces are annotated directed graphs, paths to goal states correspond to solutions, the cheapest path to a goal state corresponds to the optimal solution.

A State space is a 6-tuple $\Theta = (S,A,c,T,I,S^G)$ where:
$S \text{ is a finite set of states}$ 
$A \text{ is a finite set of actions}$ 
$c: A \to \mathbb{R}_+^0 \text{ is the cost function}$
$T \subseteq S \times A \times S \text{ is the transition relation}$
We require that T is deterministic so:
$\forall s \in S, \forall a \in A, \exists! s' \in S : (s,a,s') \in T$
$a \text{ is applicable to } s \iff \exists s' \in S : (s,a,s') \in T$
$I \in S \text{ is the initial state}$
$S^G \subseteq S \text{ is the set goal state}$


if $\Theta$ has the transition $(s,a,s') \in T$. It can also be denoted as $s \rightarrow s'$ if we are not interested in a, or $s \xrightarrow{a} s'$  if we are.

we say that $\Theta$ has unit costs if $\forall a \in A, c(a) = 1$

$s' \text{ is a successor of } s \iff \exists a \in A : s \xrightarrow{a} s'$
$s \text{ is a predecessor of } s' \iff \exists a \in A : s \xrightarrow{a} s'$

$s' \text{ is reachable from } s \iff \exists n \geq 0, \exists a_0,...,a_{n-1} \in A, \exists s_1,...,s_n \in S : s \xrightarrow{a_0} s_1 \xrightarrow{a_1}... \xrightarrow{a_{n-1}} s_n = s'$
where $a_0,... a_{n-1}$ is the the path from $s \text{ to } s'$, we can also use $s,... ,s_n$ as the path
the total cost of the path is $\sum_{i=0}^{n-1} c(a_i)$


if no reference given ($s'$ is reachable) it is implied it is from $I$
$s$ is solvable if $\exists s' \in S^G$ that is reachable from $s$, else $s$ is a _dead end_


