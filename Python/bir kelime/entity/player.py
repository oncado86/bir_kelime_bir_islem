class Player:
    """NPC (Non-Player Character) verilerinin tutulduğu varlık sınıfı
    @category: Entity Class"""

    def __init__(self):
        """NPC (Non-Player Character) verilerinin tutulduğu varlık sınıfı
        @category: Entity Class"""
        self._name = ""
        self._score = 0.0
        self._finded_words = []

    @property
    def name(self) -> str:
        """NPC (Non-Player Character) 'in isim verisini geri döndürür

        Returns:
            name (str): NPC ismi"""
        return self._name

    @name.setter
    def name(self, npc_name: str) -> None:
        """NPC (Non-Player Character) 'in isim verisini ayarlar

        Args:
            value (str): NPC ismi"""
        self._name = npc_name

    @property
    def score(self) -> float:
        """NPC (Non-Player Character) 'in puan verisini geri döndürür

        Returns:
            score (float): NPC puanı"""
        return self._score

    @score.setter
    def score(self, score: float) -> None:
        """NPC (Non-Player Character) 'in puan verisini ayarlar

        Args:
            value (float): NPC puanı"""
        self._score = score

    @property
    def finded_words(self) -> list[str]:
        """NPC (Non-Player Character) 'in bulduğu kelime verilerini geri döndürür.

        Returns:
            process (str): NPC işlemleri"""
        return self._finded_words

    @finded_words.setter
    def finded_words(self, word: str) -> None:
        """NPC (Non-Player Character) 'in bulduğu kelime verisini ayarlar.

        Args:
            value (str): NPC işlemi"""
        self._finded_words.append(word)
