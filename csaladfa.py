print("Válassz az alábbi opciók közül:\n\t(1) Családtörténet keresése\n\t(2) Személy keresése\n")

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