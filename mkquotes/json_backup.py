"""
Created: 2025.03.20
Modified: 2025.03.20

Author: MK
"""


import shutil
from pathlib import Path
from .quote_file_paths import FilePaths

class JsonBackup:
    def __init__(self, file_paths: FilePaths) -> None:
        self.file_paths = file_paths

    def backup(self):
        print(f"Backuped :")
        base_folder = self.file_paths.base_folder     
        
        
        if self.file_paths.json is None:
            print("Nie ustawionościeżek do plików JSON")
            return
            
        if not self.file_paths.json.json_file.exists():
            print(f"File {self.file_paths.json.json_file.name} nie istnieje")
            return
        
        backup_folder = self.file_paths.json.json_backup_folder
        shutil.copy(self.file_paths.json.json_file, backup_folder)
        backup_folder_name = Path(backup_folder).name
        print(f"\t{self.file_paths.json.json_file.name} ---> {backup_folder_name}/{self.file_paths.json.json_file.name}")
        print()
        
if __name__ == "__main__":
    file_paths = FilePaths("dawka-motywacji")
    json_backup = JsonBackup(file_paths)
    json_backup.backup()
