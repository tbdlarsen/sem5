

##### 1.1 Review
Explanation of the following terms
###### relation
A relation, (or table) represents a  set of [[#tuple]]s each of which maps a set of [[#attribute]]s to values from their respective [[#domain]]s.
###### tuple
An entry (row) of values within a [[#relation]]. Tuples are represented as a set, meaning that they are unordered and unique. 
###### attribute
A category (column) in a [[#relation]]. 
###### domain
The set of possible values for a given [[#attribute]]. Each domain also has the _null_ value. 
###### schema
A template of a [[#relation]] stating the different [[#attribute]]s. 
Given attributes `A1,A2,A3, R = (A1,A2,A3)` is a relational schema
###### instance
An instance is a snapshot of a relational schema at a given instant in time, i.e. it is the table with the tuples at a given time.
An instance r over the relational [[#schema]] R is denoted by `r(R)` 
###### primary key
One [[#candidate key]] is chosen as the primary key, on the basis that the value of the key never, or very rarely changes.
###### foreign key
An attribute that refers to a [[#candidate key]] of another [[#relation]].
###### candidate key
The smallest possible [[#super key]] such that the [[#super key]] property still holds, and no proper subset of the key is no longer a [[#super key]].
###### super key
A super key is a set of one or more [[#attribute]]s of a relation such that the values of these are sufficient to uniquely identify each [[#tuple]] in the relation. This property must hold for all possible [[#instance]]s of the [[#relation]]. super keys may contain attributes that do not contribute to uniquely identifying the [[#tuple]].