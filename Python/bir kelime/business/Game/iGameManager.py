from abc import ABC, abstractmethod as interface

from entity.gameData import GameData
from entity.player import Player


class IGameManager(ABC):
    """GameManager sınıfı için gerekli olan metotların imzalarını tutar.

    @category: Interface, Manager
    """

    @property
    @interface
    def game_data(self) -> GameData:
        """Oyun içerisinde kullanılan verileri verir
        @see: GameData

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir

        Returns:
            GameData: Oyun verilerinin tutulduğu varlık sınıfı
        """
        raise NotImplementedError(
            "Implement 'game_data' method from IGameManager")

    @property
    @interface
    def player(self) -> Player:
        """NPC (Non-Player Character) verilerinin tutulduğu varlık sınıfını verir
        @see: Player

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir

        Returns:
            Player: NPC verilerinin tutulduğu varlık sınıfını
        """
        raise NotImplementedError(
            "Implement 'player' method from IGameManager")

    @property
    @interface
    def words(self) -> list[str]:
        """Oyun içerisinde kullanılacak kelimelerin listesini verir

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir

        Returns:
            list[str]: Kelime listesi"""
        raise NotImplementedError("Implement 'words' method from IGameManager")

    @interface
    def create_letters(self) -> None:
        """Oyun sırasında kelime tahmini için kullanılacak olan harfleri belirler.

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir
        """
        raise NotImplementedError(
            "Implement 'create_letters' method from IGameManager")

    @interface
    def choice_npc(self) -> None:
        """Oyunu oynayacak olan NPC (Non-Character Player)'i türetir

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir
        """
        raise NotImplementedError(
            "Implement 'choice_npc' method from IGameManager")

    @interface
    def process(self) -> None:
        """NPC (Non-Character Player)'nin kelime tahmin etmesini sağlar

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir
        """
        raise NotImplementedError(
            "Implement 'process' method from IGameManager")

    @interface
    def _with_points(self) -> None:
        """NPC (Non-Character Player)'in bulduğu kelimeleri puanlar

        Raises:
            NotImplementedError: Fonksiyon, sınıfta oluşturulmazsa hata mesajını verir
        """
        raise NotImplementedError(
            "Implement '_with_points' method from IGameManager")
