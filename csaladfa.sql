DROP TABLE IF EXISTS person;
CREATE TABLE person(person_id INTEGER PRIMARY KEY AUTOINCREMENT, lastname TEXT, firstname TEXT, gender TEXT, job TEXT, placeofbirth TEXT, born DATE, placeofdeath TEXT, died DATE, causeofdeath TEXT);

INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Kiss', 'Árpád', 'férfi', 'rendező', 'Csongrád', '1999-02-13', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Nagy', 'Zoltán', 'férfi', 'lakberendező', 'Budapest', '2003-04-16', 'Párizs', '2022-10-20', 'túladagolás');
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Joó', 'Mariann', 'nő', 'üveges', 'Eger', '1989-10-20', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Eleben', 'Elemér', 'férfi', 'asztalos', 'Kecskemét', '1972-09-01', NULL, NULL, NULL);

DROP TABLE IF EXISTS parent;
CREATE TABLE parent(parent_id INTEGER PRIMARY KEY AUTOINCREMENT, person_id INTEGER, parent_person_id INTEGER, relationship TEXT, FOREIGN KEY (person_id) REFERENCES person(person_id), FOREIGN KEY (parent_person_id) REFERENCES person(person_id));

INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(4, 4, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(1, 3, 'anya');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(1, 2, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(4, 1, 'anya');

DROP TABLE IF EXISTS marriage;
CREATE TABLE marriage(marriage_id INTEGER PRIMARY KEY AUTOINCREMENT, datee DATE, place TEXT);

INSERT INTO marriage(datee, place) VALUES(2021-01-03, 'Budapest');
INSERT INTO marriage(datee, place) VALUES(2018-03-13, 'Csongrád');
INSERT INTO marriage(datee, place) VALUES(2016-10-23, 'Kecskemét');
INSERT INTO marriage(datee, place) VALUES(2022-02-22, 'Kiskunfélegyháza');


DROP TABLE IF EXISTS marriagePerson;
CREATE TABLE marriagePerson(marriagePerson_id INTEGER PRIMARY KEY AUTOINCREMENT, marriage_id INTEGER, person_id INTEGER, FOREIGN KEY (marriage_id) REFERENCES marriage(marriage_id), FOREIGN KEY (person_id) REFERENCES person(person_id));

INSERT INTO marriagePerson(marriage_id, person_id) VALUES(2, 1);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(2, 3);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(4, 4);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(4, 4);

