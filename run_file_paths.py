#! /usr/bin/env python3
"""
Skrypt testujący działanie klasy FilePaths.

Created: 2025.03.22
Modified: 2025.03.23
Author: MK
"""

from mkquotes.quote_file_paths import FilePaths
from mkquotes.quote_file_paths import ODTPaths
from mkquotes.quote_file_paths import TXTPaths
from mkquotes.quote_file_paths import JSONPaths
from mkquotes.cli_utils import get_file_names


def test_odt_paths(name):   
    print()
    odt_paths = ODTPaths(name)
    print(odt_paths)

def test_txt_paths(name):
    print()
    txt_paths = TXTPaths(name)
    print(txt_paths)

def test_json_paths(name):
    print()
    json_paths = JSONPaths(name)
    print(json_paths)

def test_file_paths1(name, create="odt-txt-json"):
    file_paths = FilePaths(name, create=create)
    print(file_paths)

def main():
    default_files = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]
    file_names = get_file_names(default_files)
    for name in file_names:
        print(f"\n\"{name}\":")

        #test_odt_paths(name)
        #test_txt_paths(name)
        #test_json_paths(name)

        test_file_paths1(name, create = "json")
    print()


main()