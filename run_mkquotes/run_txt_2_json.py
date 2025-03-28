#! /usr/bin/env python3
"""
Skrypt testujący działanie klasy Txt2JsonConverter.

Created: 2025.03.22
Modified: 2025.03.22
Author: MK
"""

from mkquotes.txt_2_json import Txt2JsonConverter
from mkquotes.quote_file_paths import FilePaths
from mkquotes.json_saver import JsonSaver
from mkquotes.quote import Quote
from mkquotes.cli_utils import get_file_names

if __name__ == "__main__":

    def main():

        print()
        default_files = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]
        file_names = get_file_names(default_files)
        for name in file_names:
            print(f"\"{name}\":")
            
            file_paths = FilePaths(name, create="json-txt")
            json_saver = JsonSaver(file_paths)
            raw_file = Txt2JsonConverter(json_saver) 
            
            print()
        print()

    main()