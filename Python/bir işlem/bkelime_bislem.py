from random import randint as rsayi
from PyQt5.QtWidgets import (
    QMainWindow as main_window,
    QApplication as application
)
from business.gameManager.gameManager import GameManager
from ui.birkelime_birislem import Ui_MainWindow as ui_main_window


class BirKelimeBirIslem(ui_main_window, main_window):
    """Uygulamanın düzgün çalışabilmesi için; PyQt5 arayüz kütüphanesinin kurulmuş olması gerekmektedir.
    Ayrıntılı bilgi için: https://pypi.org/project/PyQt5/ adresini ziyaret ediniz.
    """

    def __init__(self) -> None:
        """
        Program açıkdığında (bu) yapıcı metot tetiklenir.
        Böylece arayüz kullanıcıya gösterilmiş olur.
        Sayısal veriler üretip ekranda kullanıcıya gösterilir.
        """
        super().__init__()
        self.game_manager = GameManager()
        self.init_ui()

        # Butonlara tıklandığında ne yapacaklarının ayarlanması
        self.ui.btn_rasgele_sayi_uret.clicked.connect(self.fillNumber)
        self.ui.btn_hesapla.clicked.connect(self.calculate)
        self.ui.btn_hepsini_temizle.clicked.connect(self.clear)

    def init_ui(self) -> None:
        """Arayüzü ayarlar ve ekranda gösterir.
        """
        self.ui = ui_main_window()
        self.ui.setupUi(self)
        self.ui.btn_rasgele_sayi_uret.setFocus()
        self.fillNumber()
        self.show()

    def fillNumber(self) -> None:
        """Ekranı temizler ve hesaplamalarda kullanılacak sayıları ekranda gösterir
        """
        self.clear()
        self.game_manager.create_numbers()
        ui = self.ui
        ui.le_hedeflenen_sayi.setText(
            str(self.game_manager.game_data.target_number))
        ui.le_sayi_1.setText(
            str(self.game_manager.game_data.number_list[0]))
        ui.le_sayi_2.setText(
            str(self.game_manager.game_data.number_list[1]))
        ui.le_sayi_3.setText(
            str(self.game_manager.game_data.number_list[2]))
        ui.le_sayi_4.setText(
            str(self.game_manager.game_data.number_list[3]))
        ui.le_sayi_5.setText(
            str(self.game_manager.game_data.number_list[4]))
        ui.le_sayi_10unkati.setText(
            str(self.game_manager.game_data.number_list[5]))
        ui.btn_hesapla.setEnabled(True)
        ui.btn_hepsini_temizle.setEnabled(True)
        self.ui.statusbar.showMessage(
            f"{self.game_manager.player.name}", 3_000)

    def clear(self) -> None:
        """Ekrandaki bilgileri temizler ve Hesaplama & Temizleme Butonlarını pasifleştirir.
        """
        ui = self.ui
        ui.le_sayi_1.clear()
        ui.le_sayi_2.clear()
        ui.le_sayi_3.clear()
        ui.le_sayi_4.clear()
        ui.le_sayi_5.clear()
        ui.le_sayi_10unkati.clear()
        ui.le_hedeflenen_sayi.clear()
        ui.le_islemler.clear()
        ui.btn_hesapla.setEnabled(False)
        ui.btn_hepsini_temizle.setEnabled(False)
        self.game_manager.choice_npc()
        ui.statusbar.clearMessage()

    def calculate(self) -> None:
        """Sonsuz döngü oluşmaması için 50.000-100.000 arasında rasgele sayıda hesaplamaları yapar ve sonucu kullanıcıya bildirir.
        Eğer bulunan sonuç, ulaşılmak istenen sayı ile +-9 fark var ise yapılan işlemler ve puan ekranda gösterilir.
        Fark daha fazla ise bilgi mesajı verilir.
        """
        if self.game_manager.calculate(rsayi(50_000, 100_000)):
            self.ui.le_islemler.setText(self.game_manager.player.process)
            self.ui.statusbar.showMessage(
                f"{self.game_manager.player.name}: {round(self.game_manager.player.score)} puan")
        else:
            self.clear()
            self.ui.statusbar.showMessage(
                f"{self.game_manager.player.name}..", 30_000)


if __name__ == '__main__':
    import sys
    app = application(sys.argv)
    win = BirKelimeBirIslem()
    win.setFixedSize(win.width(), win.height())
    sys.exit(app.exec_())
