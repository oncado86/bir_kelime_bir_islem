from pathlib import Path
from dataAccess.iWordsDAL import IWordsDal


class WordsDal(IWordsDal):
    """Kelimelerin bulunduğu dosyaya erişmek için gerekli olan veri erişim katmanı
    IWordsDal arayüz sınıfını kullanır.
        Args:
            IWordsDal (interface): WordsDal sınıfnın arayüzü
        @category: Data Access
        @see: IWordsDal"""

    def __init__(self):
        """Kelimelerin bulunduğu dosyaya erişmek için gerekli olan veri erişim katmanı
        @category: Data Access"""
        import sys
        path_file = Path(sys.path[0])
        self._words = []
        self._path = f"{path_file}/data/kelimeler.txt"

    @property
    def words(self) -> list[str]:
        return self._words

    @property
    def path(self) -> str:
        return self._path

    def open(self, path: str) -> list[str]:
        with open(path) as file:  # verilen konumdaki dosyayı açar
            values = file.readlines()  # verileri satır satır okur
            for value in values:  # okunan verileri tek tek gezer
                # alt satıra geçme ifadesini kaldırarak kelime listesine ekler
                self._words.append(value.replace("\n", ""))
            return self._words
