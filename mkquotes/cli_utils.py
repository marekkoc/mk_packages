"""
Narzędzia do obsługi argumentów linii poleceń.

Created: 2025.03.23
Modified: 2025.03.23
Author: MK
"""

import sys

def get_file_names(default_files=None):
    """
    Pobiera nazwy plików z argumentów linii poleceń lub zwraca domyślną listę.
    
    Args:
        default_files (list): Domyślna lista plików, jeśli nie podano argumentów.
                             Jeśli None, zwraca pustą listę.
    
    Returns:
        list: Lista nazw plików do przetworzenia
    """
    if default_files is None:
        default_files = []
        
    # Sprawdź, czy podano argumenty z linii poleceń
    if len(sys.argv) > 1:
        # Użyj argumentów z linii poleceń jako nazw plików
        return sys.argv[1:]
    else:
        # Użyj domyślnej listy plików
        return default_files 