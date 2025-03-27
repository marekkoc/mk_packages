#! /usr/bin/env python3
"""
Skrypt testujący działanie klasy Odt2TxtConverter.

Created: 2025.03.22
Modified: 2025.03.23
Author: MK
"""

from mkquotes.odt_2_txt import Odt2TxtConverter
from mkquotes.quote_file_paths import FilePaths
from mkquotes.cli_utils import get_file_names


def main():

    default_files = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]
    file_names = get_file_names(default_files)
    for name in file_names:
        print(f"\n\"{name}\":")
        file_paths = FilePaths(name, create="odt-txt")
        
        odt_converter = Odt2TxtConverter(file_paths)
        odt_converter.odt_2_txt()

if __name__ == "__main__":
    main()