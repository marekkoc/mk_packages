"""
Created: 2025.03.14
Modified: 2025.03.15
Author: MK
"""

import json
import datetime

from .quote_manager import QuoteManager
from .quote_file_paths import FilePaths
from .quote import Quote

class QuoteManagerIO(QuoteManager):
    """
    Klasa wczytująca i zapisująca motta do pliku typu JSON.
    """
    def __init__(self, file_paths: FilePaths) -> None:
        super().__init__()
        self.file_paths = file_paths
        self._load_json_file() 

    def _load_json_file(self) -> None:
        with open(self.file_paths.file_path_json, 'r') as file:
            self.json_file = json.load(file)
        self.quotes = [Quote(**quote) for quote in self.json_file['quotes']]
        self.meta_data = self.json_file['meta_data']
        self.number_of_autors = len(set([quote.autor for quote in self.quotes]))     
        self.number_of_quotes = len(self.quotes)  

    def save_to_json(self) -> None:
        """
        Zapisuje metadane i motta do pliku JSON.
        
        Args:
            file_path_json (str): Ścieżka do pliku JSON, w którym zostaną zapisane dane.
        """
        # Dodanie aktualnej daty i godziny do meta_data
        meta_data = self.meta_data.copy()
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        meta_data['Aktualizacja'] = current_time
        

        data = {
            "meta_data": meta_data,
            "quotes": [quote.to_dict() for quote in self.quotes]
        }
        
        try:
            with open(self.file_paths.file_path_json, 'w', encoding='utf-8') as plik:
                json.dump(data, plik, ensure_ascii=False, indent=4)
            print(f'Dane zapisane do pliku \"{self.file_paths.file_path_json}\"')
        except Exception as e:
            print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")


if __name__ == "__main__":
    def main():
        file_paths = FilePaths("dawka-motywacji")
        quote_manager_io = QuoteManagerIO(file_paths)
        quote_manager_io.save_to_json()

    main()