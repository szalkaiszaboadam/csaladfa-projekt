
print("Válassz az alábbi opciók közül:\n\t (1) Családtörténet keresése\n\t(2) Személy keresése")
valasztas = ""
while True:
    valasztas = input("\n Melyiket választod?: ")

    if valasztas:
        break



csaladnev = ''



while True:
    vezeteknev = input("Családnév: (kötelező) ")

    if vezeteknev:
        break
    









vezeteknev = ''
keresztnev = ''
szuletesiHely = ''
szuletesiEv = ''







    
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