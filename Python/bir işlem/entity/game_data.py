from tables import Unknown


class GameData:
    """Oyun verilerinin tutulduğu varlık sınıfı
    @category: Entity Class"""

    def __init__(self) -> None:
        """Oyun verilerinin tutulduğu varlık sınıfı
    @category: Entity Class"""
        self._number_list = []
        self._target_number = 0
        self._npc_names = [
            "Darth Maul",
            "Darth Vader",
            "Darth Sidious",
            "Darth Tyranus",
            "Darth Bane",
            "Darth Plaguis"
        ]

    @property
    def number_list(self) -> list[int]:
        """Hesaplamada kullanılacak sayıların listesini geri döndürür

        Returns:
            number_list (list[int]): hesaplamalarda kullanılacak sayıların listesi
        """
        return self._number_list

    @number_list.setter
    def number_list(self, nlist: list[int]) -> None:
        """Hesaplamada kullanılacak sayıların listesini ayarlar

        Args:
            list (list[int]): Sayı listesi
        """
        self._number_list = nlist

    @property
    def target_number(self) -> int:
        """Hesaplamalar sonucu ulaşılmak istenen sayıyı geri döndürür

        Returns:
            target_number (int): ulaşılmak istenen sayı"""
        return self._target_number

    @target_number.setter
    def target_number(self, number: int) -> None:
        """Hesaplamalar sonucu ulaşılmak istenen sayıyı ayarlar

        Args:
            target_number (int): ulaşılmak istenen sayı
        """
        self._target_number = number

    @property
    def npc_names(self) -> list[str]:
        """NPC (Non-Player Character) isim listesini geri döndürür

        Returns:
            npc_names (list[str]): NPC isimleri
        """
        return self._npc_names
