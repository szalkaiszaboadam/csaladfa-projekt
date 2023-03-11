DROP TABLE IF EXISTS students;
CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, class TEXT);

INSERT INTO students(name, age, class) VALUES('Kiss Árpád', 15, '10b');
INSERT INTO students(name, age, class) VALUES('Nagy Zoltán', 16, '10b');
INSERT INTO students(name, age, class) VALUES('Joó Mariann', 14, '90');
INSERT INTO students(name, age, class) VALUES('Eleben Elemér', 14, '9b');