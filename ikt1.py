class Vivmany:
    def __init__(self, evszam, nev, feltalalo):
        self.evszam = evszam
        self.nev = nev
        self.feltalalo = feltalalo

    def __str__(self):
        return f"{self.evszam};{self.nev};{self.feltalalo}"


def adatokat_beolvas(fajlnev):
    adatok = []
    try:
        with open(fajlnev, 'r') as file:
            for sor in file:
                evszam, nev, feltalalo = sor.strip().split(';')
                adatok.append(Vivmany(evszam, nev, feltalalo))
    except FileNotFoundError:
        print("A megadott fájl nem található.")
    except Exception as e:
        print(f"Hiba történt az adatok beolvasása során: {e}")
    return adatok


def adatokat_kiir(adatok, fajlnev):
    try:
        with open(fajlnev, 'w') as file:
            for vivmany in adatok:
                file.write(str(vivmany) + '\n')
        print(f"Az adatok ki lettek írva a(z) {fajlnev} fájlba.")
    except Exception as e:
        print(f"Hiba történt az adatok kiírása során: {e}")


def listazas(adatok):
    for vivmany in adatok:
        print(vivmany)


def idotartomanyban_listazas(adatok, kezdo_ev, vegso_ev):
    for vivmany in adatok:
        if kezdo_ev <= int(vivmany.evszam) <= vegso_ev:
            print(vivmany)


def main():
    adatfajl_nev = input("Adja meg a vívmányok adatait tartalmazó fájl nevét: ")
    vivmanysorok = adatokat_beolvas(adatfajl_nev)

    while True:
        print("\nVívmányok kezelése:")
        print("1. Minden adat listázása a képernyőre")
        print("2. Minden adat listázása egy fájlba")
        print("3. Adott időtartományban lévő vívmányok listázása")
        print("0. Kilépés")

        valasztas = input("Válasszon egy opciót (0-3): ")

        if valasztas == '1':
            listazas(vivmanysorok)
        elif valasztas == '2':
            kimeneti_fajl_nev = input("Adja meg a kimeneti fájl nevét: ")
            adatokat_kiir(vivmanysorok, kimeneti_fajl_nev)
        elif valasztas == '3':
            kezdo_ev = int(input("Adja meg a kezdő évszámot: "))
            vegso_ev = int(input("Adja meg a végső évszámot: "))
            idotartomanyban_listazas(vivmanysorok, kezdo_ev, vegso_ev)
        elif valasztas == '0':
            break
        else:
            print("Érvénytelen opció. Kérem, válasszon újra.")


if __name__ == "__main__":
    main()

