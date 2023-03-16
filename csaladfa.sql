DROP TABLE IF EXISTS person;
CREATE TABLE person(person_id INTEGER PRIMARY KEY AUTOINCREMENT, lastname TEXT, firstname TEXT, gender TEXT, job TEXT, placeofbirth TEXT, born DATE, placeofdeath TEXT, died DATE, causeofdeath TEXT);

INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Kiss', 'Árpád', 'férfi', 'rendező', 'Csongrád', '1999-02-13', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Nagy', 'Zoltán', 'férfi', 'lakberendező', 'Budapest', '2003-04-16', 'Párizs', '2022-10-20', 'túladagolás');
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Joó', 'Mariann', 'nő', 'üveges', 'Eger', '1989-10-20', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Presutto', 'Ivett', 'nő', 'ingatlanos', 'Kiskunfélegyháza', '2006-07-25', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Eleben', 'Elemér', 'férfi', 'asztalos', 'Kecskemét', '1972-09-01', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Nagy', 'Pista', 'férfi', 'ács', 'Budapest', '1976-03-06', 'Budapest', '2020-11-03', 'természetes');
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Rácz', 'Dorina', 'nő', 'tanár', 'Bugac', '1974-10-24', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Kőrösi', 'Bálint', 'férfi', 'takarító', 'Miami', '2001-09-810', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Koncz', 'Zsolt', 'férfi', 'tanár', 'Oslo', '1979-11-24', 'Párizs', '1099-10-31', 'természetes');
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Topsi', 'Éva', 'nő', 'rendőr', 'Berlin', '1961-80-90', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Kása', 'Dorina', 'nő', 'orvos', 'Triszent', '1991-12-12', 'Milánó', '2016-08-10', 'természetes');
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Gaál', 'Milán', 'férfi', 'sportoló', 'Debbrecen', '1999-09-08', NULL, NULL, NULL);
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Fodor', 'László', 'férfi', 'tanuló', 'Győr', '2002-02-16', 'Győr', '2022-01-30', 'természetes');
INSERT INTO person(lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath) VALUES('Baliga', 'Tímea', 'nő', 'favágó', 'Szentes', '1974-08-19', 'Budapest', '1999-03-22', 'természetes');


DROP TABLE IF EXISTS parent;
CREATE TABLE parent(parent_id INTEGER PRIMARY KEY AUTOINCREMENT, person_id INTEGER, parent_person_id INTEGER, relationship TEXT, FOREIGN KEY (person_id) REFERENCES person(person_id), FOREIGN KEY (parent_person_id) REFERENCES person(person_id));

INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(5, 1, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(1, 2, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(1, 3, 'anya');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(5, 4, 'anya');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(2, 6, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(2, 7, 'anya');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(12, 8, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(8, 9, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(8, 10, 'anya');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(12, 11, 'anya');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(9, 13, 'apa');
INSERT INTO parent(person_id, parent_person_id, relationship) VALUES(9, 14, 'anya');


DROP TABLE IF EXISTS marriage;
CREATE TABLE marriage(marriage_id INTEGER PRIMARY KEY AUTOINCREMENT, datee DATE, place TEXT);

INSERT INTO marriage(datee, place) VALUES(2021-01-03, 'Budapest');
INSERT INTO marriage(datee, place) VALUES(2018-03-13, 'Csongrád');
INSERT INTO marriage(datee, place) VALUES(2000-04-14, 'Saint-Germain');
INSERT INTO marriage(datee, place) VALUES(2018-08-19, 'Szentes');
INSERT INTO marriage(datee, place) VALUES(2020-03-30, 'Sopron');
INSERT INTO marriage(datee, place) VALUES(2013-12-03, 'Tokyo');

DROP TABLE IF EXISTS marriagePerson;
CREATE TABLE marriagePerson(marriagePerson_id INTEGER PRIMARY KEY AUTOINCREMENT, marriage_id INTEGER, person_id INTEGER, FOREIGN KEY (marriage_id) REFERENCES marriage(marriage_id), FOREIGN KEY (person_id) REFERENCES person(person_id));

INSERT INTO marriagePerson(marriage_id, person_id) VALUES(1, 2);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(1, 3);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(2, 1);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(2, 4);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(3, 6);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(3, 7);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(8, 9);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(8, 10);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(9, 8);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(9, 11);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(10, 13);
INSERT INTO marriagePerson(marriage_id, person_id) VALUES(10, 14);


