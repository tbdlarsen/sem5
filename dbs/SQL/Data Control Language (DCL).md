
###### CREATE 
The CREATE keyword is used to create a table, where you can have attributes. Example
```SQL
CREATE TABLE professor(
	id integer UNIQUE NOT NULL,
	name varchar(10) NOT NULL,
	rank char(2) DEFAULT 'C1'
);
```
###### Types
types of numbers; INT, BIGINT, SMALLINT, FLOAT
types of text; char(n) always uses n bytes, i.e. char(2) always has to have 2 characters, if there is less characters inserted it can lead to undefined behavior,
varchar(n) can have up yo n characters, so varchar(3) has a max length of 3. 

###### Constraints
* UNIQUE
	* an attribute that cannot contain multiple copies of the same value. 
* NOT NULL
	* an attribute that cannot be NULL.
* PRIMARY KEY
	* declares an attribute as the [[Relational Model Core concepts#Primary key| primary key]]. A table can only have one primary key, but it can be composite (multiple attributes). The primary key includes the UNIQUE and NOT NULL constraints. 
* DEFAULT
	* When inserting data into a table, all values that are not explicitly stated are set to NULL, except if there is a DEFAULT constraint, which sets the value if not given. 


###### Sequence number generators
sequence number generations automatically create continuous identifiers, can be used for automatic surrogate keys. Example:
```SQL
CREATE SEQUENCE studentseq START 2100;

CREATE TABLE student(
id integer PRIMARY KEY DEFAULT NEXT VALUE FOR studenseq,
name varchar(20) NOT NULL,
class char(2) DEFAULT 'C1'
);
```
(in PostgreSQL it is `DEFAULT nextval(studentseq)`) 



###### Foreign keys
Foreign keys must only reference an existing value in the relation in which it is referencing.