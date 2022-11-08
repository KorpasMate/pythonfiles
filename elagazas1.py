#Kérjünk be egy egész számot és írjuk ki hogy páros vagy páratlan.

szam = int(input("Kérem a számot: "))

if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")