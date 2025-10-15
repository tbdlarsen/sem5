


# Task 1 
Based on task given in sheet 10

## a) Give an optimal plan for $\Pi$. what is the value of $h^*(I)$ 

STRIPS planning task, is a 4-tuple $\Pi = (P,A,I,G)$ where:
P is a finite set of facts (propositions), things that can be true i.e. $\{At(x) | x \in A\}$ 
A is a finite set of actions; each $a \in A$ is a triple $a = (pre_a,add_a,del_a)$ of subsets of P refered to as the action's precondition, add list and delete list respectively. we require that $add_a \cap del_a = \emptyset$. 
$I \subseteq P$ is the initial state
$G \subseteq P$ is the goal state




# Task 2 

1. Complete the formalization of the planning task. 

$P = \{at(Steffi,x), At(Letter,x),Carrying(Letter),empty\} | x \in \{Mensa, AStA, Council\}$  
$I = \{at(Steffi,Mensa),at(Letter,Council),empty\}$
$G = \{at(Steffi,Mensa),at(Letter,ASta)\}$
$A = \{fly(x,y)|(x,y) \in \{Mensa,AStA,Council\}\}$
	$\cup \{pickup(i,x)| x \in \{Council\}, i \in \{Letter\}\}$
	$\cup \{drop(i,x)| x \in \{AStA\}, i \in \{Letter\}\}$

$fly(x,y):$ 
	$pre:\{at(Steffi,x)\}$,
	$add:\{at(Steffi,y)\}$,
	$del:\{at(Steffi,x)\}$
	
$pickup(i,x):$
	$pre\{at(Steffi,x),At(Letter,i),empty\},$
	$add\{carrying(Letter)\},$
	$del\{at(Letter,i),empty\}$
$drop(i,x):$
	$pre\{at(Steffi,x),carrying(i)\},$
	$add\{empty\},$
	$del\{carrying(i)\}$

2. Give an optimal plan for the task
$<fly(Mensa,Council),pickup(Letter,Council),fly(Council,AStA),drop(Letter,AStA),fly(AStA,Council)>$
	1. the optimal path has 5 actions, so $h^*(I)=5$
	