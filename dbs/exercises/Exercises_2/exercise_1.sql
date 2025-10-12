

CREATE TABLE student(
    sid integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    firstname varchar(20),
    lastname varchar(20),
    semester integer,
    birthdate date
);

CREATE TABLE tutor(
    tid integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    firstname varchar(20),
    lastname varchar(20),
    is_senior boolean
);

CREATE TABLE studygroup(
    gid integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tid REFERENCES tutor(tid),
    weekday varchar(10),
    room varchar(20),
    starttime time
);

CREATE TABLE exercisesheet(
    eid integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    maxpoints integer
);

CREATE TABLE handsin(
    sid REFERENCES student(sid),
    eid REFERENCES exercisesheet(eid),
    achievedpoints integer,
    PRIMARY KEY (sid, gid) 
);

CREATE TABLE member(
    sid REFERENCES student(sid),
    gid REFERENCES study_group(gid),
    PRIMARY KEY (sid, gid)
);



-- exercise 1 
SELECT S.sid, S.lastname
FROM student S 
    JOIN member M ON s.sid = m.sid
    JOIN study_group SG ON SG.gid = m.gid
GROUP BY S.sid, S.lastname
HAVING (COUNT(DISTINCT SG.weekday)>2);

-- exercise 2
SELECT T.tid
FROM tutor T
    JOIN studygroup SG ON T.tid = SG.tid
WHERE COUNT(DISTINCT SG.tid)
-- TBC