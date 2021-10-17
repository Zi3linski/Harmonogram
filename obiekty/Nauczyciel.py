from obiekty.Osoba import Osoba
from typing import List
from obiekty.Harmonogram import Harmonogram


class Nauczyciel(Osoba):
    """Klasa, przechowujaca dane nauczyciela i jego grafik."""
    uczniowie: List[Osoba]
    tytul: str
    stawkaGodzinowa: float
    harmonogram: Harmonogram
    def __init__(self):
        pass

    def najblizszeZajecia(self):
        """Zwraca informację o najbliższych zajęciach w formie daty i godziny od do."""
        pass

    def harmonogram(self):
        """Podaje caly grafik z podziałem na dni."""
        pass

    def wolneGodziny(self, dlugosc: int = 0 ):
        """POdaje wszystkie wolne terminy o dlugosci podanej do funkcji."""
        if dlugosc>0:
            pass
        else:
            pass
