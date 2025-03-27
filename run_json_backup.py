#! /usr/bin/env python3
"""
Skrypt testujący. Tworzy kopie zapasowe plików JSON.

Created: 2025.03.20
Modified: 2025.03.23

Author: MK
"""

from mkquotes.json_backup import JsonBackup
from mkquotes.quote_file_paths import FilePaths
from mkquotes.cli_utils import get_file_names

def main():
    # Pobierz nazwy plików z argumentów lub użyj domyślnych
    default_files = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]
    file_names = get_file_names(default_files)
    
    for file_name in file_names:
        file_paths = FilePaths(file_name, create="json")
        json_backup = JsonBackup(file_paths)
        json_backup.backup()

if __name__ == "__main__":
    main()