#! /usr/bin/env python3
"""
Skrypt testujący działanie klasy QuoteManager.

Created: 2025.03.22
Modified: 2025.03.23
Author: MK
"""

from mkquotes.quote_manager import QuoteManager
from mkquotes.quote_file_paths import FilePaths
from mkquotes.json_loader import JsonLoader
from mkquotes.json_saver import JsonSaver
from mkquotes.cli_utils import get_file_names

def main():
    default_files = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]
    file_names = get_file_names(default_files)
    for name in file_names:
        print(f"\n\"{name}\":")

        file_paths = FilePaths(name, create="json")
        quote_manager = QuoteManager()

        json_loader = JsonLoader(file_paths)
        json_saver = JsonSaver(file_paths)

        quote_manager.set_json_loader(json_loader)
        quote_manager.set_json_saver(json_saver)

        quote_manager.save_to_json(test_mode=True)

def test_operator_indeksowania():
    print("test operator indeksowania")
    file_paths = FilePaths("dawka-motywacji", create="json")
    quote_manager = QuoteManager()
    json_loader = JsonLoader(file_paths)
    quote_manager.set_json_loader(json_loader)

    print()

    print(quote_manager[1].print_with_id())
    print(quote_manager[2].print_with_id())
    print(quote_manager[3].print_with_id())

    print()

    print(quote_manager.next(2).print_with_id())
    print(quote_manager.previous(2).print_with_id())



if __name__ == "__main__":
    #main()
    test_operator_indeksowania()