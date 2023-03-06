package business;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import entity.GameData;
import entity.Player;
import entity.Process;

/**
 * Oyun ile ilgili metotların bulunduğu sınıf.
 * IGameManager arayüz sınıfını kullanır.
 *
 * @see IGameManager
 */
public class GameManager implements IGameManager {
    private GameData gameData;
    private Player player;
    private Random rsayi = new Random();
    private Process processEnty = new Process();
    private boolean isFined = false;

    public GameManager() {
        gameData = new GameData();
        player = new Player();
        createNumbers();
        choiceNpc();
    }

    /**
     * Hesaplamardan elde edilen sonucun istenilen aralıkta olma durumunu verir
     *
     * @return isFined -> boolean
     */
    public boolean getIsFined() {
        return isFined;
    }

    @Override
    public GameData gameData() {
        return gameData;
    }

    @Override
    public Player player() {
        return player;
    }

    @Override
    public void createNumbers() {
        gameData.getNumberList().clear();
        for (int i = 0; i < 5; i++) {
            gameData.setNumberList(rsayi.nextInt(9) + 1);
        }
        gameData.setNumberList((int) (Math.random() * 100));
        gameData.setTargetNumber((int) (Math.random() * 1000));
        if (gameData.getNumberList().get(5) < 10 || gameData.getTargetNumber() < 100) {
            createNumbers();
        }
    }

    @Override
    public void choiceNpc() {
        player.setProcess("");
        player.setScore(0);
        player.setName(gameData.getNpcNames().get(rsayi.nextInt(gameData.getNpcNames().size())));
    }

    @Override
    public boolean isFinished(float bulunanSonuc) {
        return ((gameData.getTargetNumber() - 9) <= bulunanSonuc && bulunanSonuc <= (gameData.getTargetNumber() + 9));
    }

    /**
     * İşlem sonucunu hesaplar
     *
     * @param gelenSonuc  -> Bir önceki adımda elde edilen net sonuç (float)
     * @param gelenSayi   -> Hesaplamaya dahil edilecek sayı (float)
     * @param gelensIslem -> Hesaplamada kullanılacak işlem (String)
     * @return sonuc -> Hesaplama sonucu (float)
     */
    private float findResult(float gelenSonuc, float gelenSayi, String gelensIslem) {
        float sonuc = 0;
        if ("+".equals(gelensIslem))
            sonuc = gelenSonuc + gelenSayi;
        if ("-".equals(gelensIslem))
            sonuc = gelenSonuc - gelenSayi;
        if ("*".equals(gelensIslem))
            sonuc = gelenSonuc * gelenSayi;
        if ("/".equals(gelensIslem))
            sonuc = gelenSonuc / gelenSayi;
        return sonuc;
    }

    @Override
    public void process(float gelenSonuc, float gelenSayi, String gelenCikti) {
        String islem = processEnty.getDortIslem().get(rsayi.nextInt(processEnty.getDortIslem().size()));

        /**
         * Çarpma ve bölme işlemine göre 1 etkisiz elemandır
         * Çarpma ya da bölme işlemiyle 1 sayısının kullanımasını engeller.
         */
        if (("*".equals(islem) || "/".equals(islem)) && gelenSayi == 1) {
            if (gelenSonuc == 1 && ("*".equals(islem) || "/".equals(islem))) {
                processEnty.setSonuc(gelenSonuc);
                processEnty.setCikti(gelenCikti);
            }
        } else if (gelenSonuc == 1 && ("*".equals(islem) || "/".equals(islem))) {
            if (("*".equals(islem) || "/".equals(islem)) && gelenSayi == 1) {
                processEnty.setSonuc(gelenSonuc);
                processEnty.setCikti(gelenCikti);
            }
        } else {
            processEnty.setSonuc(findResult(gelenSonuc, gelenSayi, islem));
            processEnty.setCikti(String.format("(%s %s %s)", gelenCikti, islem, (int) gelenSayi));
        }
    }

    /**
     * NPC verilerini ayarlar
     *
     * @param sonuc      -> İşlemler sonrasında elde edilen sonuç bilgisi
     * @param cikti      -> Hesaplamalarda kullanılan işlemler
     * @param numberList -> Hesaplamalarda kullanılan sayılar
     */
    private void setPlayerValues(float sonuc, String cikti, List<Float> numberList) {
        /**
         * Son hamlede hedefe ulaşmak için,
         * aradaki fark listede varsa ve kullanılmamışsa, hedeflenen sayıya ulaşılır
         */
        float fark = Math.abs(sonuc - gameData.getTargetNumber());
        for (float sayi : numberList) {
            if (fark == sayi) {
                if (sonuc > gameData.getTargetNumber()) {
                    sonuc -= fark;
                    cikti += String.format(" - %s) = %s", (int) fark, sonuc);
                }
                if (gameData.getTargetNumber() > sonuc) {
                    sonuc += fark;
                    cikti += String.format(" + %s) = %s", (int) fark, sonuc);
                }
                player.setProcess(cikti);
                player.setScore(100);
                break;
            } else {
                // istenilen sonuca ulaşılırsa, NPC (Non-Player Character)'nin puanı ve
                // matematiksel işlemler (işlem önceliğine uygun olarak) ekranda gösterilir.
                cikti += String.format(" = %s", sonuc);
                player.setProcess(cikti);
                // puan: ulaşışmak istenilen sayı ile hesaplanan sayı arasındaki farkın mutlak
                // değerinin 10 katı olarak hesaplanmaktadır.
                fark = 10 - Math.abs(sonuc - gameData.getTargetNumber());
                player.setScore(fark * 10);
                break;
            }
        }
    }

    @Override
    public void calculate(int tekrarSayisi) {
        List<Float> numberList = new ArrayList<>();
        /**
         * Sayı listesinden rasgele bir değer, sonuç olarak kabul edilerel işlemlere
         * başlanır.
         * Bu rasgele işlem adedince sayı listesinden sayılar alınır ve yine rasgele
         * işlemlere tabi tutulur.
         * Eğer istenilen sonuca ulaşılırsa döngü kırılır,
         * istenilen sonuca ulaşılamazsa sonsuz döngüye girilmemesi için kullanıcıya bir
         * bilgi mesajı verilir.
         */
        for (int i = 0; i < tekrarSayisi; i++) {
            numberList.clear();
            for (float number : gameData.getNumberList()) {
                numberList.add(number);
            }
            // listeden rasgele bir sayı sonuc olarak kabul edilir ve sayının tekrar
            // kullanılmaması için listeden çıkartılır.
            processEnty.setSonuc(numberList.get(rsayi.nextInt(5)));
            numberList.remove(numberList.indexOf(processEnty.getSonuc()));
            processEnty.setCikti("" + ((int) processEnty.getSonuc()));

            while (!numberList.isEmpty()) {
                // listeden rasgele bir sayı işleme tabi tutulmak için seçilir ve sayının tekrar
                // kullanılmaması için listeden çıkartılır.
                float sayi = numberList.get(rsayi.nextInt(numberList.size()));
                process(processEnty.getSonuc(), sayi, processEnty.getCikti());
                numberList.remove(numberList.indexOf((sayi)));

                if (isFinished(processEnty.getSonuc())) {
                    // eğer bulunan sonuç ile ulaşılmak istenen sayı arasında +-9 fark var ise döngü
                    // kırılır.
                    setPlayerValues(processEnty.getSonuc(), processEnty.getCikti(), numberList);
                    isFined = true;
                }
            }
        }

    }
}
