
###### Structure
The definition of the database's [[#Relation]] and their concerns.
###### Integrity
The rules that ensures the database's contents satisfy application constraints.
###### Manipulation 
The interface and methods for accessing and modifying a database's contents. 


###### Relation
An unordered set that contains the relationships of attributes that represents entities. Usually represented through a table. Each attribute of the table is represented by the columns, The set of attributes (tuple) are the rows, sometimes called a record. The amount of rows are called the cardinality and the amount of attributes (columns) is called the arity. An N-ary relation is a relation with N attributes, a table with N columns. 
![[Relational table.png]]
Values are atomic/scalar, but can be NULL if no data, if defined so. 


###### Primary key
The primary key is a key that uniquely identifies a tuple (row). Multiple attributes can compose a primary key, i.e. a primary key can be id, name. By definition no tuples can have the same value for the primary key attribute(s). Often for practical purposes primary keys are auto-generated unique integers, known as **surrogate keys**. 

###### Foreign key
A foreign key is a relation attribute that references the key of another [[#Relation]]. For example, the course registration  [[#Relation]] may have an attribute that references a student name, that is the [[#Primary key]] from the student [[#Relation]]. 

###### Schema of a database
The schema of a database in the relational model is defined by the set of its [[#Relation]] definitions, including attributes, keys, and [[#Foreign key|foreign keys]]. 