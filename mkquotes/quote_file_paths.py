"""
Created: 2025.03.12
Modified: 2025.03.18
Author: MK
"""

from pathlib import Path
from mkenvs import EnvVars

class QuotePaths:
    def __init__(self, base_name: str, base_folder: Path | str | None = None) -> None:
        self.base_folder: Path  = Path(base_folder) if base_folder else Path(EnvVars.get_python_quotes())
        self.base_name = base_name
        self.tmp_name = f"{self.base_name}-tmp"
               
class ODTPaths(QuotePaths):
    extension = 'odt'
    
    def __init__(self, base_name: str, base_folder: Path | str | None = None) -> None:
        super().__init__(base_name, base_folder)
        
        self.odt_folder = Path(self.base_folder) / 'odt'
        self.odt_file = self.odt_folder / f"{self.base_name}.{ODTPaths.extension}"

    def __str__(self) -> str:
        s = f"ODT Paths:"
        s += f"\n\tbase_name={self.base_name}"
        s += f"\n\tbase_folder={self.base_folder}"
        s += f"\n\ttmp_name={self.tmp_name}"
        s += f"\n\todt_folder={self.odt_folder}"
        s += f"\n\todt_file={self.odt_file}"        
        return s

class TXTPaths(QuotePaths):
    extension = 'txt'

    def __init__(self, base_name: str, base_folder: Path | str | None = None) -> None:
        super().__init__(base_name, base_folder)
        
        self.txt_folder = Path(self.base_folder) / 'txt'
        self.txt_file = self.txt_folder / f"{self.base_name}.{TXTPaths.extension}"       

    def __str__(self) -> str:
        s = f"TXT Paths:"
        s += f"\n\tbase_name={self.base_name}"
        s += f"\n\tbase_folder={self.base_folder}"
        s += f"\n\ttmp_name={self.tmp_name}"
        s += f"\n\ttxt_folder={self.txt_folder}"
        s += f"\n\ttxt_file={self.txt_file}"        
        return s

class JSONPaths(QuotePaths):
    extension = 'json'

    def __init__(self, base_name: str, base_folder: Path | str | None = None) -> None:
        super().__init__(base_name, base_folder)        
        self.json_folder = Path(self.base_folder) 
        self.json_file = self.json_folder / f"{self.base_name}.{JSONPaths.extension}"
        self.json_tmp_file = self.json_folder / f"{self.tmp_name}.{JSONPaths.extension}"
        self.json_backup_folder = Path(self.base_folder) / 'json_backup'

    def __str__(self) -> str:
        s = f"JSON Paths:"
        s += f"\n\tbase_name={self.base_name}"
        s += f"\n\tbase_folder={self.base_folder}"
        s += f"\n\ttmp_name={self.tmp_name}"
        s += f"\n\tjson_folder={self.json_folder}"
        s += f"\n\tjson_file={self.json_file}"
        s += f"\n\tjson_tmp_file={self.json_tmp_file}"
        s += f"\n\tjson_backup_folder={self.json_backup_folder}"
        return s
                
class FilePaths:
    """
    Klasa agregująca wszystkie typy ścieżek do plików.
    Używa klas specjalistycznych do obsługi poszczególnych typów plików.
    """
    def __init__(self, base_name: str, base_folder: Path | str | None = None, create: str = "json-txt-odt") -> None:
        """
        Inicjalizuje obiekt FilePaths.

        Args:
            base_name (str): Nazwa podstawowa pliku.
            base_folder (str | None, optional): Ścieżka do folderu bazowego. Domyślnie None.
            create (str, optional): Określa, które typy ścieżek mają być utworzone.
                                   Format: "typ1-typ2-typ3". Domyślnie "json-txt-odt".
        """
        self.base_name = base_name
        self.base_folder = Path(base_folder) if base_folder else Path(EnvVars.get_python_quotes())  
        
        # Konwersja parametru create na listę typów
        create_types = create.lower().split('-')
        
        # Inicjalizacja poszczególnych typów ścieżek w zależności od parametrów
        self.odt = ODTPaths(base_name, base_folder) if "odt" in create_types else None
        self.txt = TXTPaths(base_name, base_folder) if "txt" in create_types else None
        self.json = JSONPaths(base_name, base_folder) if "json" in create_types else None
        
        # Dla zachowania kompatybilności wstecznej
        self.file_path_txt = self.txt.txt_file if self.txt else None
        self.file_path_json = self.json.json_file if self.json else None

    def __str__(self) -> str:
        s = f"FilePaths:"
        s += f"\n\tbase_name={self.base_name}"
        s += f"\n\tbase_folder={self.base_folder}"
        if self.odt:
            s += f"\n\n\tODT:"
            s += f"\n\todt={self.odt}"
        else:
            s += f"\n\n\tODT: nie istnieje"
        if self.txt:
            s += f"\n\n\tTXT:"
            s += f"\n\ttxt={self.txt}"
        else:
            s += f"\n\n\tTXT: nie istnieje"
        if self.json:
            s += f"\n\n\tJSON:"
            s += f"\n\tjson={self.json}"
        else:
            s += f"\n\n\tJSON: nie istnieje"
        return s


if __name__ == "__main__":

    def main():
        names = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"]        
        
        for name in names:
            file_paths = FilePaths(name)
            if file_paths.txt:
                print(f"Plik txt:\t{file_paths.txt.txt_file.name},    (istnieje: {file_paths.txt.txt_file.exists()})")
            if file_paths.json:
                print(f"Plik json:\t{file_paths.json.json_file.name}, (istnieje: {file_paths.json.json_file.exists()})")
            print()
            

    main()
