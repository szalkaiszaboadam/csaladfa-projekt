import os
import sys

import sqlite3 as sqlite
con = sqlite.connect('csaladfa.db')


person = []
with con:
  cur = con.cursor()
  cur.execute('SELECT * FROM person')
  for p in cur.fetchall():
    person_id, lastname, firstname, gender, job, placeofbirth, born, placeofdeath, died, causeofdeath = p
    person.append({ 'person_id' : person_id, 'lastname' : lastname, 'firstname' : firstname, 'gender' : gender, 'job' : job, 'placeofbirth' : placeofbirth, 'born' : born, 'placeofdeath' : placeofdeath, 'died': died, 'causeofdeath': causeofdeath})


parent = []
with con:
  cur = con.cursor()
  cur.execute('SELECT * FROM parent')
  for par in cur.fetchall():
    parent_id, person_id, parent_person_id, relationship = par
    parent.append({'parent_id' : parent_id, 'person_id' : person_id, 'parent_person_id' : parent_person_id, 'relationship' : relationship})

marriage = []
with con:
  cur = con.cursor()
  cur.execute('SELECT * FROM marriage')
  for mar in cur.fetchall():
    marriage_id, datee, place = mar
    marriage.append({'marriage_id' : marriage_id, 'datee' : datee, 'place' : place})

marriagePerson = []
with con:
  cur = con.cursor()
  cur.execute('SELECT * FROM marriagePerson')
  for marP in cur.fetchall():
    marriagePerson_id, marriage_id, person_id, relationship = marP
    marriagePerson.append({'marriagePerson_id' : marriagePerson_id, 'marriage_id' : marriage_id, 'person_id' : person_id, 'relationship' : relationship})

'''print(f"\n{person}")
print(f"\n{parent}")
print(f"\n{marriage}")
print(f"\n{marriagePerson}\n")'''

print("Személy keresése:")

csaladn = ''
keresztn = ''

while True:
    csaladn = input("   ├─ Vezetéknév: ")
    if csaladn:
        break

while True:
    keresztn = input("   └─ Keresztnév: ")
    if keresztn:
        break
    
ii = 0
while ii < len(person) and (csaladn != person[ii]['lastname'] or keresztn != person[ii]['firstname']):
  ii += 1

'''for i in range(len(person)):
      if csaladn != person[i]['lastname'] or keresztn != person[i]['firstname']:
        letezik += 1'''

