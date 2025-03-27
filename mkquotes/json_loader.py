"""
Created: 2025.03.19
Modified: 2025.03.19
Author: MK
"""

import json

from .quote import Quote
from .quote_file_paths import FilePaths

class JsonLoader:
    """
    Klasa wczytująca dane z pliku JSON.
    """
    def __init__(self, file_paths: FilePaths) -> None:
        self.file_paths = file_paths
        self._load_json_file()

    def _load_json_file(self) -> None:
            if not self.file_paths.json:
                raise ValueError("Ścieżki JSON nie są zdefiniowane")
                
            with open(self.file_paths.json.json_file, 'r') as file:
                self.json_file = json.load(file)
            self.quotes = [Quote(**quote) for quote in self.json_file['quotes']]
            self.meta_data = self.json_file['meta_data']
            self.number_of_autors = len(set([quote.autor for quote in self.quotes]))     
            self.number_of_quotes = len(self.quotes)  

    def get_quotes(self) -> list[Quote]:
            return self.quotes

    def get_meta_data(self) -> dict:
            return self.meta_data   

    def get_number_of_autors(self) -> int:
            return self.number_of_autors

    def get_number_of_quotes(self) -> int:
            return self.number_of_quotes


