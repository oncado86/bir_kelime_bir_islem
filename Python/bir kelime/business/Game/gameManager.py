from business.Game.iGameManager import IGameManager
from business.Words.wordsManager import WordsManager
from entity.gameData import GameData
from entity.player import Player
from random import choice as rsecim, choices as rsecimler


class GameManager(IGameManager):
    """Oyun ile ilgili metotların bulunduğu sınıf.
    IGameManager arayüz sınıfını kullanır.

    Args:
        IGameManager (interface): GameManager sınıfının arayüz sınıfı
    @category: Business, Manager
    @see: IGameManager
    """

    def __init__(self):
        """Oyun ile ilgili metotların bulunduğu sınıf.
        @category: Business, Manager"""
        self._game_data = GameData()
        self._player = Player()
        self._wordsManager = WordsManager()
        self.choice_npc()
        self.create_letters()
        self._get_words()

    @property
    def game_data(self) -> GameData:
        return self._game_data

    @property
    def player(self) -> Player:
        return self._player

    @property
    def words(self) -> list[str]:
        return self._wordsManager.words

    def _get_words(self) -> None:
        """Kelimelerin içerisinde bulunduğu dosyayı açıp içerisindeki verileri almayı sağlar.
        Bu sayede NPC (Non-Player Character)'in türettiği kelimeler bu veriler ile kıyaslanıp kelimenin doğruluğu kontrol edilebilir.
        """
        self._wordsManager.open(self._wordsManager.path)

    def create_letters(self) -> None:
        # rasgle seçlen 10 adet ünlü, 10 adet ünsüz harf ile bir liste
        harfler_temp = [rsecimler(self.game_data.alfabe[0:8], k=10)] + \
            [rsecimler(self.game_data.alfabe[8:], k=10)]
        harfler = []
        self.game_data.letters.clear()
        for i in range(2):
            for harf in harfler_temp[i]:
                harfler.append(harf)
        self.game_data.letters = harfler

    def choice_npc(self) -> None:
        self.player.name = rsecim(self.game_data.npc_names)

    def process(self) -> None:
        # önceki işlemlerde veri olmasına karşın bulunan kelmeler listesi temizlenir
        self.player.finded_words.clear()

        for kelime in self.words:  # dosyadaki kelimeler tek tek gezilir
            # kontrol edilen kelimenin harfleri bir listeye dönüştürülür
            kelime_harfler = [i for i in kelime]
            for harf in self.game_data.letters:  # kullanılacak harfler tek tek gezilir
                if harf in kelime_harfler:  # sıradaki harf, kontrol edilen kelime içinde varsa, kontroldeki kelime harfleri listesinden çıkartılır
                    kelime_harfler.remove(harf)
            # kontrol edilen kelime harf sayısı >=2 ve de kelime harf listesindeki eleman sayısı 0 ise bulunan kelime listesine eklenir
            if len(kelime_harfler) == 0 and len(kelime) >= 2:
                self.player.finded_words = f"{kelime} ({len(kelime)})"

        self._with_points()
        self.player.finded_words.sort(key=len)
        self.player.finded_words.reverse()

    def _with_points(self) -> None:
        self.player.score = 0
        # puanlama: kelimelerin harf sayılarının toplanmasıyla yapılır
        for word in self.player.finded_words:
            self.player.score += len(word)
