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
    marriagePerson_id, marriage_id, person_id = marP
    marriagePerson.append({'marriagePerson_id' : marriagePerson_id, 'marriage_id' : marriage_id, 'person_id' : person_id})

'''print(f"\n{person}")
print(f"\n{parent}")
print(f"\n{marriage}")
print(f"\n{marriagePerson}\n")'''

print("\n Személy keresése az adatbázisunkban:")

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
  print("\n       Az általad megadott személy nem szerepel az adatbázisunkban!\n")
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

if personID > 0:
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
        print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
        #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
      else:
        print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
        #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
 


pot_parentApa = parentApa
pot_parentAnya = parentAnya
pot_marriagePersonID = marriagePersonID
pot_gyermekID = gyermekID

for i in range(len(person)):
  if personID == person[i]['person_id']:
    print(f"\n {person[i]['lastname']} {person[i]['firstname']} csaladtagjairól tovább információkért\n válassz az alábbi lehetőségek közül:")

for i in range(len(person)):
  if parentApa > 0:
    if parentApa == person[i]['person_id']:
      print(f"  └─ (1) {person[i]['lastname']} {person[i]['firstname']} életrajza")
  if parentAnya > 0:
    if parentAnya == person[i]['person_id']:
      print(f"  └─ (2) {person[i]['lastname']} {person[i]['firstname']} életrajza")
  if marriagePersonID > 0:
    if marriagePersonID == person[i]['person_id']:
      print(f"  └─ (3) {person[i]['lastname']} {person[i]['firstname']} életrajza")
  if gyermekID > 0:
    if gyermekID == person[i]['person_id']:
      print(f"  └─ (4) {person[i]['lastname']} {person[i]['firstname']} életrajza")


valasztas = 0
if personID > 0:
  while valasztas not in range(1,5):
          valasztas = int(input("\n  Melyik lehetőséget választod?: "))

