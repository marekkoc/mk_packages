"""
Created: 2025.03.10
Modified: 2025.03.19
Author: MK
"""

import json
import datetime
import random

from .quote import Quote
from .quote_file_paths import FilePaths
from .json_loader import JsonLoader
from .json_saver import JsonSaver
from .quote_manager import QuoteManager


class QuoteSelector(QuoteManager):
    """
    Klasa selektująca motta w pliku JSON.
    """
    def __init__(self) -> None:
        super().__init__()       


    def sort_by_autor(self) -> None:
        """
        Sortuje autory po autorze.
        """    
        self.autors.sort()
    
    def sort_by_count(self) -> None:
        """
        Sortuje autorow po liczbie mott.
        """    
        self.autors = sorted(self.autors, key=lambda x: self.autor_quote_count[x], reverse=True)

    def shuffle_autors(self) -> None:
        """
        Losowo miesza listę autorów.
        """        
        random.shuffle(self.autors)
    
    def random_autor(self) -> str:
        """
        Zwraca losowego autora.
        """
        return random.choice(self.autors)

    def random_quote(self) -> Quote:
        """
        Zwraca losowe motto.
        """
        return random.choice(self.quotes)
    
    def get_quotes(self) -> list[Quote]:
        return self.quotes
    
    def get_autor_with_quotes(self) -> dict[str, list[str]]:
        return self.autor_quote_list
    
    def get_autor_quote_count(self) -> dict[str, int]:
        return self.autor_quote_count
    
    def get_autors(self) -> list[str]:
        return self.autors

if __name__ == "__main__":

    def main():
        print()
        file_paths = FilePaths("2007_Ruiz_Cztery-umowy", create="json")

        quote_selector = QuoteSelector()

        quote_selector.set_json_loader(JsonLoader(file_paths))
        
        print(quote_selector.random_quote())
        print()
    

    main()
    




