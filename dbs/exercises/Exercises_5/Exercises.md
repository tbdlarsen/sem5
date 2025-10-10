
1. Example of when not using tombstones will create problems

if we try to insert a value, and we  have previously deleted an element. Then if we have a hash collision and the next element is the deleted element. If we don't have a tombstone there, we just insert the value at that spot, but there could be a duplicate key in the next place that will not be checked. If there was a tombstone there we would keep on checking that cluster, then if there were no duplicates we can insert at the tombstone.
So 
```
hash(v1) = 2
hash(v2) = 2
hash(v3) = 2

PUT v1
PUT v2 (3 after probing)
PUT v3 (4 after probing)
DELETE V2
PUT v3 (3 after probing)
```
This would result in a duplicate v3 key. 


2. Indexes
	1. Indexes speed up query processing but it is usually a bad idea to create indexes on every attribute and every combination of attributes that might potentially be useful for an arbitrary query. Explain why?
	   - Storage overhead:
	     each index consumes additional disk space
	   - Maintenance cost
	     For every update the indexes has to be updated
	   - Diminishing returns
	     If we have the right indexes on primary and/or secondary keys we can make each query exhaustive
	   1.  Is it possible in general to have two clustering indexes on the same relation for different search keys? explain your answer
	   - In general it is not possible.  Clustering works by storing the tuples together based on similar values of the clustering key. Adding another key would interfere with the ordering of the first key. One workaround is to just store copies of the tuples based on the amount of keys.

3. B+-trees
	1. Construct a B+-tree for the following set of key values: (2, 3, 5, 7, 11, 17, 19, 23, 29, 31) Assume that the tree is initially empty and values are added one-by-one in ascending order. Construct B+-trees for the cases where the number of pointers that will fit in one node is as follows: 4,6, and 8
	   * order = 4
	![[4-b+-tree.png]]
	1. do the following sequence to the tree: Insert 9, Insert 10, Insert 8, Delete 23, Delete 19
	   ![[4-b+-tree-insert.png]]