personID = 0
if ii < len(person):
  for i in range(len(person)):
    if csaladn == person[i]['lastname'] and keresztn == person[i]['firstname']:
      if person[i]['died'] == None:
        print(f"\n{csaladn} {keresztn} ({person[i]['born'][:4]} - )")
        print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
        print(f" │ ├─ Foglalkozása: {person[i]['job']}")
        print(f" │ └─ Neme: {person[i]['gender']}\n │")
      else:
        print(f"\n{csaladn} {keresztn} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
        print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
        print(f" │ ├─ Foglalkozása: {person[i]['job']} ")
        print(f" │ ├─ Neme: {person[i]['gender']} ")
        print(f" │ └─ Elhalálozás helye: {person[i]['placeofdeath']}\n │             ├─ ideje: {person[i]['died']}\n │             └─ oka: {person[i]['causeofdeath']}\n │")
      
      personID = person[i]['person_id']
else:
  print("       Az általad megadott személy nem szerepel az adatbázisunkban!")
'''while True:
    csaladn = input("   ├─ Vezetéknév: ")
    if csaladn:
      break

  while True:
    keresztn = input("   └─ Keresztnév: ")
    if keresztn:
      break'''
    



parentApa = 0
parentAnya = 0
for i in range(len(parent)):
  if personID == parent[i]['person_id']:
    if parent[i]['relationship'] == "apa":
      parentApa = parent[i]['parent_person_id']
    if parent[i]['relationship'] == "anya":
      parentAnya = parent[i]['parent_person_id']


if parentApa > 0:
  for i in range(len(person)):
    if person[i]['person_id'] == parentApa:
      if person[i]['died'] == None:
        print(f" ├─ Apja: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
        #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
      else:
        print(f" ├─ Apja: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
        #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
else:
  print(" │  Az apa nem szerepel az adatbázisban")

if parentAnya > 0:
  for i in range(len(person)):
    if person[i]['person_id'] == parentAnya:
      if person[i]['died'] == None:
        print(f" ├─ Anyja: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
        #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
      else:
        print(f" ├─ Anyja: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
        #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
else:
  print(" │  Az anya nem szerepel az adatbázisban")  
    

marriageID = 0
for i in range(len(marriagePerson)):
  if personID == marriagePerson[i]['person_id']:
    marriageID = marriagePerson[i]['marriage_id']

marriagePersonID = 0
for i in range(len(marriagePerson)):
  if marriageID == marriagePerson[i]['marriage_id'] and personID != marriagePerson[i]['person_id']:
    marriagePersonID = marriagePerson[i]['person_id']
    for j in range(len(person)):
      if marriagePersonID == person[j]['person_id']:
        if person[j]['gender'] == 'férfi':
          if person[j]['died'] == None:
            print(f" │\n ├─ Férje: {person[j]['lastname']} {person[j]['firstname']} ({person[j]['born'][:4]} - )")
          else:
             print(f" │\n ├─ Férje: {person[j]['lastname']} {person[j]['firstname']} ({person[j]['born'][:4]} - {person[j]['died'][:4]})")
        if person[j]['gender'] == 'nő':
          if person[j]['died'] == None:
            print(f" │\n ├─ Felesége: {person[j]['lastname']} {person[j]['firstname']} ({person[j]['born'][:4]} - )")
          else:
            print(f" │\n ├─ Felesége: {person[j]['lastname']} {person[j]['firstname']} ({person[j]['born'][:4]} - {person[j]['died'][:4]})")




gyermekID = 0
for i in range(len(parent)):
  if personID == parent[i]['parent_person_id']:
    gyermekID = parent[i]['person_id']

if gyermekID > 0:
  for i in range(len(person)):
    if person[i]['person_id'] == gyermekID:
      if person[i]['died'] == None:
        print(f" │\n ├─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
        #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
      else:
        print(f" │\n ├─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
        #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")

'''
#Házastárs keresése:
if neme == "ferfi":
  for i in range(len(szemelyek)):
    for j in range(len(hazassagok)):
      if sorszam == hazassagok[j]['fej'] and hazassagok[j]['feleseg'] == szemelyek[i]['id']:
        print(f"  ˙--> feleség : {szemelyek[i]['csaladnev']} {szemelyek[i]['keresztnev']}")


if neme == "no":
  for i in range(len(szemelyek)):
    for j in range(len(hazassagok)):
      if sorszam == hazassagok[j]['feleseg'] and hazassagok[j]['fej'] == szemelyek[i]['id']:
        print(f"  ˙--> férj : {szemelyek[i]['csaladnev']} {szemelyek[i]['keresztnev']}")


'''






'''print("Válassz az alábbi opciók közül:\n\t(1) Családtörténet keresése\n\t(2) Személy keresése\n")

valasztas = 0

while valasztas not in range(1,3):
        valasztas = int(input("Melyiket választod?: "))
        


if valasztas == 1:
    print("\n\n    Családtörténet keresése ---\n")

    csaladnev = ''

    while True:
        csaladnev = input(" Családnév:")

        if csaladnev:
            break

if valasztas == 2:
    print("\n\n    --- Személy keresése ---\n")


    vezeteknev = ''
    keresztnev = ''
    szuletesiHely = ''
    szuletesiEv = ''

    while True:
        vezeteknev = input(" Vezetéknév: (kötelező)")

        if vezeteknev:
            break

    keresztnev = input(" Keresztnév: (nem kötelező)")

    szuletesiHely = input(" Születési hely: (nem kötelező)")

    szuletesiEv = input(" Születési év: (nem kötelező)")
    

    if keresztnev == "":
        keresztnev = "-"
    
    if szuletesiHely == "":
        szuletesiHely = "-"
    
    if szuletesiEv == "":
        szuletesiEv = "-"

    print(vezeteknev, keresztnev, szuletesiHely, szuletesiEv)
'''