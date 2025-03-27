#! /usr/bin/env python3

"""
Skrypt testujący. Sprawdza działanie klsy do losowego wyboru cytatu.

Created: 2025.03.20
Modified: 2025.03.23

Author: MK
"""

from mkquotes.quote_selector import QuoteSelector
from mkquotes.quote_file_paths import FilePaths
from mkquotes.json_loader import JsonLoader
from mkquotes.cli_utils import get_file_names

def main():
    print()
    default_files = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]
    file_names = get_file_names(default_files)
    for name in file_names:
        print(f"\n\"{name}\":\n")

        file_paths = FilePaths(name, create="json")
        quote_selector = QuoteSelector()
        quote_selector.set_json_loader(JsonLoader(file_paths))
        
        #print(quote_selector.get_autor_quote_count())

        print(quote_selector.random_quote())




if __name__ == "__main__":
    main() 
