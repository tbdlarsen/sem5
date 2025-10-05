INSERT INTO student (first_name, last_name, is_senior) VALUES
('Helle', 'Hansen', FALSE),
('Helle', 'Jensen', FALSE),
('Mads', 'Larsen', TRUE),
('Anna', 'Hansen', FALSE),
('Peter', 'Nielsen', TRUE),
('Jonas', 'Olsen', FALSE),
('Sofie', 'Peterson', FALSE),
('Carlo', 'Hansen', TRUE),
('Maria', 'Berg', FALSE),
('Frederik', 'Jensen', TRUE);

INSERT INTO tutor (first_name, last_name, is_senior) VALUES
('Lise', 'Hansen', TRUE),
('Mark', 'Nielsen', FALSE),
('Clara', 'Olsen', TRUE),
('Jonas', 'Peterson', FALSE);

INSERT INTO study_group (tid, weekday, room, starttime) VALUES
((SELECT tid FROM tutor WHERE first_name='Lise' AND last_name='Hansen'), 'Monday', 'Room 101', '09:00'),
((SELECT tid FROM tutor WHERE first_name='Clara' AND last_name='Olsen'), 'Wednesday', 'Room 102', '13:00'),
((SELECT tid FROM tutor WHERE first_name='Lise' AND last_name='Hansen'), 'Friday', 'Room 101', '10:00'),
((SELECT tid FROM tutor WHERE first_name='Mark' AND last_name='Nielsen'), 'Thursday', 'Room 103', '11:00');

INSERT INTO member (sid, gid) VALUES
((SELECT sid FROM student WHERE first_name='Helle' AND last_name='Hansen' LIMIT 1), (SELECT gid FROM study_group WHERE weekday='Monday' LIMIT 1)),
((SELECT sid FROM student WHERE first_name='Mads' AND last_name='Larsen' LIMIT 1), (SELECT gid FROM study_group WHERE weekday='Wednesday' LIMIT 1)),
((SELECT sid FROM student WHERE first_name='Carlo' AND last_name='Hansen' LIMIT 1), (SELECT gid FROM study_group WHERE weekday='Friday' LIMIT 1));



