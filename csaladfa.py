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

print("Személy keresése:")


vezeteknev = ''
keresztnev = ''

while True:
    vezeteknev = input("\t ├─ Vezetéknév: ")

    if vezeteknev:
        break

while True:
    keresztnev = input("\t └─ Keresztnév: ")

    if keresztnev:
        break
    

print(f"\n{vezeteknev} {keresztnev}")


import sqlite3 as sqlite
con = sqlite.connect('csaladfa.db')


person = []
with con:
  cur = con.cursor()
  cur.execute('SELECT * FROM person')
  for p in cur.fetchall():
    id, lastname, firstname, gender, job, born, died = p
    person.append({ 'id' : id, 'lastname' : lastname, 'firstname' : firstname, 'gender' : gender, 'job' : job, 'born' : born, 'died': died})
print(person)


parent = []
with con:
  cur = con.cursor()
  cur.execute('SELECT * FROM parent')
  for par in cur.fetchall():
    parent_id, person_id, parent_person_id, relationship = par
    parent.append({'parent_id' : parent_id, 'person_id' : person_id, 'parent_person_id' : parent_person_id, 'relationship' : relationship})
print(parent)

""""
#Név bekérése:
csaladn = input("Családnevét: ")
keresztn = input("Keresztnevét: ")
print("-----------------------------------------------------")
print(f"{csaladn} {keresztn} - adatlapja:")


#faj és egyébb adatok keresése:
sorszam=0
for i in range(len(szemelyek)):
  if csaladn == szemelyek[i]['csaladnev'] and keresztn == szemelyek[i]['keresztnev']:
    print(f"  |--> születés helye-ideje: {szemelyek[i]['szuletes']} - {szemelyek[i]['szulhey']}")
    print(f"  |--> foglalkozás: {szemelyek[i]['foglalkozas']} ")
    sorszam = szemelyek[i]['id']

neme = ""
for i in range(len(hazassagok)):
  if sorszam == hazassagok[i]['fej']:
    neme = "ferfi"
  if sorszam == hazassagok[i]['feleseg']:
    neme = "no"


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
"""

