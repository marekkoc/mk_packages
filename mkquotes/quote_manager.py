"""
Created: 2025.03.14
Modified: 2025.03.22
Author: MK
"""

from .quote import Quote
from .quote_file_paths import FilePaths
from .json_loader import JsonLoader
from .json_saver import JsonSaver

class QuoteManager:
    """
    Klasa zarządzająca mottami.

    Zawiera listę mott, metadane, liczbę autorów i liczbę mott.
    """
    def __init__(self) -> None:
        self.json_loader: JsonLoader | None = None
        self.json_saver: JsonSaver | None = None
        self.quotes: list[Quote] = []
        self.meta_data: dict = {}
        self.number_of_autors = 0
        self.number_of_quotes = 0
        self.autors: list[str] = []
        self.autor_quote_count: dict[str, int] = {}
        self.autor_quote_list: dict[str, list[str]] = {}
        self.quotes_by_id: dict[int, Quote] = {}

    def set_json_loader(self, json_loader: JsonLoader) -> None:
        self.json_loader = json_loader
        self.quotes = self.json_loader.get_quotes()
        self.meta_data = self.json_loader.get_meta_data()    
        self.number_of_autors = self.json_loader.get_number_of_autors()
        self.number_of_quotes = self.json_loader.get_number_of_quotes()
        self.autor_quote_count = self._count_quotes_for_autor()    
        self.autor_quote_list = self._count_autor_with_quotes()
        self.autors = list(self.autor_quote_count.keys())
        self.quotes_by_id = {quote.id: quote for quote in self.quotes}
    
    def _count_quotes_for_autor(self) -> dict[str, int]:
        """
        Tworzy słownik, w którym kluczem jest autor, a wartością liczba mott autora.
        """
        autor_quote_count: dict[str, int] = {}
        for quote in self.quotes:
            if quote.autor not in autor_quote_count:
                autor_quote_count[quote.autor] = 1
            else:
                autor_quote_count[quote.autor] += 1
        return autor_quote_count

    def _count_autor_with_quotes(self) -> dict[str, list[str]]:
        """
        Tworzy słownik, w którym kluczem jest autor, a wartością lista wszystkich mott danegoautora.
        """
        dct: dict[str, list[str]] = {}
        for quote in self.quotes:
            if quote.autor not in dct:
                dct[quote.autor] = [quote.tekst]
            else:
                if quote.tekst not in dct[quote.autor]:
                    dct[quote.autor].append(quote.tekst)               
        return dct 

    def set_json_saver(self, json_saver: JsonSaver) -> None:
        self.json_saver = json_saver  
        self.json_saver.set_meta_data(self.meta_data)
        self.json_saver.set_quotes(self.quotes)

    def save_to_json(self, test_mode: bool = False) -> None:
        if self.json_saver is None:
            raise ValueError("JsonSaver is not set")          
        self.json_saver.save_to_json(**{'test_mode': test_mode})

    def get_number_of_autors(self) -> int:
        return self.number_of_autors

    def get_number_of_quotes(self) -> int:
        return self.number_of_quotes
    
    def get_autors(self) -> list[str]:
        return self.autors
    
    def get_autor_quote_count(self) -> dict[str, int]:
        return self.autor_quote_count
    
    def get_autor_quote_list(self) -> dict[str, list[str]]:
        return self.autor_quote_list

    def __getitem__(self, quote_id: int) -> Quote:
        """
        Operator indeksowania - pozwala na dostęp do cytatów przez ich ID.
        
        Args:
            quote_id: ID cytatu
            
        Returns:
            Quote: Cytat o podanym ID
            
        Raises:
            KeyError: Gdy cytat o podanym ID nie istnieje
        """
        if quote_id not in self.quotes_by_id:
            raise KeyError(f"Cytat o ID {quote_id} nie istnieje")        
        return self.quotes_by_id[quote_id]

    def previous(self, current_id: int) -> Quote:
        """
        Pobiera poprzedni cytat przed cytatem o podanym ID.
        
        Args:
            current_id: ID aktualnego cytatu
            
        Returns:
            Quote: Poprzedni cytat w kolejności ID
            
        Raises:
            KeyError: Gdy cytat o podanym ID nie istnieje
        """
        if current_id not in self.quotes_by_id:
            raise KeyError(f"Cytat o ID {current_id} nie istnieje")
        
        # Pobierz wszystkie ID i posortuj je
        all_ids = sorted(list(self.quotes_by_id.keys()))
        
        # Znajdź indeks bieżącego ID w posortowanej liście
        current_index = all_ids.index(current_id)
        
        # Oblicz indeks poprzedniego ID (z zapętleniem)
        previous_index = (current_index - 1) % len(all_ids)
        
        # Zwróć cytat o poprzednim ID
        return self.quotes_by_id[all_ids[previous_index]]

    def next(self, current_id: int) -> Quote:
        """
        Pobiera następny cytat po cytacie o podanym ID.
        
        Args:
            current_id: ID aktualnego cytatu
            
        Returns:
            Quote: Następny cytat w kolejności ID
            
        Raises:
            KeyError: Gdy cytat o podanym ID nie istnieje
        """
        if current_id not in self.quotes_by_id:
            raise KeyError(f"Cytat o ID {current_id} nie istnieje")
        
        # Pobierz wszystkie ID i posortuj je
        all_ids = sorted(list(self.quotes_by_id.keys()))
        
        # Znajdź indeks bieżącego ID w posortowanej liście
        current_index = all_ids.index(current_id)
        
        # Oblicz indeks następnego ID (z zapętleniem)
        next_index = (current_index + 1) % len(all_ids)
        
        # Zwróć cytat o następnym ID
        return self.quotes_by_id[all_ids[next_index]]

if __name__ == "__main__":

    def main():
        print()
        for name in ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]:
            file_paths = FilePaths(name, create="json")
            json_loader = JsonLoader(file_paths)
            json_saver = JsonSaver(file_paths)

            quote_manager = QuoteManager()

            quote_manager.set_json_loader(json_loader)
            quote_manager.set_json_saver(json_saver)
            quote_manager.save_to_json()

    main()
    print()