class Player:
    """NPC (Non-Player Character) verilerinin tutulduğu varlık sınıfı
    @category: Entity Class"""

    def __init__(self) -> None:
        """NPC (Non-Player Character) verilerinin tutulduğu varlık sınıfı
    @category: Entity Class"""
        self._name = ""
        self._score = 0.0
        self._process = ""

    @property
    def name(self) -> str:
        """NPC (Non-Player Character) 'in isim verisini geri döndürür

        Returns:
            name (str): NPC ismi"""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """NPC (Non-Player Character) 'in isim verisini ayarlar

        Args:
            value (str): NPC ismi"""
        self._name = value

    @property
    def score(self) -> float:
        """NPC (Non-Player Character) 'in puan verisini geri döndürür

        Returns:
            score (float): NPC puanı"""
        return self._score

    @score.setter
    def score(self, value: float) -> None:
        """NPC (Non-Player Character) 'in puan verisini ayarlar

        Args:
            value (float): NPC puanı"""
        self._score = value

    @property
    def process(self) -> str:
        """NPC (Non-Player Character) 'in yaptığı işlem verilerini geri döndürür.

        Returns:
            process (str): NPC işlemleri"""
        return self._process

    @process.setter
    def process(self, value: str) -> None:
        """NPC (Non-Player Character) 'in yaptığı işlem verisini ayarlar.

        Args:
            value (str): NPC işlemi"""
        self._process = value
