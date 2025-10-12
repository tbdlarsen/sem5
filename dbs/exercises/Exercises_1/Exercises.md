

Exercises 1 and 2 are in the .sql files


Exercise 3
1. The full query is 
```postgresql
SELECT SG.gid
FROM studygroup SG
EXCEPT
SELECT s.firstname
FROM student s
WHERE s.firstname IS NOT NULL;
```
2. The null is redundant since we only return the s.first_name if there is one.
3. The full query is 
```postgresql
SELECT S.firstname, S.lastname
FROM student S, member M, tutor T, study_groud SG,
WHERE T.firstname = 'Helle' AND T.tid = SG.tid
	AND S.sid = M.sid AND m.gid = SG.gid;

```
4. The full query is
```postgresql
SELECT S.sid
FROM student S, tutor T
WHERE S.birthdate < '1998-03-01'
	AND S.firstname = T.firstname
	AND T.is_Senior = False;

```
