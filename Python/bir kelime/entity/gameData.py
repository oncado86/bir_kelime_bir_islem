class GameData:
    """Oyun verilerinin tutulduğu varlık sınıfı
    @category: Entity Class"""

    def __init__(self) -> None:
        """Oyun verilerinin tutulduğu varlık sınıfı
        @category: Entity Class"""
        self._letters = []
        self._alfabe = [
            "a", "e", "ı", "i", "o", "ö", "u", "ü",
            "b", "c", "ç", "d", "f", "g", "ğ", "h",
            "j", "k", "l", "m", "n", "p", "r", "s",
            "ş", "t", "v", "y", "z"
        ]
        self._npc_names = [
            "Darth Maul",
            "Darth Vader",
            "Darth Sidious",
            "Darth Tyranus",
            "Darth Bane",
            "Darth Plaguis"
        ]

    @property
    def alfabe(self) -> list[str]:
        """Oyun içerisinde kullanılacak olan alfabe"""
        return self._alfabe

    @property
    def letters(self) -> list[str]:
        """Oyun içerisinde NPC (Non-Character Player)'in kelime tahmininde kullanacağı harfleri verir

        Returns:
            letters (list[str]) -> Harf listesi"""
        return self._letters

    @letters.setter
    def letters(self, letters_list: list[str]) -> None:
        """Oyun içerisinde NPC (Non-Character Player)'in kelime tahmininde kullanacağı harfleri ayarlar

        Args:
            letters_list (list[str]) -> Harf listesi"""
        self._letters = letters_list

    @property
    def npc_names(self) -> list[str]:
        """NPC (Non-Player Character) isim listesini geri döndürür

        Returns:
            npc_names (list[str]): NPC isimleri
        """
        return self._npc_names
