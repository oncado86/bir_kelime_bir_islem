from abc import ABC, abstractmethod as interface
from dataAccess.wordsDAL import WordsDal


class IWordsManager(ABC):
    """Kelime iş katmanı (IWordsManager sınıfı) için gerekli olan metotların imzalarını tutar.
        @category: Interface
        @category: Business, Manager"""
    def __init__(self):
        """WordsManager sınıfı için gerekli olan metotların imzalarını tutar"""
        self._message = "Implement this method in subclass of IWordsManager"

    @property
    @interface
    def words(self) -> list[str]:
        """Oyun içerisinde kullanılacak kelimelerin listesini verir

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir

        Returns:
            list[str]: Kelime listesi
        """
        raise NotImplementedError(self._message)

    @property
    @interface
    def path(self) -> str:
        """İçerisinde kelimelerin tutulduğu dosyanın yolunu verir

            Raises:
                NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir
            Returns:
                path[str]: dosya yolu"""
        raise NotImplementedError(self._message)

    @path.setter
    @interface
    def path(self, path: str) -> None:
        """İçerisinde kelimelerin tutulduğu dosyanın yolunu ayarlar

        Args:
            path (str): dosya yolu

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir
        """
        raise NotImplementedError(self._message)

    @interface
    def open(self, path: str) -> list[str] | None:
        """Kelimelerin içerisinde bulunduğu dosyayı açıp içerisindeki verileri almayı sağları

        Args:
            path (str): dosyanın bulunduğu konumun yolu

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir

        Returns:
            list[str]: kelimelerin listesi 
        """
        raise NotImplementedError(self._message)
