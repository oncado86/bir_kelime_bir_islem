package entity;

/**
 * NPC (Non-Player Character) varlık sınıfı.
 * 
 * @apiNote NPC bilgilerini tutar
 * @category Varlık Sınıfı
 */
public class Player {
    private String name;
    private float score;
    private String process;

    /**
     * Player varlık sınıfını parametresiz oluşturur
     */
    public Player() {
    }

    /**
     * Player varlık sınıfını parametrelerle oluşturur
     * 
     * @param name    -> NPC ismi (String)
     * @param score   -> NPC puanı (float)
     * @param process -> NPC işlem bilgisi (String)
     */
    public Player(String name, float score, String process) {
        this.name = name;
        this.score = score;
        this.process = process;
    }

    /**
     * NPC ismini verir
     * 
     * @return name -> NPC ismi (String)
     */
    public String getName() {
        return name;
    }

    /**
     * NPC ismini ayarlar
     * 
     * @param name -> NPC ismi (String)
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * NPC puanını verir
     * 
     * @return score -> NPC puanı (float)
     */
    public float getScore() {
        return score;
    }

    /**
     * NPC puanını ayarlar
     * 
     * @param score -> NPC puanı (float)
     */
    public void setScore(float score) {
        this.score = score;
    }

    /**
     * NPC'nin yaptığı işlemleri verir
     * 
     * @return process -> NPC işlemleri (String)
     */
    public String getProcess() {
        return process;
    }

    /**
     * NPC'nin yaptığı işlemleri ayarlar
     * 
     * @param process -> NPC işlemşeri (String)
     */
    public void setProcess(String process) {
        this.process = process;
    }

}
