print("Válassz az alábbi opciók közül:\n\t(1) Családtörténet keresése\n\t(2) Személy keresése\n")

valasztas = 0

while valasztas not in range(1,3):
    valasztas = int(input("\n Melyiket választod?: "))
print(valasztas)


if valasztas == 1:
    print("Családtörténet keresése")

    csaladnev = ''

    while True:
        csaladnev = input("  Családnév:")

        if csaladnev:
            break

if valasztas == 2:
    print("Személy keresése")


    vezeteknev = ''
    keresztnev = ''
    szuletesiHely = ''
    szuletesiEv = ''

    while True:
        vezeteknev = input("  Vezetéknév: (kötelező)")

        if vezeteknev:
            break

    keresztnev = input("  Keresztnév: (nem kötelező)")

    szuletesiHely = input("  Születési hely: (nem kötelező)")

    szuletesiEv = input("  Születési év: (nem kötelező)")
    

    if keresztnev == "":
        keresztnev = "-"
    
    if szuletesiHely == "":
        szuletesiHely = "-"
    
    if szuletesiEv == "":
        szuletesiEv = "-"

    print(vezeteknev, keresztnev, szuletesiHely, szuletesiEv)


    









