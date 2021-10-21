from obiekty.Osoba import Osoba
from typing import List
from obiekty.Harmonogram import Harmonogram
from Przedmiot import Przedmiot
from Uczen import Uczen

class Nauczyciel(Osoba):
    """Klasa, przechowujaca dane nauczyciela i jego grafik."""
    uczniowie: List[Osoba]
    tytul: str
    stawkaGodzinowa: float
    harmonogram: Harmonogram
    def __init__(self):
        self.harmonogram = Harmonogram()
    # zasugerowac sie uczniem, harmonogram on tworzy w unicie

    def dodajUcznia(self, osoba : Osoba):
        """Dodaje ucznia do nauczciela"""
        self.osoba[osoba]=osoba
    def usunUcznia(self, uczen : Uczen)->None:
        """Usuwa ucznia od nauczyciela"""
        self.uczniowie.pop()
    def dodajZajecia(self, przedmiot : Przedmiot)-> None:
        """Dodaje zajecia do grafiku nauczyciela"""

    def usunZajecia(self, przedmiot : Przedmiot)->None:
        """usuwa zajecia z harmonogramu"""
        self.remove(przedmiot)
    def najblizszeZajecia(self,przedmiot : Przedmiot)->None:
        """Zwraca informację o najbliższych zajęciach w formie daty i godziny od do."""
        pass

    def harmonogram(self, harmonogram : Harmonogram) -> None:
        """Podaje caly grafik z podziałem na dni."""
        pass

    def wolneGodziny(self, dlugosc: int = 0 ):
        """POdaje wszystkie wolne terminy o dlugosci podanej do funkcji."""
        if dlugosc>0:
            pass
        else:
            pass

    def __str__(self):
        """Zwraca dane o nauczycielu """
        pass
