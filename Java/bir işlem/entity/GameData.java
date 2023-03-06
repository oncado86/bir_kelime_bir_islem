package entity;

import java.util.ArrayList;
import java.util.List;

/**
 * Oyun verilerinin tutulduğu varlık sınıfı.
 * 
 * @apiNote Oyun verilerini tutar
 * @category Varlık Sınıfı
 */
public class GameData {
    private List<Integer> numberList;
    private int targetNumber;
    private List<String> npcNames;

    /**
     * GameData varlık sınıfını parametresiz oluşturur
     */
    public GameData() {
        numberList = new ArrayList<>();
        npcNames = new ArrayList<>();
        npcNames.add("Darth Maul");
        npcNames.add("Darth Vader");
        npcNames.add("Darth Sidious");
        npcNames.add("Darth Tyranus");
        npcNames.add("Darth Bane");
        npcNames.add("Darth Plagus");
    }

    /**
     * Hesaplarda kullanılacak sayıların listesini verir
     * 
     * @return numberList -> Sayı listesi (ArrayList[int])
     */
    public List<Integer> getNumberList() {
        return numberList;
    }

    /**
     * Hesaplarda kullanılmak üzere sayı listesine bir tam sayı ekler
     * 
     * @param number -> Tam sayı (int)
     */
    public void setNumberList(int number) {
        this.numberList.add(number);
    }

    /**
     * Hesaplamalar sonucu ulaşılmak istenen sayıyı verir
     * 
     * @return targetNumber -> Hedeflenen sayı (int)
     */
    public int getTargetNumber() {
        return targetNumber;
    }

    /**
     * Hesaplamalar sonucu ulaşılmak istenen sayıyı ayarlar
     * 
     * @param targetNumber -> Hedeflenen sayı (int)
     */
    public void setTargetNumber(int targetNumber) {
        this.targetNumber = targetNumber;
    }

    /**
     * MPC (Non-Player Character) isim listesini verir
     * 
     * @return npcNames -> NPC isimleri (ArrayList[String])
     */
    public List<String> getNpcNames() {
        return npcNames;
    }

}
