![[image.png]]


1. Run Uniform-cost-search

Queue   |   Done

| Queue                             | Done          |
| --------------------------------- | ------------- |
| A                                 |               |
| B(2), D(4),C(5)                   | A             |
| D(4), E(4), C(5)                  | A,B           |
| E(4),C(5)                         | A,B,D         |
| B(5, already visited), C(5)       | A,B,D,E       |
| A(6, already visited), G(6),H(7), | A,B,D,E,C     |
| D(9, already visited),H(7),I(10), | A,B,D,E,C,G   |
| I(8),I(10)                        | A,B,D,E,C,G,H |
Fastest path is via I(8), the solution found is optimal, (found both ways to reach I, also the shortest)

