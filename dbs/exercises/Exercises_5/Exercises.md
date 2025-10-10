
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
	   - if we create indexes for every attribute, we might as well just look for the value within that attribute. Typically we have the indexes on the search keys because that is what separates the rows from each other. 
	   1.  Is it possible in general to have two clustering indexes on the same relation for different search keys? explain your answer
	   - In general it is not possible. Because we store the tuples are stored in a different order to clump similar values together. We could have multiple keys if we just store copies of the tuples for each key. 