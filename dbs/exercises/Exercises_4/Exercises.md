

# 1.1 Review
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

# 1.2 Review Questions
Assume the following `University` schema (written in PostgreSQL see task for exact question).
```postgresql
CREATE TABLE employee(
	eid integer UNIQUE,
	ename varchar(20),
	did integer REFERENCES department(did)
);

CREATE TABLE department(
	did integer UNIQUE,
	dname varchar(20),
	location varchar(20)
);

CREATE TABLE project(
	pid integer UNIQUE,
	pname varchar(20),
	budget integer
);

CREATE TABLE works_on(
	eid integer REFERENCES employee(eid),
	pid integer REFERENCES project(pid),
	hours integer
);

```

## Part A
1. In `Employee, {eid}` is a candidate key 
	1. False, UNIQUE does not imply not null, so two employees can have NULL as a eid, i.e. we cannot uniquely identify them. 
2. In `Works_on, {eid}` alone, uniquely identifies a tuple
	1.  false, since eid is not a candidate key, eid cannot be a foreign key, and it does not satisfy the super key property.
3. In `department, {did,dname}` is a super key
	1. false, Unique does not imply not null, so we can have multiple departments where did and dname are null. 
4. A foreign key is only allowed to reference a declared primary key, never a candidate key.
	1. false, a foreign key is allowed to reference any candidate keys within a relation.
5. Attributes that form a primary key may contain NULL values.
	1. false, else we could have multiple tuples with NULL as primary keys, and thus be unable to uphold the super key property that states that we have to be able to uniquely identify tuples based on the super key.
## Part b
1. Suppose that, in the current instance of employee, no two employees share the same
   ename. From this observation, can we conclude that ename can be used as a superkey (or primary key) of employee?
	1. No, a super key has to be unique based on the relational schema, not the instance. i.e. it has to hold for all possible instances of the relation.
2. Consider department(did, dname, location). Assume that both {did} and {dname,location} can uniquely identify a tuple in this relation. Among the following sets, which are super keys and which are candidate keys?
	1. {did}
		1. superkey, and candidate key since it is minimal
	2. {dname,location}
		1. super key, and candidate key since it is minimal.
	3. {did, dname}
		1. super key, not candidate key since dname is not essential.
	4. {did, location}
		1. super key, not candidate key since location is not essential.