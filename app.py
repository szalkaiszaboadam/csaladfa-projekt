vezeteknev = ''
keresztnev = ''
szuletesiHely = ''
szuletesiEv = ''

print("\t\tCsaládfa keresése\n")

while True:
    vezeteknev = input("Vezetéknév: (kötelező) ")

    if vezeteknev:
        break
    
    
keresztnev = input("Keresztnév: ")

szuletesiHely = input("Születési hely: ")

szuletesiEv = input("Születési év: ")

if keresztnev == "":
    keresztnev = "-"
    
if szuletesiHely == "":
    szuletesiHely = "-"
    
if szuletesiEv == "":
    szuletesiEv = "-"



print(vezeteknev, keresztnev, szuletesiHely, szuletesiEv)