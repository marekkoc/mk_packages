"""
Klasa reprezentująca pojedynczy cytat. Klasa bazowa dla innych klas cytatów. 

Klasa zawiera tekst, autora, id oraz liczbę obiektów.

Created: 2025.03.06
Modified: 2025.03.22
Author: MK
"""

class Quote:
    """
    Klasa reprezentująca pojedynczy cytat.

    Zawiera tekst, autora, id oraz liczbę obiektów.
    """

    def __init__(self, tekst: str, autor: str, id: int | None = None) -> None:
        self.tekst: str = tekst
        self.autor: str = autor

        # to jest nick klasy, do zapisu w pliku JSON jako "id"
        #self.id = id if id is not None else Quote.ostatnie_id
        self.id = id
        
    def __str__(self) -> str:
        """
        Zwraca tekstową reprezentację pojedynczego cytatu.
        """
        return f"{self.tekst} /{self.autor}/"    
   
    def __repr__(self) -> str:
        """
        Aby wyswetlic wymusic wywoalnie __str__ podczas wyswitalnia listy mott.
        """
        return self.__str__()
    
    def print_with_id(self) -> str:
        """
        Zwraca tekstową reprezentację pojedynczego cytatu.
        """
        return f"({self.id}) {self.tekst} ({self.autor})"

    def to_dict(self) -> dict:
        """
        Konwertuje obiekt Cytat na słownik.
        """
        return {"tekst": self.tekst, "autor": self.autor, "id": self.id}

    @classmethod
    def from_dict(cls, data: dict) -> 'Quote':
        """
        Tworzy obiekt Quote z słownika.
        """
        return cls(data["tekst"], data["autor"])
       
    
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
    
   

    
