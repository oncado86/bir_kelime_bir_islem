from typing import Literal
from business.gameManager.iGameManager import IGameManager
from entity.game_data import GameData
from entity.player import Player
from random import randint as rsayi, choice as rsecim
from PyQt5.QtWidgets import QMessageBox as message_box


class GameManager(IGameManager):
    """Oyun ile ilgili metotların bulunduğu sınıf.
    IGameManager arayüz sınıfını kullanır.

    Args:
        IGameManager (interface): GameManager sınıfının arayüz sınıfı
    @category: Business, Manager
    @see: IGameManager
    """

    def __init__(self) -> None:
        """Oyun ile ilgili metotların bulunduğu sınıf.
        """
        self._game_data = GameData()
        self._player = Player()
        self.create_numbers()
        self.choice_npc()

    @property
    def game_data(self) -> GameData:
        """Oyun verilerini ulaşmayı sağlayan property.
        GameData sınıfından türetilir.

        Returns:
            property (GameData): Oyun verileri
        """
        return self._game_data

    @property
    def player(self) -> Player:
        """NPC (Non-Player Character) verilerini ulaşmayı sağlayan property.
        Player sınıfından türetilir

        Returns:
            property (Player): NPC verileri
        """
        return self._player

    def create_numbers(self) -> None:
        """Oyun içerisinde kullanılacak olan sayıların türetilmesini sağlar.
        5 tane 1 basamaklı,
        1 tane 2 basamaklı,
        1 tane 3 basamaklı"""
        self.game_data.number_list.clear()
        self.game_data.number_list = [rsayi(1, 9) for i in range(5)]
        self.game_data.number_list.append(rsayi(10, 99))
        self.game_data.target_number = rsayi(100, 999)

    def choice_npc(self) -> None:
        """Oyunu oynayacak NPC (Non-Player Character)'i türetir.
        """
        self.player.process = ""
        self.player.score = 0
        self.player.name = rsecim(self.game_data.npc_names)

    def isFinished(self, bulunan_sonuc: float) -> bool:
        """Yapılan işlemler sonucunda ulaşılan sonucun, ulaşılmak istenen sonuç aralığında olup olmadığını kontrol eder.

        Args:
            bulunan_sonuc (int): Hesaplamalar sonucu ulaşılan sonuç
        Returns:
            bool: İstenilen aralıktaysa -> True, değilse -> False"""
        return ((self.game_data.target_number-9) <= bulunan_sonuc <= (self.game_data.target_number+9))

    def process(self, gelen_sonuc: float, gelen_sayi: float, gelen_cikti: str) -> tuple[float, str]:
        """Tüm hesaplamaları rasgele olarak yapmaya yarar.

        Args:
            gelen_sonuc (float): bir önceki adımda bulunmuş olan sonuç değeri.
            gelen_sayi (float): işleme tabi tutulacak sayı değeri.
            gelen_cikti (str): daha önceki işlemlerin geçmişi.

        Returns:
            sonuc (float): işlemler sonrası elde edilen sonuç değeri.
            cikti (str): işlemler sonrası elde edilen matematiksel işlem sırası.
        """

        islem = rsecim(["+", "-", "*", "/"])

        # Çarpma ve bölme işlemine göre 1 etkisiz elemandır
        # Çarpma ya da bölme işlemiyle 1 sayısının kullanımasını engeller.
        if ((islem == "*" or islem == "/") and gelen_sayi == 1) or (gelen_sonuc == 1 and (islem == "*" or islem == "/")):
            return float(gelen_sonuc), gelen_cikti
        sonuc = eval(f"{gelen_sonuc} {islem} {gelen_sayi}")

        # Ekranda daha anlaşılır olması için çarpma ve bölme operatörlerinin simgesi değiştirilir.
        if islem == "*":
            islem = "x"
        if islem == "/":
            islem = "÷"

        cikti = f"({gelen_cikti} {islem} {gelen_sayi})"
        return float(sonuc), cikti

    def information_message(self) -> tuple[bool, int]:
        """Kullanıcıya bilgilendirme mesajı görüntüler.

        Returns:
            True/False: geri döndürülen değer sonucunda hesaplama denemelerine baştan başlanır ya da hesaplama bitirilir.
            0: deneme_adedi değişkenini 0 olarak ayarlar, bu sayede tüm denemeler tekrar yapılabilir.
        """

        evet = message_box().StandardButton.Yes
        hayir = message_box().StandardButton.No

        mesaj = message_box.critical(None,  # type: ignore
                                     "Uzun Sürdü!",
                                     f"{self.player.name}..\n\nÇok zor!\nBir çok kombinasyon denedim fakat sonuca ulaşamadım..\nDenemeye devam etmemi ister misin?",
                                     evet | hayir)  # type: ignore # type : ignore
        if mesaj == evet:
            return True, 0
        return False, 0

    def set_player_values(self, sonuc: float, cikti: str, numbers: list) -> None:
        """ NPC verilerini ayarlar
        """
        if (abs(sonuc - self.game_data.target_number)) in numbers:
            # son hamlede hedefe ulaşmak için
            # aradaki fark listede varsa ve kullanılmamışsa, hedeflenen sayıya ulaşılır
            fark = abs(sonuc - self.game_data.target_number)
            if sonuc > self.game_data.target_number:
                sonuc -= fark
                cikti += f" - {int(fark)})"
            if self.game_data.target_number > sonuc:
                sonuc += fark
                cikti += f" + {int(fark)})"
            cikti += f" = {sonuc:.2f}"
            self.player.process = cikti
            self.player.score = 100
        else:
            # istenilen sonuca ulaşılırsa, NPC (Non-Player Character)'nin puanı ve  matematiksel işlemler (işlem önceliğine uygun olarak) ekranda gösterilir.
            cikti += f" = {sonuc:.2f}"
            sonuc = float(f"{sonuc:.2f}")
            self.player.process = cikti
            # puan: ulaşışmak istenilen sayı ile hesaplanan sayı arasındaki farkın mutlak değerinin 10 katı olarak hesaplanmaktadır.
            fark = 10 - abs(sonuc - self.game_data.target_number)
            self.player.score = fark*10

    def calculate(self, tekrar_sayisi: int) -> Literal[True] | None:
        """Rasgele üretilmiş sayıları, yine rasgele olarak işlemlere tabi tutup istenilen sayıya ulaşmaya çalışır.

        Args:
            tekrar_sayisi (int): İşlemlerin kaç defa tekrarlanacağını (denemenin bir seferde kaç defa yapılacağını) belirtir.
        """
        hesapla = True
        deneme_adedi = 0

        """
            Sayı listesinden rasgele bir değer, sonuç olarak kabul edilerel işlemlere başlanır.
            Bu rasgele işlem adedince sayı listesinden sayılar alınır ve yine rasgele işlemlere tabi tutulur.
            Eğer istenilen sonuca ulaşılırsa döngü kırılır,
            istenilen sonuca ulaşılamazsa sonsuz döngüye girilmemesi için kullanıcıya bir bilgi mesajı verilir.
        """
        while hesapla:
            sayilar = self.game_data.number_list.copy()
            # listeden rasgele bir sayı sonuc olarak kabul edilir ve sayının tekrar kullanılmaması için listeden çıkartılır.
            sonuc = rsecim(sayilar)
            sayilar.remove(sonuc)
            cikti = f"{sonuc}"

            while len(sayilar) > 0:
                # listeden rasgele bir sayı işleme tabi tutulmak için seçilir ve sayının tekrar kullanılmaması için listeden çıkartılır.
                # işlem sonucu 0 değerini türetirse döngü adımları atlanır
                sayi = rsecim(sayilar)
                sonuc, cikti = self.process(sonuc, sayi, cikti)
                if sonuc == 0:
                    continue
                sayilar.remove(sayi)
                if self.isFinished(sonuc):
                    self.set_player_values(sonuc, cikti, sayilar)
                    return True
                elif deneme_adedi == tekrar_sayisi:
                    # deneme sayacı tamamlandığında istenilen sonuca ulaşılamazsa bilgi mesajı verilir
                    hesapla, deneme_adedi = self.information_message()

            deneme_adedi += 1