if valasztas == 1:
  #pot_parentApa = 0
  if ii < len(person):
    for i in range(len(person)):
      if pot_parentApa == person[i]['person_id']:
        if person[i]['died'] == None:
          print(f"\n{person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
          print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
          print(f" │ ├─ Foglalkozása: {person[i]['job']}")
          print(f" │ └─ Neme: {person[i]['gender']}\n │")
        else:
          print(f"\n{person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
          print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
          print(f" │ ├─ Foglalkozása: {person[i]['job']} ")
          print(f" │ ├─ Neme: {person[i]['gender']} ")
          print(f" │ └─ Elhalálozás helye: {person[i]['placeofdeath']}\n │             ├─ ideje: {person[i]['died']}\n │             └─ oka: {person[i]['causeofdeath']}\n │")
        
        #pot_parentApa = person[i]['person_id']
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
    if pot_parentApa == parent[i]['person_id']:
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
    if pot_parentApa == marriagePerson[i]['person_id']:
      marriageID = marriagePerson[i]['marriage_id']


  marriagepot_parentApa = 0
  for i in range(len(marriagePerson)):
    if marriageID == marriagePerson[i]['marriage_id'] and pot_parentApa != marriagePerson[i]['person_id']:
      marriagepot_parentApa = marriagePerson[i]['person_id']
      for j in range(len(person)):
        if marriagepot_parentApa == person[j]['person_id']:
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
    if pot_parentApa == parent[i]['parent_person_id']:
      gyermekID = parent[i]['person_id']

  if gyermekID > 0:
    for i in range(len(person)):
      if person[i]['person_id'] == gyermekID:
        if person[i]['died'] == None:
          print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
          #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
        else:
          print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
          #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")

if valasztas == 2:
#pot_parentAnya = 0
  if ii < len(person):
    for i in range(len(person)):
      if pot_parentAnya == person[i]['person_id']:
        if person[i]['died'] == None:
          print(f"\n{person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
          print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
          print(f" │ ├─ Foglalkozása: {person[i]['job']}")
          print(f" │ └─ Neme: {person[i]['gender']}\n │")
        else:
          print(f"\n{person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
          print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
          print(f" │ ├─ Foglalkozása: {person[i]['job']} ")
          print(f" │ ├─ Neme: {person[i]['gender']} ")
          print(f" │ └─ Elhalálozás helye: {person[i]['placeofdeath']}\n │             ├─ ideje: {person[i]['died']}\n │             └─ oka: {person[i]['causeofdeath']}\n │")
        
        #pot_parentAnya = person[i]['person_id']
  else:
    print("       Az általad megadott személy nem szerepel az adatbázisunkban!")


  parentApa = 0
  parentAnya = 0
  for i in range(len(parent)):
    if pot_parentAnya == parent[i]['person_id']:
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
    if pot_parentAnya == marriagePerson[i]['person_id']:
      marriageID = marriagePerson[i]['marriage_id']


  marriagepot_parentAnya = 0
  for i in range(len(marriagePerson)):
    if marriageID == marriagePerson[i]['marriage_id'] and pot_parentAnya != marriagePerson[i]['person_id']:
      marriagepot_parentAnya = marriagePerson[i]['person_id']
      for j in range(len(person)):
        if marriagepot_parentAnya == person[j]['person_id']:
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
    if pot_parentAnya == parent[i]['parent_person_id']:
      gyermekID = parent[i]['person_id']

  if gyermekID > 0:
    for i in range(len(person)):
      if person[i]['person_id'] == gyermekID:
        if person[i]['died'] == None:
          print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
          #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
        else:
          print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
          #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")

if valasztas == 3:
  #pot_marriagePersonID = 0
  if ii < len(person):
    for i in range(len(person)):
      if pot_marriagePersonID == person[i]['person_id']:
        if person[i]['died'] == None:
          print(f"\n{person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
          print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
          print(f" │ ├─ Foglalkozása: {person[i]['job']}")
          print(f" │ └─ Neme: {person[i]['gender']}\n │")
        else:
          print(f"\n{person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
          print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
          print(f" │ ├─ Foglalkozása: {person[i]['job']} ")
          print(f" │ ├─ Neme: {person[i]['gender']} ")
          print(f" │ └─ Elhalálozás helye: {person[i]['placeofdeath']}\n │             ├─ ideje: {person[i]['died']}\n │             └─ oka: {person[i]['causeofdeath']}\n │")
        
        #pot_marriagePersonID = person[i]['person_id']
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
    if pot_marriagePersonID == parent[i]['person_id']:
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
    if pot_marriagePersonID == marriagePerson[i]['person_id']:
      marriageID = marriagePerson[i]['marriage_id']


  marriagepot_marriagePersonID = 0
  for i in range(len(marriagePerson)):
    if marriageID == marriagePerson[i]['marriage_id'] and pot_marriagePersonID != marriagePerson[i]['person_id']:
      marriagepot_marriagePersonID = marriagePerson[i]['person_id']
      for j in range(len(person)):
        if marriagepot_marriagePersonID == person[j]['person_id']:
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
    if pot_marriagePersonID == parent[i]['parent_person_id']:
      gyermekID = parent[i]['person_id']

  if gyermekID > 0:
    for i in range(len(person)):
      if person[i]['person_id'] == gyermekID:
        if person[i]['died'] == None:
          print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
          #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
        else:
          print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
          #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")

if valasztas == 4:
#pot_gyermekID = 0
  if ii < len(person):
    for i in range(len(person)):
      if pot_gyermekID == person[i]['person_id']:
        if person[i]['died'] == None:
          print(f"\n{person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
          print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
          print(f" │ ├─ Foglalkozása: {person[i]['job']}")
          print(f" │ └─ Neme: {person[i]['gender']}\n │")
        else:
          print(f"\n{person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
          print(f" │ ├─ Születés helye: {person[i]['placeofbirth']}\n │ │        └─ ideje: {person[i]['born']}")
          print(f" │ ├─ Foglalkozása: {person[i]['job']} ")
          print(f" │ ├─ Neme: {person[i]['gender']} ")
          print(f" │ └─ Elhalálozás helye: {person[i]['placeofdeath']}\n │             ├─ ideje: {person[i]['died']}\n │             └─ oka: {person[i]['causeofdeath']}\n │")
        
        #pot_gyermekID = person[i]['person_id']
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
    if pot_gyermekID == parent[i]['person_id']:
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
    if pot_gyermekID == marriagePerson[i]['person_id']:
      marriageID = marriagePerson[i]['marriage_id']


  marriagepot_gyermekID = 0
  for i in range(len(marriagePerson)):
    if marriageID == marriagePerson[i]['marriage_id'] and pot_gyermekID != marriagePerson[i]['person_id']:
      marriagepot_gyermekID = marriagePerson[i]['person_id']
      for j in range(len(person)):
        if marriagepot_gyermekID == person[j]['person_id']:
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
    if pot_gyermekID == parent[i]['parent_person_id']:
      gyermekID = parent[i]['person_id']

  if gyermekID > 0:
    for i in range(len(person)):
      if person[i]['person_id'] == gyermekID:
        if person[i]['died'] == None:
          print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - )")
          #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")
        else:
          print(f" │\n └─ Gyermeke: {person[i]['lastname']} {person[i]['firstname']} ({person[i]['born'][:4]} - {person[i]['died'][:4]})")
          #print(f" │\t\t└─ Születés helye: {person[i]['placeofbirth']}\n │\t\t          └─ ideje: {person[i]['born']}")





