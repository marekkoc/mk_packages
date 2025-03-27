"""
Created: 2025.03.10
Modified: 2025.03.19
Author: MK
"""

import subprocess
from pathlib import Path

from .quote_file_paths import FilePaths  # Import względny dla użycia jako pakiet


class Odt2TxtConverter:
        
    def __init__(self, file_paths: FilePaths):
        self.file_paths = file_paths
        
    def odt_2_txt(self):
        """
        Konwertuje cytaty z pliku odt na txt.
        Wykorzystuje LibreOffice w trybie headless do konwersji.
        """        
        
        base_name = self.file_paths.base_name
        odt_folder = self.file_paths.odt.odt_folder if self.file_paths.odt else None
        txt_folder = self.file_paths.txt.txt_folder if self.file_paths.txt else None
        input_file = odt_folder / f"{base_name}.odt" if odt_folder else None
        
        # Sprawdzenie czy plik istnieje
        if not input_file:
            raise FileNotFoundError(f"Plik {input_file} nie znaleziony")
        
        try:
            # Wykonanie komendy konwersji
            cmd = ["libreoffice", "--headless", "--convert-to", "txt", str(input_file)]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            
            # Przeniesienie pliku do katalogu cytaty, jeśli został utworzony w bieżącym katalogu
            output_file = Path(f"{base_name}.txt")
            if output_file.exists():
                if self.file_paths.txt:
                    target_path: Path = self.file_paths.txt.txt_folder / output_file.name
                    output_file.rename(target_path)
                    print(f'   Plik: \"{input_file.name}\" -----> \"./{self.file_paths.txt.txt_folder.name}/{target_path.name}\"')
                else:
                    print(f"Nie można przenieść pliku - brak skonfigurowanego katalogu TXT")
            else:
                print("Konwersja zakończona, ale nie znaleziono pliku wyjściowego")
                
        except subprocess.CalledProcessError as e:
            print(f"Błąd podczas konwersji pliku: {e}")
            print(f"Wyjście błędu: {e.stderr}")
        except Exception as e:
            print(f"Wystąpił nieoczekiwany błąd: {e}")


if __name__ == "__main__":
    
    def main():
        names = ["dawka-motywacji", "52-notatki", "2007_Ruiz_Cztery-umowy"] 
        for name in names:
            print(f"\n\"{name}\":")
            file_paths = FilePaths(name)
            
            odt_converter = Odt2TxtConverter(file_paths)
            odt_converter.odt_2_txt()
    
    main()







