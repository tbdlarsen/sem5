
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
```SQL
CREATE TABLE professor(
id integer PRIMARY KEY,
name varchar(20) NOT NULL,
rank char(2)
);


CREATE TABLE course(
courseid integer PRIMARY KEY,
title varchar(20) NOT NULL,
ects integer,
taughtby integer,
FOREIGN KEY(taughtby) REFERENCES professor(id)
);

```
Foreign keys can also reference candidate keys enforced with UNIQUE constraints. In a [[Relational Model Core concepts#Relation| relational schema]] any attribute that makes logical sense can be used as keys. Although it is considered bad practice to use keys with text for performance reasons, use integer surrogate keys when possible.

###### Changing table definitions
After creating a table, it is possible to add/remove attributes and constraints. 
```SQL
CREATE TABLE student(
id integer PRIMARY KEY,
name varchar(20) NOT NULL,
semester integer
);
```

**Adding an attribute**
```SQL
ALTER TABLE student
	ADD COLUMN study_group integer;
```
**Deleting and attribute**
```SQL
ALTER TABLE student
	DROP COLUMN semester;
```
**Changing and attribute type**
```SQL
ALTER TABLE student
	ALTER COLUMN name type varchar(25);
```
**Add an attribute constraint**
```SQL
ALTER TABLE student
	ALTER COLUMN semester SET NOT NULL;
```


###### Deleting a table
```SQL
DROP TABLE student;
```
when using the drop keyword it deletes the content of the table but not the table itself.


```SQL
TRUNCATE TABLE student;
```
truncate cannot be used if another table has a foreign key that references the table we want to delete.  