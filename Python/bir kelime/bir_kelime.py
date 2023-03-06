from PyQt5.QtWidgets import (
    QMainWindow as main_window,
    QApplication as application
)
from PyQt5.QtGui import (
    QStandardItemModel as standart_item_model,
    QStandardItem as standart_item
)
from business.Game.gameManager import GameManager
from ui.birkelime_birislem import Ui_MainWindow as ui_main_window


class BirKelime(ui_main_window, main_window):
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

    def init_ui(self):
        """Arayüzü ayarlar ve ekranda gösterir.
        """
        self.ui = ui_main_window()
        self.ui.setupUi(self)

        # ListView objesinin ayarlarnması
        self.txt_model = standart_item_model()
        self.txt_standart_item = standart_item
        self.ui.listView_kelimeler.setModel(self.txt_model)
        self.ui.listView_kelimeler.clicked.connect(self.list_click)

        # Butonlara tıklandığında ne yapacaklarının ayarlanması
        self.ui.btn_hepsini_temizle.clicked.connect(self.clear)
        self.ui.btn_rasgele_harf_uret.clicked.connect(self.fill_letters)
        self.ui.btn_kelime_bul.clicked.connect(self.find_words)
        self.ui.statusbar.showMessage(self.game_manager.player.name, 3_000)

        # LineEdit obje listesi
        self.line_edit_list = [
            self.ui.le_unlu_harf_1,
            self.ui.le_unlu_harf_2,
            self.ui.le_unlu_harf_3,
            self.ui.le_unlu_harf_4,
            self.ui.le_unlu_harf_5,
            self.ui.le_unlu_harf_6,
            self.ui.le_unlu_harf_7,
            self.ui.le_unlu_harf_8,
            self.ui.le_unlu_harf_9,
            self.ui.le_unlu_harf_10,
            self.ui.le_unsuz_harf_1,
            self.ui.le_unsuz_harf_2,
            self.ui.le_unsuz_harf_3,
            self.ui.le_unsuz_harf_4,
            self.ui.le_unsuz_harf_5,
            self.ui.le_unsuz_harf_6,
            self.ui.le_unsuz_harf_7,
            self.ui.le_unsuz_harf_8,
            self.ui.le_unsuz_harf_9,
            self.ui.le_unsuz_harf_10
        ]

        self.fill_letters()
        self.show()

    def fill_letters(self):
        """Ekranı temizler ve hesaplamalarda kullanılacak sayıları ekranda gösterir
        """
        self.clear()
        self.line_edit_font_defaut_size()
        self.game_manager.create_letters()

        unlu_harfler = self.game_manager.game_data.letters[:10]
        lineedit_unluler = self.line_edit_list[:10]
        unsuz_harfler = self.game_manager.game_data.letters[10:]
        lineedit_unsuzler = self.line_edit_list[10:]

        for index in range(10):
            lineedit_unluler[index].setText(unlu_harfler[index])
            lineedit_unsuzler[index].setText(unsuz_harfler[index])

        self.ui.btn_kelime_bul.setEnabled(True)
        self.ui.btn_hepsini_temizle.setEnabled(True)
        self.txt_model.clear()
        self.ui.statusbar.showMessage(self.game_manager.player.name, 3_000)

    def clear(self):
        """Ekrandaki bilgileri temizler ve Hesaplama & Temizleme Butonlarını pasifleştirir.
        """
        for le in self.line_edit_list:
            le.clear()

        self.ui.statusbar.clearMessage()
        self.ui.btn_hepsini_temizle.setEnabled(False)
        self.ui.btn_kelime_bul.setEnabled(False)
        self.game_manager.choice_npc()
        self.txt_model.clear()

    def find_words(self):
        self.game_manager.player.finded_words.clear()
        self.game_manager.player.score = 0
        self.game_manager.process()

        self.txt_model.clear()

        for word in self.game_manager.player.finded_words:
            self.txt_model.appendRow(self.txt_standart_item(word))

        info = f"{self.game_manager.player.name}: {len(self.game_manager.player.finded_words):,} kelime; {self.game_manager.player.score:,} puan".replace(
            ",", ".")
        self.ui.statusbar.clearMessage()
        self.ui.statusbar.showMessage(info)

    def line_edit_font_defaut_size(self):
        """LineEdit objelerinin font ayarlarını varsayılan yapar"""
        for le in self.line_edit_list:
            font = le.font()
            font.setPointSize(13)
            font.setBold(False)
            le.setFont(font)

    def list_click(self):
        """Listeden bir veri seçildiğinde, seçilen kelimede kullanılan harfleri vurgular"""
        self.line_edit_font_defaut_size()
        word = str(self.ui.listView_kelimeler.currentIndex().data())
        word_letter = [i for i in word]
        for le in self.line_edit_list:
            if le.text() in word_letter:
                font = le.font()
                font.setPointSize(25)
                font.setBold(True)
                le.setFont(font)
                word_letter.remove(le.text())


if __name__ == "__main__":
    import sys
    app = application(sys.argv)
    win = BirKelime()
    win.setFixedSize(win.width(), win.height())
    sys.exit(app.exec_())
