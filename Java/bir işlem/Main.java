import business.GameManager;

public class Main {
    public static void main(String[] args) {

        GameManager gameManager = new GameManager();

        System.out.println("\nKullanılacak sayılar: "+ gameManager.gameData().getNumberList().toString().replace("[", "").replace("]", ""));
        System.out.println("Hedef: " + gameManager.gameData().getTargetNumber());
        System.out.println("\n" + gameManager.player().getName() + ";");

        /**
         * Sonsuz döngü oluşmaması için 10.000'e kadar rasgele sayıda
         * hesaplamaları yapar ve sonucu kullanıcıya bildirir.
         * Eğer bulunan sonuç, ulaşılmak istenen sayı ile +-9 fark var ise yapılan
         * işlemler ve puan ekranda gösterilir.
         * Fark daha fazla ise bilgi mesajı verilir.
         */
        gameManager.calculate(10000);
        if (gameManager.getIsFined()) {
            System.out.println(gameManager.player().getProcess());
            System.out.println(gameManager.player().getScore());
        } else {
            System.out.println("..bulamadım..");
        }

    }
}
