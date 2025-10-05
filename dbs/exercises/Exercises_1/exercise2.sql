SELECT DISTINCT last_name FROM student AS s
WHERE s.first_name = 'Helle';


SELECT DISTINCT last_name FROM student AS s
WHERE s.last_name LIKE '%sen';

SELECT first_name, last_name, is_senior FROM tutor as t
WHERE t.is_senior = TRUE;