# POLVAKMATİK Program Yapısı Analiz Raporu

## 1. Genel Bakış
**POLVAKMATİK**, yangın eğitimi, tatbikat ve denetim hizmetleri için maliyet hesaplaması yapan ve teklif oluşturan bir yazılımdır. Proje klasörü içerisinde aynı iş mantığını yürüten iki farklı uygulama yapısı bulunmaktadır:
1.  **Python (Streamlit)** tabanlı bir veri uygulaması.
2.  **HTML/JS** tabanlı, tarayıcı üzerinde çalışan ve çıktı almaya uygun bir web arayüzü.

## 2. Dosya Yapısı ve Amaçları

| Dosya Adı | Tür | Açıklama |
| :--- | :--- | :--- |
| `app.py` | Python | Streamlit kütüphanesi kullanılarak yazılmış backend/frontend birleşik hesaplama uygulaması. |
| `maliyet_hesaplaV4.html` | HTML | HTML, CSS ve JavaScript içeren, kullanıcı dostu arayüze sahip, yazdırılabilir teklif formu oluşturan tek sayfalık uygulama. (En güncel sürüm) |
| `maliyet_hesaplaV3.html` | HTML | HTML arayüzünün önceki versiyonu. |
| `requirements.txt` | Metin | Python projesi için gerekli kütüphaneleri listeler (Sadece `streamlit`). |
| `POLVAK LOGO.png` | Resim | Teklif formunda kullanılan kurum logosu. |

## 3. Teknik Analiz

### A. Python Uygulaması (`app.py`)
*   **Teknoloji:** Python, Streamlit.
*   **Mantık:**
    *   Kullanıcıdan asgari ücret, işletme türü, otel sınıfı, personel sayısı ve paket seçimi gibi girdileri alır.
    *   İşletme türüne göre (Otel veya Diğer) ve otel yıldız sayısına göre katsayılar (`oranlar`) belirlenir.
    *   **Paket 1, 2, 3 ve 4** için ayrı maliyet hesaplamaları yapılır.
    *   Paket 4 seçiminde **%35 indirim** uygulanır.
*   **Kullanım:** Hızlı prototipleme ve veri girişi/hesaplama için uygundur. Arayüz standart Streamlit bileşenlerinden oluşur.

### B. HTML/JS Uygulaması (`maliyet_hesaplaV4.html`)
*   **Teknoloji:** HTML5, CSS3, Vanilla JavaScript.
*   **Kütüphaneler:** FontAwesome (CDN üzerinden ikonlar için).
*   **Arayüz Tasarımı:**
    *   **Split View (Bölünmüş Görünüm):** Sol tarafta veri giriş paneli, sağ tarafta dinamik olarak güncellenen "Teklif Formu" önizlemesi bulunur.
    *   **Responsive:** Mobil ve masaüstü uyumludur.
    *   **Yazdırma (Print) Özelliği:** `@media print` CSS kuralları sayesinde, yazdır dendiğinde sadece sağ taraftaki resmi teklif formu kağıda dökülür, butonlar ve giriş alanları gizlenir.
*   **Mantık:**
    *   JavaScript tarafında `otelOranlar` ve `digerOranlar` objeleri ile katsayılar tutulur.
    *   `hesapla()` fonksiyonu DOM üzerinden verileri alır, hesaplar ve HTML tablosunu günceller.
    *   Logo bulunamadığında kullanıcıyı uyaran hata yönetimi (`onerror`) mevcuttur.

## 4. Hesaplama Mantığı (Her iki yapıda da ortaktır)
Program aşağıdaki parametrelere göre fiyat çıkarır:
1.  **Sabit Ücret:** Asgari ücret * Sabit Oran (Otel yıldızına göre değişir).
2.  **Kişi Başı Belge Ücreti:** Personel Sayısı * Asgari Ücret * Kişi Başı Oran.
3.  **Denetim Ücreti:** Asgari ücret * Denetim Oranı.
4.  **Paketler:**
    *   **Paket 1:** Sabit Ücret + Belge Ücreti.
    *   **Paket 2:** Paket 1 + 1 Asgari Ücret (Tatbikat Farkı).
    *   **Paket 3:** Sadece Denetim Ücreti.
    *   **Paket 4:** Paket 1 + Paket 2 Farkı + Paket 3 + Sertifikalı Personel Maliyeti - %35 İndirim.

## 5. Sonuç
Proje, hem hızlı hesaplama (Python/Streamlit) hem de profesyonel teklif sunumu (HTML/JS) ihtiyaçlarını karşılayacak şekilde geliştirilmiştir. `maliyet_hesaplaV4.html` dosyası, son kullanıcıya sunulacak nihai ürün (teklif formu) için daha gelişmiş ve görsel olarak zengin bir çözümdür.
