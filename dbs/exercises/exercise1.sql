CREATE SEQUENCE student_id START 1;

CREATE TABLE student(
   sid integer DEFAULT nextval('student_id') PRIMARY KEY,
   first_name varchar(20) NOT NULL,
   last_name varchar(20) NOT NULL,
   is_senior boolean DEFAULT FALSE

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
    tid integer NOT NULL,
    weekday varchar(20) NOT NULL,
    room varchar (20),
    starttime time,
    FOREIGN KEY(tid) REFERENCES tutor(tid)
);

CREATE SEQUENCE exercise_nr START 1;

CREATE TABLE exercise(
    
);