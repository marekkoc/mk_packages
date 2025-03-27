"""
Pakiet do zarządzania i wybierania cytatów (mott).

Ten pakiet zawiera narzędzia do wczytywania, zapisywania, zarządzania
i wybierania cytatów z różnych źródeł.

Created: 2025.03.15
Modified: 2025.03.19
Author: MK
"""

from .quote import Quote
from .quote_manager import QuoteManager
from .quote_selector import QuoteSelector
from .quote_file_paths import FilePaths
from .txt_2_json import Txt2JsonConverter
from .odt_2_txt import Odt2TxtConverter
from .json_loader import JsonLoader
from .json_saver import JsonSaver
from .old.quote_file_names import QuoteFileNames
from .cli_utils import get_file_names

__all__ = [
    'Quote',
    'QuoteManager',
    'QuoteSelector',
    'FilePaths',
    'Txt2JsonConverter',
    'Odt2TxtConverter',
    'JsonLoader',
    'JsonSaver',
    'QuoteFileNames',
    'get_file_names',
]

__version__ = '0.1.0' 