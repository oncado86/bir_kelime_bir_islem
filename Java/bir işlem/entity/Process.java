package entity;

import java.util.ArrayList;
import java.util.List;

/**
 * Hesaplama verilerinin tutulduğu varlık sınıfı.
 * 
 * @apiNote Hesaplama verilerin tutar
 * @category Varlık Sınıfı
 */
public class Process {
    private float sonuc;
    private String cikti;
    private List<String> islemler;

    /**
     * Hesaplama varlık sınıfını parametresiz oluşturur
     */
    public Process() {
        islemler = new ArrayList<>();
        islemler.add("+");
        islemler.add("-");
        islemler.add("*");
        islemler.add("/");
    }

    /**
     * Hesaplamalarda elde edilen sonuç bilgisini geri verir
     * 
     * @return sonuc -> İşlem sonucu (float)
     */
    public float getSonuc() {
        return sonuc;
    }

    /**
     * Hesaplamalarda elde edilen sonuç bilgisini ayarlar
     * 
     * @param sonuc -> sonuç (float)
     */
    public void setSonuc(float sonuc) {
        this.sonuc = sonuc;
    }

    /**
     * Hesaplamaların matematiksel ifadesini geri verir
     * 
     * @return cikti -> İşlemler (String)
     */
    public String getCikti() {
        return cikti;
    }

    /**
     * Hesaplamaların matematiksel ifadesini ayarlar
     * 
     * @param cikti -> İşlemler (String)
     */
    public void setCikti(String cikti) {
        this.cikti = cikti;
    }

    /**
     * Hesaplamalarda kullanılacak dört işlemi geri verir
     * 
     * @return islemler -> Dört işlem (ArrayList[String])
     */
    public List<String> getDortIslem() {
        return islemler;
    }

}
