## Serializability
given the transactions $T_1, T_2, T_3, T_4$ in the table where `R()` and `W()` are for _Read_ and _Write_ 

| Time  | $t_1$  | $t_2$  | $t_3$  | $t_4$  | $t_5$  | $t_6$  | $t_7$  | $t_8$  | $t_9$  | $t_{10}$ |
| ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | -------- |
| $T_1$ |        |        | `W(E)` |        | `R(D)` |        |        |        | `W(A)` |          |
| $T_2$ |        | `W(B)` |        | `R(A)` |        |        |        |        |        |          |
| $T_3$ |        |        |        |        |        |        |        | `R(E)` |        | `W(C)`   |
| $T_4$ | `W(D)` |        |        |        |        | `R(B)` | `R(C)` |        |        |          |

Draw the correct conflict dependency graph for the schedule. 

![[conflict-dependency-graph.png]]

1. Is this schedule serial
	1. Since there are not cycles in the graph the schedule is not serial
2. Is the schedule conflict serializable
	1. Since the graph is acyclic, yes 
3. What is the minimum number of transactions that need to be removed to produce a conflict serializable schedule
	1. Zero
4. Is the schedule above conflict equivalent to the schedule $T_2, T_4, T_1, T_3$ 

| Time  | $t_1$  | $t_2$  | $t_3$  | $t_4$  | $t_5$  | $t_6$  | $t_7$  | $t_8$  | $t_9$  | $t_{10}$ |
| ----- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ | -------- |
| $T_2$ |        | `W(B)` |        | `R(A)` |        |        |        |        |        |          |
| $T_4$ | `W(D)` |        |        |        |        | `R(B)` | `R(C)` |        |        |          |
| $T_1$ |        |        | `W(E)` |        | `R(D)` |        |        |        | `W(A)` |          |
| $T_3$ |        |        |        |        |        |        |        | `R(E)` |        | `W(C)`   |

| Conflict schedule 1                  | Conflict schedule 2 |
| ------------------------------------ | ------------------- |
| $T_4.W(D)\rightsquigarrow T_1.R(D)$  |                     |
| $T_2.W(B)\rightsquigarrow T_4.R(B)$  |                     |
| $T_1.W(E)\rightsquigarrow T_3.R(E)$  |                     |
| $T_2.R(A)\rightsquigarrow T_1.W(A)$  |                     |
| $T_4.R(C) \rightsquigarrow T_3.W(C)$ |                     |
