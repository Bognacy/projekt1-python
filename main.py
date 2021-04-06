import csv


# import pandas

class Pojazd:
    def __init__(self, marka, model, rok, pojemn, przebieg, skrzynia):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.pojemn = pojemn
        self.przebieg = przebieg
        self.skrzynia = skrzynia


baza = []


def dodaj(marka: str, model: str, rok: int, pojemn: int, przebieg: int, skrzynia: int):
    baza.append(Pojazd(marka, model, rok, pojemn, przebieg, skrzynia))

    dodaj("Audi", "A4", 2001, 2100, 190000, 1)

def dodaj_ui():
    print("Podaj markę:")
    mar = input()
    print("Podaj model:")
    mod = input()
    print("Podaj rocznik:")
    rocz = input()
    print("Podaj pojemnosc")
    poj = input()
    print("Podaj Przebieg:")
    prze = input()
    print("Czy posiada automatyczną szkrzynie biegów?"
          "1 - automat"
          "2 - manual ")
    sk = input()

    dodaj(mar, mod, int(rocz), int(poj), int(prze), int(sk))


def wyswietl(ktr):
    obj = baza[ktr]
    print(obj.marka, obj.model, obj.rok, obj.pojemn, obj.przebieg, obj.skrzynia, sep=' ')


def zapisz():
    with open('katalog.csv', 'w') as f:
        for obj in baza:
            write = csv.writer(f)
            write.writerow([obj.marka, obj.model, str(obj.rok), str(obj.pojemn), str(obj.przebieg), str(obj.skrzynia)])


def wczytaj():
    with open('katalog.csv', newline='') as f:
        reader = csv.reader(f)
        baza = list(reader)
        tout = []
        for tab in baza:
            s = Pojazd(tab[0], tab[1], int(tab[2]), int(tab[3]), int(tab[4]), int(tab[5]))
            tout.append(s)
            # print(tab)
        return tout


baza = wczytaj()


def wyswietl_baze():
    for i in range(len(baza)):
        print(i+1, ""  , end='')
        wyswietl(i)


def sortuj_marke(czy_malejaco):
    baza.sort(key=lambda x: x.marka , reverse=czy_malejaco)
    # sortowanko

def sortuj_model(czy_malejaco):
    baza.sort(key=lambda x: x.model, reverse=czy_malejaco)
    # sortowanko

def sortuj_rok(czy_malejaco):
    baza.sort(key=lambda x: x.rok, reverse=czy_malejaco)
    # sortowanko

def sortuj_przebieg(czy_malejaco):
    baza.sort(key=lambda x: x.przebieg, reverse=czy_malejaco)
    # sortowanko

def sortuj():
    print("Wybierz kryterium sortowania:"
          "1.Marka"
          "2.Model"
          "3.Rocznik"
          "4.Przebieg")
    w1 = input()
    print("1. Rosnąco"
          "2. Malejąco")
    w2 = int(input()) - 1

    if w1 == 1:
        sortuj_marke(w2)
    elif w1 == 2:
        sortuj_model(w2)
    elif w1 == 3:
        sortuj_rok(w2)
    elif w1 == 4:
        sortuj_rok(w2)
    print("Gotowe!")

def filtruj_rok(rok):
    for i, obj in enumerate(baza):
        if obj.rok > rok:
            wyswietl(i)

def filtruj_pojemnosc(pojemnosc):
    for i, obj in enumerate(baza):
        if obj.pojemn > pojemnosc:
            wyswietl(i)

def filtr():
    print("Wybierz parametr filtrowania:\n"
          "1. Rocznik\n"
          "2. Pojemnosc\n")
    p=int(input())
    if p == 1:
        print("Podaj od którego roku najpóźniej szukać\n")
        r=int(input())
        filtruj_rok(r)
    elif p == 2:
        print("Podaj minimalna pojemnosc:\n ")
        r=int(input())
        filtruj_pojemnosc(r)


def menu():
    print("Wybierz polecenie (nr) z listy:\n"
          "1. Wczytaj katalog z pliku\n"
          "2. Zapisz katalog do pliku\n"
          "3. Dodaj pojazd\n"
          "4. Wyswietl wskazany pojazd\n"
          "5. Wyświetl wszystkie pojazdy\n"
          "6. Posortuj po wskazanym parametrze\n"
          "7. Wyświetlanie warunkowe:\n"
          "8. Usuń wskazany pojazd\n")
    w = int(input())
    if w == 1:
        wczytaj()
    elif w == 2:
        zapisz()
    elif w == 3:
        dodaj_ui()
    elif w == 4:
        print("Który?")
        wyswietl(input())
    elif w == 5:
        wyswietl_baze()
    elif w == 6:
        sortuj()
    elif w == 7:
        filtr()
    elif w == 8:
        print("Który?")
        wyswietl_baze()
        baza.remove(int(input())-1)
    else:
        exit(0)

while 1:
    menu()

##wyswietl(1) musze dodać zmiane odczytywanych wrtości na jeden obiekt typu pojazd
