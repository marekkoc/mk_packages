#! /usr/bin/env python3

"""
Plik testuje nazwy plików z cytatami i ich nicki.

Created: 2025.03.22
Modified: 2025.03.22
Author: MK
"""

# Importujemy predefiniowane obiekty zamiast tworzyć je na nowo
from mkquotes.old.quote_instances import DAWKA, NOTATKI, UMOWY, ALL_QUOTE_FILE_NAMES

if __name__ == "__main__":
    def main():
        # Teraz używamy predefiniowanych obiektów
        lst = ALL_QUOTE_FILE_NAMES

        print()
        for item in lst:
            print(item)
        print()

        print(DAWKA)
        print(NOTATKI)
        print(UMOWY)

    main()

