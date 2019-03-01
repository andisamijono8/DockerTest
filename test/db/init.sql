CREATE DATABASE students;
USE students;

CREATE TABLE student_dreams (
  name VARCHAR(20),
  dream VARCHAR(20)
);

INSERT INTO student_dreams
  (name, dream)
VALUES
  ('Rahul', 'Husband'),
  ('Min Xue', 'Wife'),
  ('Ethan', "Best Programmer");
