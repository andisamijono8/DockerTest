CREATE DATABASE students;
USE students;

CREATE TABLE student_dreams (
  name VARCHAR(20),
  dream VARCHAR(20)
);

INSERT INTO student_dreams
  (name, dream)
VALUES
  ('Bear', 'Husband'),
  ('Key', 'Wife'),
  ('Hair', "Best Programmer"),
  ('One-lined eyes', "Sun");

