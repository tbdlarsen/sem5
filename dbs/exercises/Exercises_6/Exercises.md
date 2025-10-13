


| Relation   | Primary key |
| ---------- | ----------- |
| `R(a,b,c)` | `(a,b)`     |
| `S(a,d)`   | `(a)`       |
| `T(a,e,f)` | `(a,f)`     |
To be joined on `a`

assume:
* B= 445 pages in buffer
* R spans M = 1500 pages with 80 tuples per page
* S pans N = 4500 pages with 150 tuples  per page
* T spans O = 200 pages with 250 tuples per page
* 1 buffer block for output, and 1 buffer block for input, so
  K = B-2

# Exercise 1 
assume no indexes

I/O cost of Block nested loop k buffers = $N^P+(\lceil N^P/K \rceil \times N^C)$
where 
$N^P$ is number of pages in outer relation
$N^C$ is number of pages in inner relation
$K$ is number of buffers available

a) Cost of block nested loop join with S as outer and R as inner, see `Exercises.py`
`I/O cost = 21000`
b) Cost of block nested loop join with R as outer and S as inner, see `Exercises.py`
`I/O cost = 19500`
c) Cost of block nested loop join with R as outer and T as inner, see `Exercises.py`
`I/O cost = 2300`

# Exercise 2
# Exercise 3
consider:

| Relation     | Primary key |
| ------------ | ----------- |
| $r_1(A,B,C)$ | $A$         |
| $r_2(C,D,E)$ | $C$         |
| $r_3(E,F)$   | $E$         |
Assume that 

| Relation | Number of tuples |
| -------- | ---------------- |
| $r_1$    | 1000             |
| $r_2$    | 1500             |
| $r_3$    | 750              |

And
* $|Values(C,r_1)=900|$
* $|Values(C,r_2) = 1100|$
* $|Values(E,r_2) = 50|$
* $|Values(E,r_3) = 100|$


1. What is the estimate size of $r_1 \bowtie r_2$
We know that $Max(C_{r_1}, C_{r_2})=1100$ from the given values, then the total must be
$\frac{|r_1| \times |r_2|}{Max(C_{r_1},C_{r_2})}=1364$

2. What is the estimate size of $r_1 \bowtie r_3$
$r_1$ and $r_3$ have no items in common so the total would be $|r_1| \times |r_3| = 750000$

3. What is the estimate size of $r_2 \bowtie r_3$
We know that $Max(E_{r_2}, E_{r_3})=100$ from the given values, then the total must be
$\frac{|r_2| \times |r_3|}{Max(E_{r_2},E_{r_3})}=11250$

4. Estimate the size of $r_1 \bowtie r_2  \bowtie r_3$ and give an efficient strategy for computing the join
Since we know $|r_1| \bowtie |r_2| < |r_1| \bowtie |r_3|$ we would first join $r_1$ with $r_2$ and then join the result with $r_3$ since joining the smaller ones first gives the smallest total result. giving us a total of 

$\frac{|1364| \times |r_3|}{Max(E_{r_{1,2}},E_{r_3})}= 10227$






5. What would change if instead we say that C is primary key in $r_1$





# Exercise 4
