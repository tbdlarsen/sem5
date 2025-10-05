CREATE SEQUENCE student_id START 1;

CREATE TABLE student(
   sid integer DEFAULT nextval('student_id') PRIMARY KEY,
   first_name varchar(20) NOT NULL,
   last_name varchar(20) NOT NULL,
   semester integer NOT NULL,
   birthdate date

);

CREATE SEQUENCE tutor_id START 1;

CREATE TABLE tutor(
    tid integer DEFAULT nextval('tutor_id') PRIMARY KEY,
    first_name varchar(20) NOT NULL,
    last_name varchar(20) NOT NULL,
    is_senior boolean DEFAULT TRUE
);

CREATE SEQUENCE study_group_id START 1;

CREATE TABLE study_group(
    gid integer DEFAULT nextval('study_group_id') PRIMARY KEY,
    tid integer REFERENCES tutor(tid),
    weekday varchar(20) NOT NULL,
    room varchar(20),
    starttime time
);

CREATE SEQUENCE exercise_nr START 1;

CREATE TABLE exercise(
    eid integer DEFAULT nextval('exercise_nr') PRIMARY KEY,
    maxpoints integer
);

CREATE TABLE hands_in(
    sid integer REFERENCES student(sid),
    eid integer REFERENCES exercise(eid),
    achieved_points integer,
    --FOREIGN KEY(sid) REFERENCES student(sid),
    --FOREIGN KEY(eid) REFERENCES exercise(eid),
    PRIMARY KEY(sid, eid)
);

CREATE TABLE member(
    sid integer REFERENCES student(sid),
    gid integer REFERENCES study_group(gid),
    PRIMARY KEY(sid,gid)
);