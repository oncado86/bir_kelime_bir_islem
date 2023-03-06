package business;

import entity.GameData;
import entity.Player;

/**
 * Oyun iş katmanı için kullanılacak operasyonların imzasını tutar
 * 
 * @category Business, Interface
 */
public interface IGameManager {
    /**
     * Oyun verilerinin tutulacağı varlık sınıfını verir.
     * 
     * @return gameData -> Oyun Verileri (GameData)
     * @see GameData
     */
    GameData gameData();

    /**
     * NPC (Non-Player Character) varlık sınıfını verir.
     * 
     * @return player -> NPC (Player)
     * @see Player
     */
    Player player();

    /**
     * Oyun içerisinde kullanılacak olan sayıların türetilmesini sağlar.
     * 
     * @apiNote 5 tane 1 basamaklı
     * @apiNote 1 tane 2 basamaklı
     * @apiNote 1 tane 3 basamaklı
     */
    void createNumbers();

    /**
     * Oyunu oynayacak NPC (Non-Player Character)'i türetir.
     */
    void choiceNpc();

    /**
     * Yapılan işlemler sonucunda ulaşılan sonucun, ulaşılmak istenen sonuç
     * aralığında olup olmadığını kontrol eder.
     * 
     * @param bulunanSonuc -> Hesaplamalar sonucu ulaşılan sonuç (float)
     * @return boolean -> bulunanSonuc istenilen aralıktaysa True, değilse False
     */
    boolean isFinished(float bulunanSonuc);

    /**
     * Tüm hesaplamaları rasgele olarak yapmaya yarar.
     * 
     * @param gelenSonuc -> Bir önceki adımda bulunmuş olan sonuç değeri (float)
     * @param gelenSayi  -> işleme tabi tutulacak sayı değeri (float)
     * @param gelenCikti -> daha önceki işlemlerin geçmişi (String)
     */
    void process(float gelenSonuc, float gelenSayi, String gelenCikti);

    /**
     * Rasgele üretilmiş sayıları, yine rasgele olarak işlemlere tabi tutup
     * istenilen sayıya ulaşmaya çalışır.
     * 
     * @param tekrarSayisi -> İşlemlerin kaç defa tekrarlanacağını (denemenin bir
     *                     seferde kaç defa yapılacağını) belirtir. (int)
     */
    void calculate(int tekrarSayisi);

}
