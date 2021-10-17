from obiekty.Przedmiot import Przedmiot
from obiekty.Uczen import Uczen


def main():
    p1 = Przedmiot("Polski",1,35,"Pt",12)
    p1.dodajOcene(5)
    p1.dodajOcene(4)
    print(p1)
    p1.usunOcene(4)
    print(p1)
    u1 = Uczen("Michal", "Zielinski", "78895456125", 25)
    u1.dodajPrzedmiot(p1)
    u1.dodajOcene("Polski", 5)
    u1.dodajOcene("Polski", 1)
    u1.dodajOcene("Polski", 5)
    u1.dodajOcene("Polski", 5)
    print(u1.postepy("Polski"))
    u1.dodajPrzedmiot(Przedmiot("Matematyka", 2, 35, "Wt", 2))
    print(u1)

    u1.pokazPrzedmiot("Polski")
    u1.usunPrzedmiot("Matematyka")
    u1.pokazPrzedmiot("Matematyka")


if __name__ == '__main__':
    main()


