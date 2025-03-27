"""
Moduł zawiera nazwy plików cytatów.

Created: 2025.03.22
Modified: 2025.03.22
Author: MK
"""

class QuoteFileNames:
    """
    Klasa zawiera nazwy plików cytatów.
    """

    def __init__(self, file_name: str, nick: str) -> None:
        self.file_name = file_name
        self.nick = nick

    def get_file_name(self) -> str:
        return self.file_name
    
    def get_nick(self) -> str:
        return self.nick        
    
    def __str__(self) -> str:
        return f"{self.file_name} /{self.nick}/"
