"""
Created: 2025.03.07
Modified: 2025.03.19
Author: MK
"""

import json
import datetime
from pathlib import Path


from .quote import Quote
from .quote_file_paths import FilePaths
from .json_saver import JsonSaver


class Txt2JsonConverter():
    def __init__(self, json_saver: JsonSaver) -> None:
        """
        Klasa wczytuje plik tekstowy. 

        Domyślnie zakładamy, że plik jest w katalogu cytaty.
        
        Created: 2025.03.10
        Modified: 2025.03.12
        """
        self.json_saver = json_saver    
        self.file_paths = json_saver.file_paths
        self.file_keys: list[str] = ["date", "source", "category", "modivied", "version", "autor", "year"]
        # '\xa0'-niełamliwa spacja, '\u200b'-zero-width space, '\u200c'-zero-width non-joiner,
        #  '\u200d'-zero-width joiner, '\u200e'-left-to-right mark
        # '\u200f'-right-to-left mark, '\u202f'-narrow no-break space
        self.replace_characters  = ['\xa0', '\u200b', '\u200c', '\u200d', '\u200e', '\u200f', '\u202f', '  ']

        self.lines_content: list[str] = self._load_lines_from_txt()
        self.meta_data: dict[str, str] = self._load_meta_data()
        self.quotes: list[Quote] = self._load_various_atuhor_mottoes()
        self.json_saver.set_meta_data(self.meta_data)
        self.json_saver.set_quotes(self.quotes)
        self.json_saver.save_to_json()

    def _load_lines_from_txt(self) -> list[str]:
        """
        Metoda wczytuje zawartość pliku tekstowego.
        """       
        # Sprawdzenie czy ścieżka do pliku istnieje
        if self.file_paths.file_path_txt is None:
            raise FileNotFoundError("Ścieżka do pliku tekstowego nie jest zdefiniowana")
        
        # Sprawdzenie czy plik istnieje
        if not self.file_paths.file_path_txt.exists():
            raise FileNotFoundError(f"Plik {self.file_paths.file_path_txt} nie znaleziony")       
       
        with open(self.file_paths.file_path_txt, 'r', encoding='utf-8-sig') as plik:
            return plik.readlines()

    def _normalize_text(self, text: str) -> str:
        """
        Normalizuje tekst, zamieniając polskie znaki na ich odpowiedniki bez ogonków.
        """
        polish_chars = {
            'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 
            'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
            'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N', 
            'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
        }
        for polish, latin in polish_chars.items():
            text = text.replace(polish, latin)
        return text

    def _load_meta_data(self) -> dict[str, str]:
        """
        Metoda zwraca metadane pliku.
        """
        meta_data = {}
        for linia in self.lines_content:
            if linia.startswith(tuple(["*", " *", "  *"])):
                linia = linia.strip().strip("*").strip()
                # Normalizujemy tekst przed sprawdzeniem kluczy
                #normalized_line = self._normalize_text(linia.lower())
                # Dodaj informacje o cytatach do słownika
                #for key in self.file_keys:
                 #   if normalized_line.startswith(key.lower()):
                print(f"\t{linia}")
                original_key = linia.lower().split(": ")[0].strip().title()
                meta_data[original_key] = linia.lower().split(": ")[1].title().strip()
        return meta_data

    def _load_various_atuhor_mottoes(self) -> list[Quote]:
        """        
        Lista linii z pliku według NOWEGO formatu:
        - linie z informacjami o cytatach (data, zrodlo, kategoria,...)
        - cytat,
        - autor.
        """
        quotes = []
        quote = {}        
        
        for linia in self.lines_content:
            linia = linia.strip()  # usuń białe znaki z początku i końca

            # Pomiń puste linie
            if not linia or linia.startswith(tuple(["#", "*", " *", "  *"])):
                continue

            # Pomijamy meta dane
            normalized_line = self._normalize_text(linia.lower())
            if normalized_line.lower().startswith(tuple(self.file_keys)):
                continue

            # Zamieniamy znaki specjalne na spacje
            for char in self.replace_characters:
                linia = linia.replace(char, ' ')
            
            # Jeśli linia nie jest pusta i nie mamy jeszcze cytatu, to to jest cytat
            if not "c" in quote:
                quote["c"] = linia if linia.endswith((".", "!", "?")) else linia + "."
            # Jeśli mamy już cytat, ale nie mamy autora, to to jest autor
            elif not "a" in quote:
                quote["a"] = linia.strip()
                
                # Dodaj parę cytat-autor do listy i zresetuj zmienne
                quotes.append(Quote(quote["c"], quote["a"]))
                quote = {}        
        
        # usuwamy duplikaty
        quotes = list(set(quotes))
        
        # dodajemy id do cytatów jako liczba całkowita
        for i, quote in enumerate(quotes, start=1):
            quote.id = i
        print(f"  Dodano id do {len(quotes)} cytatów.")

        # sortujemy cytaty po id
        quotes.sort(key=lambda x: x.id)

        return list(set(quotes)).copy()
    

if __name__ == "__main__":

    def main():
        names = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]
        print()
        for name in names:
            print(f"\"{name}\":")
            
            file_paths = FilePaths(name, create="json-txt")
            json_saver = JsonSaver(file_paths)
            raw_file = Txt2JsonConverter(json_saver) 

            #for key, value in raw_file.meta_data.items():
            #    print(f"\t{key}: {value}")
            
            print()
    print()

    main()


    