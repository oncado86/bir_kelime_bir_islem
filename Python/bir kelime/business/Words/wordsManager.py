from business.Words.iWordsManager import IWordsManager
from dataAccess.wordsDAL import WordsDal
from core.information import Information as info


class WordsManager(IWordsManager):
    """Kelimelerin bulunduğu dosyaya erişmek için gerekli olan iş katmanı
    IWordsManager arayüz sınıfını kullanır.
        Args:
            IWordsDal (interface): WordsManager sınıfnın arayüzü
        @category: Business, Manager
        @see: IWordsManager"""

    def __init__(self):
        """Kelimelerin bulunduğu dosyaya erişmek için gerekli olan işkatmanı
        @category: Business, Manager"""
        self._wordsDal = WordsDal()

    @property
    def words(self):
        return self._wordsDal.words

    @property
    def path(self) -> str:
        return self._wordsDal.path

    @path.setter
    def path(self, path: str):
        if len(path) > 0:
            self._wordsDal.path = path

    def open(self, path: str):
        if len(path) > 0 and ".txt" in path:
            try:
                return self._wordsDal.open(path)
            except Exception:
                info().information_message("Dosya açılırken beklenmedik bir hata oluştu")
