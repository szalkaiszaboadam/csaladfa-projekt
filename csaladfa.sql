DROP TABLE IF EXISTS person;
CREATE TABLE person(person_id INTEGER PRIMARY KEY AUTOINCREMENT, lastname TEXT, firstname TEXT, gender TEXT, job TEXT, born DATE, died DATE);

INSERT INTO person(lastname, firstname, gender, job, born, died) VALUES('Kiss', 'Árpád', 'férfi', 1999-02-13, NULL);
INSERT INTO person(lastname, firstname, gender, job, born, died) VALUES('Nagy', 'Zoltán', 'férfi', 2003-04-16, 2022-10-20);
INSERT INTO person(lastname, firstname, gender, job, born, died) VALUES('Joó', 'Mariann', 'nő', 1989-10-20, NULL);
INSERT INTO person(lastname, firstname, gender, job, born, died) VALUES('Eleben', 'Elemér', 'férfi', 1972-09-1, nuLL);

DROP TABLE IF EXISTS parent;
CREATE TABLE parent(parent_id INTEGER PRIMARY KEY AUTOINCREMENT, person_id INTEGER FOREIGN KEY, parent_person_id INTEGER FOREIGN KEY, relationship TEXT);

INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(1, 4, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(2, 3, 'anya');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(3, 2, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(4, 1, 'anya');

DROP TABLE IF EXISTS marriage;
CREATE TABLE marriage(marriage_id INTEGER PRIMARY KEY AUTOINCREMENT, datee DATE, place TEXT);

INSERT INTO marriage(datee, place) VALUES(2021-01-03, 'Budapest');
INSERT INTO marriage(datee, place) VALUES(2018-03-13, 'Csongrád');
INSERT INTO marriage(datee, place) VALUES(2016-10-23, 'Kecskemét');
INSERT INTO marriage(datee, place) VALUES(2022-02-22, 'Kiskunfélegyháza');


DROP TABLE IF EXISTS marriagePerson;
CREATE TABLE marriagePerson(marriagePerson_id INTEGER PRIMARY KEY AUTOINCREMENT, marriage_id INTEGER FOREIGN KEY, person_id INTEGER FOREIGN KEY, relationship TEXT);

INSERT INTO marriagePerson(marriage_id, person_id, relationship) VALUES(4, 1);
INSERT INTO marriagePerson(marriage_id, person_id, relationship) VALUES(3, 2);
INSERT INTO marriagePerson(marriage_id, person_id, relationship) VALUES(2, 3);
INSERT INTO marriagePerson(marriage_id, person_id, relationship) VALUES(1, 4);

