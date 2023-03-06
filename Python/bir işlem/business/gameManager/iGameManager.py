from abc import ABC, abstractclassmethod as interface
from typing import Literal

from entity.game_data import GameData
from entity.player import Player


class IGameManager(ABC):
    """GameManager sınıfı için gerekli olan metotların imzalarını tutar.
    
    @category: Interface, Manager"""

    @property  # type: ignore
    @interface
    def game_data(self) -> GameData:
        raise NotImplementedError(
            "Implement 'game_data' method from IGameManager")

    @property  # type: ignore
    @interface
    def player(self) -> Player:
        raise NotImplementedError(
            "Implement 'player' method from IGameManager")

    @interface
    def create_numbers(self) -> None:
        raise NotImplementedError(
            "Implement 'create_numbers' method from IGameManager")

    @interface
    def choice_npc(self) -> None:
        raise NotImplementedError(
            "Implement 'choice_npc' method from IGameManager")

    @interface
    def isFinished(self, value: int) -> bool:
        raise NotImplementedError(
            "Implement 'isFinished' method from IGameManager")

    @interface
    def process(self, gelen_sonuc: float, gelen_sayi: float, gelen_cikti: str) -> tuple[float, str]:
        raise NotImplementedError(
            "Implement 'process' method from IGameManager")

    @interface
    def information_message(self) -> tuple[bool, int]:
        raise NotImplementedError(
            "Implement 'information_message' method from IGameManager")

    @interface
    def calculate(self, tekrar_sayisi: int) -> Literal[True] | None:
        raise NotImplementedError(
            "Implement 'calculate' method from IGameManager")
