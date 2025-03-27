"""
Created: 2025.03.18
Modified: 2025.03.18
Author: MK
"""

from .quote import Quote

class QuoteBook(Quote):
    """
    Klasa reprezentująca cytat z książki.

    Zawiera tekst, autora, id oraz liczbę obiektów.
    Wszystkie cytaty z tej samej książki mają wspólnego autora, tytuł i rok.
    """
    # Zmienne klasowe wspólne dla wszystkich cytatów z tej samej książki
    autor_ksiazki = ""
    tytul = ""
    rok = 0
    liczba_obiektow = 0
    
    def __init__(self, tekst: str, strona: int=0) -> None:
        # Wywołanie konstruktora klasy nadrzędnej z autorem książki
        super().__init__(tekst, QuoteBook.autor_ksiazki)
        QuoteBook.liczba_obiektow += 1
        self.id = QuoteBook.liczba_obiektow
        self.strona = strona

    @classmethod
    def ustaw_dane_ksiazki(cls, autor: str, tytul: str, rok: int) -> None:
        """
        Ustawia dane książki dla wszystkich cytatów.
        """
        cls.autor_ksiazki = autor
        cls.tytul = tytul
        cls.rok = rok
    
    def __str__(self) -> str:
        """
        Zwraca tekstową reprezentację pojedynczego cytatu z książki.
        """
        return f"{self.tekst} /{QuoteBook.autor_ksiazki}/ (z książki \"{QuoteBook.tytul}, str.:{self.strona}\", {QuoteBook.rok})"    
   
    def __repr__(self) -> str:
        """
        Aby wyswetlic wymusic wywoalnie __str__ podczas wyswitalnia listy mott.
        """
        return self.__str__()
    
    def print_with_id(self) -> str:
        """
        Zwraca tekstową reprezentację pojedynczego cytatu.
        """
        return f"{self.id}) ** {self.tekst} **  -  {QuoteBook.autor_ksiazki}"

    def to_dict(self) -> dict:
        """
        Konwertuje obiekt QuoteBook na słownik.
        """
        return {
            "tekst": self.tekst, 
            "autor": QuoteBook.autor_ksiazki, 
            "tytul": QuoteBook.tytul, 
            "rok": QuoteBook.rok
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'QuoteBook':
        """
        Tworzy obiekt QuoteBook z słownika.
        """
        # Zakładamy, że dane książki są już ustawione
        return cls(data["tekst"])
    
    def __del__(self) -> None:
        """
        Destruktor obiektu - zmniejsza licznik obiektów przy usunięciu.
        """
        QuoteBook.liczba_obiektow -= 1
    
    @classmethod
    def get_liczba_obiektow(cls) -> int:
        """
        Zwraca aktualną liczbę istniejących obiektów klasy Quote.
        """
        return cls.liczba_obiektow
    
    def __eq__(self, other: object) -> bool:
        """
        Porównuje dwa obiekty Quote.
        Zwraca True, jeśli tekst i autor są identyczne.
        """
        if not isinstance(other, Quote):
            return False
        return self.tekst == other.tekst and self.autor == other.autor
    
    def __lt__(self, other: 'Quote') -> bool:
        """
        Operator mniejszości (<).
        Porównuje dwa obiekty Quote na podstawie tekstu, a następnie autora.
        """
        if not isinstance(other, Quote):
            raise TypeError("Porównanie możliwe tylko z innym obiektem Quote")
        if self.tekst != other.tekst:
            return self.tekst < other.tekst
        return self.autor < other.autor
    
    def __gt__(self, other: 'Quote') -> bool:
        """
        Operator większości (>).
        Porównuje dwa obiekty Quote na podstawie tekstu, a następnie autora.
        """
        if not isinstance(other, Quote):
            raise TypeError("Porównanie możliwe tylko z innym obiektem Quote")
        if self.tekst != other.tekst:
            return self.tekst > other.tekst
        return self.autor > other.autor
    
    def __hash__(self) -> int:
        """
        Implementacja funkcji hash dla obiektu Quote.
        Umożliwia używanie obiektów Quote jako kluczy w słownikach i elementów zbiorów.
        """
        return hash((self.tekst, self.autor))


if __name__ == "__main__":
    quote: Quote  = Quote("Dupa lampa", "Violka")
    print(quote.print_with_id())
    print(f"Liczba obiektów: {quote.get_liczba_obiektow()}")
   

    
