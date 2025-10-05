SELECT DISTINCT last_name FROM student AS s
WHERE s.first_name = 'Helle';


SELECT DISTINCT last_name FROM student AS s
WHERE s.last_name LIKE '%sen';

SELECT first_name, last_name, is_senior FROM tutor as t
WHERE t.is_senior = TRUE;

SELECT first_name,last_name FROM student AS s
JOIN member AS m ON m.sid = s.sid
JOIN study_group AS sg on sg.gid = m.gid
WHERE sg.weekday IN ('Wednesday','Friday');


