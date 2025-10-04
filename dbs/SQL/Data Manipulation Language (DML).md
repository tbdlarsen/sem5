
###### Insert 
the INSERT keyword is used when we want to insert a tuple into a [[Relational Model Core concepts#Relation|relation]], (an entry into a table).
```SQL
CREATE TABLE student(
	id integer PRIMARY KEY,
	name varchar(20) NOT NULL,
	semester integer DEFAULT 1;
);

INSERT INTO student VALUES 
	(1000, 'John', 1);
```
Note, we cannot insert two tuples with the same primary key, because of the UNIQUE constraint, so if we try to do so the query will fail. 


###### Delete
the DELETE keyword is used when we want to delete something from a [[Relational Model Core concepts#Relation|relation]].
```SQL
DELETE FROM student;
```
This will delete all entries in the student table. 

```SQL
DELETE FROM student
WHERE semester > 2;
```
This will delete all entries where the semester is larger than 2. 
