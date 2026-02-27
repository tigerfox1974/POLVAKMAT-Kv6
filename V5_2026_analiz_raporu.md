# POLVAK Teklif Hazırlama Sistemi V5 2026 — Kapsamlı Analiz Raporu

> **Dosya:** `maliyet_hesaplaV5 2026.html`  
> **Toplam Satır:** 517  
> **Teknoloji:** HTML5 + CSS3 + Vanilla JavaScript (Tek dosya — Single Page Application)  
> **Harici Bağımlılık:** FontAwesome 6.0.0 (CDN)  
> **Analiz Tarihi:** 27 Şubat 2026

---

## 1. GENEL BAKIŞ

Bu dosya, **Kıbrıs Türk Polis Güçlendirme Vakfı (POLVAK)** adına yangın eğitimi hizmetleri için **maliyet hesaplaması** yapan ve **yazdırılabilir teklif formu** üreten tarayıcı tabanlı bir uygulamadır. Tüm HTML, CSS ve JavaScript tek bir `.html` dosyasında toplanmıştır.

---

## 2. EKRAN YAPISI (LAYOUT)

Uygulama **Split View (Bölünmüş Görünüm)** düzenindedir:

```
┌─────────────────────────────────────────────────────┐
│                  .main-container                     │
│  ┌──────────────┐   ┌────────────────────────────┐  │
│  │  SOL PANEL   │   │        SAĞ PANEL           │  │
│  │  (input-     │   │     (preview-panel)         │  │
│  │   panel)     │   │                             │  │
│  │              │   │  ┌──────────────────────┐   │  │
│  │ • Kurum Adı  │   │  │    POLVAK LOGO       │   │  │
│  │ • Asgari Üc. │   │  │ Yangın Eğitimi       │   │  │
│  │ • İşletme T. │   │  │ Teklif Formu          │   │  │
│  │ • Otel Sınıfı│   │  ├──────────────────────┤   │  │
│  │ • Personel S.│   │  │ Sayın: XXX Yetkilisi │   │  │
│  │ • Paket Seç. │   │  │ Tarih: XX.XX.XXXX    │   │  │
│  │ • Sertifika  │   │  ├──────────────────────┤   │  │
│  │   (koşullu)  │   │  │  HIZMET TABLOSU      │   │  │
│  │              │   │  │  ..................... │   │  │
│  │ [Hesapla]    │   │  │  GENEL TOPLAM: XX TL  │   │  │
│  │ [Yazdır]     │   │  ├──────────────────────┤   │  │
│  │              │   │  │ İmza Alanları         │   │  │
│  └──────────────┘   │  └──────────────────────┘   │  │
│                      └────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

- **Sol Panel (flex: 0.8):** Veri giriş formu.
- **Sağ Panel (flex: 1.2):** Canlı teklif formu önizlemesi (yazdırılacak alan).

---

## 3. TÜM FORM ALANLARI (INPUT FIELDS)

| # | Alan Adı | HTML ID | Tip | Varsayılan Değer | Açıklama |
|---|----------|---------|-----|-------------------|----------|
| 1 | Kurum / İşletme Adı | `kurumAdi` | `text` | *(boş)* | Teklif verilen kurumun adı |
| 2 | Brüt Asgari Ücret (TL) | `asgariUcret` | `number` | `60618` | 2026 yılı brüt asgari ücreti |
| 3 | İşletme Türü | `isletmeTuru` | `select` | `otel` | "Otel / Turistik Tesis" veya "Diğer İşletmeler" |
| 4 | Otel Sınıfı | `otelSinifi` | `select` | `1` | 1-5 yıldız arası otel kategorisi |
| 5 | Personel Sayısı | `personelSayisi` | `number` | `10` | Eğitim alacak toplam personel |
| 6 | Paket Seçimi | `paketSecimi` | `select` | `1` | 4 farklı hizmet paketi |
| 7 | Sertifika Alacak Kişi Sayısı | `mudahaleSayisi` | `number` | `5` | Sadece Paket 4'te görünür |

---

## 4. TÜM BUTONLAR VE İŞLEVLERİ

| # | Buton | CSS Sınıfı | İkon | Tetiklediği İşlem | Açıklama |
|---|-------|-----------|------|-------------------|----------|
| 1 | **Hesapla** | `btn btn-calc` (Yeşil `#27ae60`) | `fa-sync-alt` | `hesapla()` | Girilen verilere göre maliyet tablosunu hesaplar ve sağ paneli günceller |
| 2 | **Teklif Yazdır** | `btn btn-print` (Lacivert `#002366`) | `fa-print` | `window.print()` | Tarayıcının yazdırma diyaloğunu açar; sadece teklif formu basılır |

---

## 5. SELECT (AÇILIR LİSTE) SEÇENEKLERİ

### 5.1 İşletme Türü (`isletmeTuru`)
| Değer | Görünen Metin |
|-------|---------------|
| `otel` | Otel / Turistik Tesis |
| `diger` | Diğer İşletmeler (Küçük İşletme/Kurum) |

### 5.2 Otel Sınıfı (`otelSinifi`) — Koşullu görünür, sadece İşletme Türü = `otel` ise
| Değer | Görünen Metin |
|-------|---------------|
| `1` | 1 Yıldız / Bungalov |
| `2` | 2 Yıldız |
| `3` | 3 Yıldız / Özel Belgeli / 2. Snf TK |
| `4` | 4 Yıldız / Butik Otel |
| `5` | 5 Yıldız / 1. Sınıf TK |

### 5.3 Paket Seçimi (`paketSecimi`)
| Değer | Görünen Metin | İçerik |
|-------|---------------|--------|
| `1` | Paket 1 (Temel Eğitim) | Sabit ücret + Personel belge ücreti |
| `2` | Paket 2 (Tatbikat) | Paket 1 + Tatbikat ücreti (1 asgari ücret) |
| `3` | Paket 3 (Denetim) | Sadece denetim ve raporlama ücreti |
| `4` | Paket 4 (Full + Sertifika) | Tümü + sertifika maliyeti - %35 indirim |

---

## 6. JAVASCRIPT FONKSİYONLARI

| # | Fonksiyon | Tetikleyen | Görevi |
|---|-----------|------------|--------|
| 1 | `toggleOtelSecenekleri()` | `isletmeTuru` select `onchange` | İşletme türü "otel" ise Otel Sınıfı alanını gösterir, değilse gizler |
| 2 | `toggleSertifika()` | `paketSecimi` select `onchange` | Paket 4 seçildiğinde "Sertifika Alacak Kişi Sayısı" alanını gösterir, değilse gizler |
| 3 | `formatTL(money)` | Dahili | Sayıları Türk Lirası formatında biçimlendirir (örn: `12.345,67 TL`) |
| 4 | `hesapla()` | Hesapla butonu `onclick` | **Ana hesaplama fonksiyonu** — tüm girdileri okur, oranları belirler, maliyet tablosunu oluşturur |

### 6.1 `hesapla()` Fonksiyonu Detaylı Akış:
```
1. Girdi okuma (kurumAdi, asgariUcret, isletmeTuru, personelSayisi, paket)
2. İşletme türüne göre oran seçimi (otel → yıldız bazlı / diğer → sabit oranlar)
3. Temel hesaplamalar:
   • sabitUcret = asgariUcret × oran.sabit
   • belgeUcreti = personelSayisi × (asgariUcret × oran.kisi)
   • p1_toplam  = sabitUcret + belgeUcreti
   • p3_toplam  = asgariUcret × oran.denetim
4. Paket'e göre tablo satırları ve final toplam oluşturma
5. DOM güncelleme (kalemlerTablosu innerHTML + outToplam)
```

---

## 7. ORAN / KATSAYI TABLOSU

### 7.1 Otel Oranları (`otelOranlar`)
| Yıldız | Sabit Oran | Kişi Başı Oran | Denetim Oranı |
|--------|-----------|----------------|---------------|
| 1 ★ | 0.10 | 0.010 | 0.60 |
| 2 ★★ | 0.10 | 0.011 | 0.65 |
| 3 ★★★ | 0.15 | 0.012 | 0.70 |
| 4 ★★★★ | 0.20 | 0.013 | 0.75 |
| 5 ★★★★★ | 0.25 | 0.015 | 0.80 |

### 7.2 Diğer İşletme Oranları (`digerOranlar`)
| Sabit Oran | Kişi Başı Oran | Denetim Oranı |
|-----------|----------------|---------------|
| 0.10 | 0.010 | 0.60 |

---

## 8. PAKET BAZLI HESAPLAMA DETAYLARI

### Paket 1 — Temel Eğitim
```
Tesis Sabit Ücreti       = asgariUcret × sabitOran
Personel Belge Ücreti    = personelSayısı × asgariUcret × kişiOranı
────────────────────────────────────────────────
TOPLAM                   = Sabit Ücret + Belge Ücreti
```

### Paket 2 — Tatbikat
```
Paket 1 Toplamı          = (üstteki hesap)
Tatbikat Ücreti          = 1 × asgariUcret
────────────────────────────────────────────────
TOPLAM                   = Paket 1 + Tatbikat
```

### Paket 3 — Denetim
```
Denetim ve Raporlama     = asgariUcret × denetimOranı
────────────────────────────────────────────────
TOPLAM                   = Denetim Ücreti
```

### Paket 4 — Full + Sertifika (%35 İndirimli)
```
Paket 1 (Temel Eğitim)          = sabitÜcret + belgeÜcreti
Paket 2 (Tatbikat Farkı)        = asgariUcret
Paket 3 (Denetim & Raporlama)   = asgariUcret × denetimOranı
Sertifikalı Personel Maliyeti    = sertifikaKişi × asgariUcret × 0.10
────────────────────────────────────────────────
Ara Toplam                       = Tümünün toplamı
Kampanya İndirimi                = Ara Toplam × %35
────────────────────────────────────────────────
GENEL TOPLAM                     = Ara Toplam - İndirim
```

---

## 9. ÖRNEK HESAPLAMA (Varsayılan Değerlerle)

**Girdi:** Brüt Asgari Ücret = 60.618 TL | 1 Yıldız Otel | 10 Personel | Paket 4 | 5 Sertifika

| Kalem | Hesaplama | Tutar |
|-------|-----------|-------|
| Sabit Ücret | 60.618 × 0.10 | 6.061,80 TL |
| Belge Ücreti | 10 × 60.618 × 0.01 | 6.061,80 TL |
| **Paket 1 Toplamı** | 6.061,80 + 6.061,80 | **12.123,60 TL** |
| Tatbikat (Paket 2 Farkı) | 60.618 | 60.618,00 TL |
| Denetim (Paket 3) | 60.618 × 0.60 | 36.370,80 TL |
| Sertifika (5 kişi) | 5 × 60.618 × 0.10 | 30.309,00 TL |
| **Ara Toplam** | | **139.421,40 TL** |
| İndirim (%35) | 139.421,40 × 0.35 | -48.797,49 TL |
| **GENEL TOPLAM** | | **90.623,91 TL** |

---

## 10. TEKLİF FORMU ÖNİZLEME PANELİ (Sağ Taraf) BİLEŞENLERİ

| # | Bileşen | HTML ID/Class | Açıklama |
|---|---------|---------------|----------|
| 1 | Logo | `.logo-img` | `POLVAK MAX Logo.png` dosyasını yükler; bulunamazsa `onerror` ile alert gösterir |
| 2 | Başlık | `.header h1` | "Yangın Eğitimi Teklif Formu" |
| 3 | Müşteri Bilgisi | `.client-info` | Kurum adı (`outKurumAdi`), Tarih (`tarih`) ve açıklama metni |
| 4 | Hizmet Tablosu | `#kalemlerTablosu` | Dinamik satırlarla hesaplama kalemleri |
| 5 | Genel Toplam | `#outToplam` | Kırmızı renkte (`#c0392b`) vurgulu toplam tutar |
| 6 | Footer | `.footer` | Yasal uyarı metni |
| 7 | İmza Alanları | `.signature-area` | "POLVAK Yetkilisi" ve "Kurum Yetkilisi" imza kutuları |

---

## 11. MODALLER VE POPUP'LAR

| # | Tür | Tetikleyen | Açıklama |
|---|-----|------------|----------|
| 1 | `alert()` (Tarayıcı Popup) | Logo yükleme hatası (`onerror`) | "Logo dosyası bulunamadı! Lütfen POLVAK MAX Logo.png dosyasını klasöre ekleyin." mesajı gösterir |

> ⚠️ **Not:** Dosyada özel hazırlanmış modal (overlay/dialog) bulunmamaktadır. Tek popup, logo bulunamadığında tetiklenen tarayıcı alert'idir.

---

## 12. KOŞULLU GÖRÜNÜRLÜK (CONDITIONAL UI)

| Koşul | Etkilenen Alan | Davranış |
|-------|---------------|----------|
| İşletme Türü = `otel` | `#otelSinifiGroup` | **Görünür** (display: block) |
| İşletme Türü = `diger` | `#otelSinifiGroup` | **Gizli** (display: none) |
| Paket Seçimi = `4` | `#sertifikaGroup` | **Görünür** (display: block) |
| Paket Seçimi ≠ `4` | `#sertifikaGroup` | **Gizli** (display: none / `.hidden` class) |

---

## 13. CSS TASARIM ÖZELLİKLERİ

| Özellik | Detay |
|---------|-------|
| **Ana Renk Paleti** | Lacivert `#002366`, Yeşil `#27ae60`, Kırmızı `#c0392b`, Gri `#f0f2f5` |
| **Font Ailesi** | Segoe UI, Tahoma, Geneva, Verdana, sans-serif |
| **Kutu Gölgeleri** | `0 4px 15px rgba(0,0,0,0.1)` — Kartlara derinlik efekti |
| **Border Radius** | 12px (paneller), 6px (input/buton) |
| **Geçiş Efektleri** | `transition: 0.2s–0.3s` (buton hover, input focus) |
| **İndirim Satırı** | Yeşil metin + açık yeşil arka plan (`#f9fff9`) |
| **Toplam Satırı** | Kalın, büyük font (18px), kırmızı renk, çift çizgi üst kenarlık |

---

## 14. YAZDIRMA (PRINT) DAVRANIŞI

`@media print` kuralları ile yazdırma sırasında:

| Eleman | Davranış |
|--------|----------|
| `.input-panel` | **Gizlenir** — Sol panel basılmaz |
| `.btn-group` | **Gizlenir** — Butonlar basılmaz |
| `.preview-panel` | Tam genişlikte, gölge/kenarlık yok |
| `body` | Beyaz arka plan, sıfır margin/padding |
| Renk baskısı | `-webkit-print-color-adjust: exact` ile korunur |

**Sonuç:** Yazdırdığınızda sadece profesyonel teklif formu kağıda dökülür.

---

## 15. RESPONSIVE (MOBİL UYUM) DAVRANIŞI

| Ekran Genişliği | Davranış |
|-----------------|----------|
| > 768px | Yan yana flexbox düzeni (sol panel + sağ panel) |
| ≤ 768px | Dikey yığın düzeni (`flex-direction: column`) |

---

## 16. HARİCİ BAĞIMLILIKLAR

| Kaynak | URL | Amaç |
|--------|-----|------|
| FontAwesome 6.0.0 | `cdnjs.cloudflare.com/...` | İkonlar (hesap makinesi, yazdır, bilgi, yenile) |
| `POLVAK LOGO.png` | Yerel dosya | Favicon olarak kullanılır |
| `POLVAK MAX Logo.png` | Yerel dosya | Teklif formundaki kurum logosu |

---

## 17. SAYFA YÜKLENDİĞİNDE ÇALIŞAN KOD

```javascript
document.getElementById("tarih").innerText = new Date().toLocaleDateString('tr-TR');
```
Sayfa açıldığında otomatik olarak günün tarihini Türkçe formatla (gg.aa.yyyy) teklif formuna yazar.

---

## 18. V4'TEN V5'E GEÇİŞTE FARKLAR

V4 analiz raporuyla karşılaştırıldığında V5 2026 sürümünde:

| Özellik | V4 | V5 2026 |
|---------|-----|----|
| Asgari Ücret Varsayılanı | Eski değer | **60.618 TL** (2026 güncellemesi) |
| Dosya Adı | maliyet_hesaplaV4.html | maliyet_hesaplaV5 2026.html |
| Logo Dosyası | Aynı | Aynı (POLVAK MAX Logo.png) |
| Hesaplama Mantığı | Aynı | Aynı (değişiklik yok) |

> **Sonuç:** V5, V4'ün 2026 yılı asgari ücret güncellemesiyle yeniden adlandırılmış versiyonudur. Fonksiyonel fark yoktur.

---

## 19. TESPİT EDİLEN EKSİKLİKLER VE İYİLEŞTİRME ÖNERİLERİ

| # | Konu | Açıklama | Öneri |
|---|------|----------|-------|
| 1 | **Form Validasyonu Yok** | Asgari ücret veya personel sayısı negatif/boş girilirse hata kontrolü yapılmıyor | `hesapla()` içine input doğrulama eklenebilir |
| 2 | **Modal Yok** | Kullanıcıya bilgi/onay göstermek için sadece tarayıcı alert kullanılıyor | Özel modal bileşeni eklenebilir |
| 3 | **Kaydetme/Geçmiş Yok** | Hesaplanan teklifler saklanmıyor | LocalStorage veya backend ile geçmiş teklif kaydı eklenebilir |
| 4 | **PDF Dışa Aktarma Yok** | Teklif sadece tarayıcı print ile yazdırılabiliyor | html2pdf.js gibi bir kütüphane ile doğrudan PDF üretilebilir |
| 5 | **Tek Dosya Yapısı** | HTML, CSS ve JS tek dosyada birleşik | Modüler yapıya geçiş (ayrı dosyalar) önerilir |
| 6 | **KDV/Vergi Hesabı Yok** | Fiyatlar vergisiz gösterilmekte | İsteğe bağlı KDV satırı eklenebilir |
| 7 | **Logo Hata Yönetimi** | `onerror` ile alert gösteriliyor ancak logo yerine alternatif metin/icon gösterilmiyor | Fallback logo veya SVG placeholder eklenebilir |

---

## 20. DOSYA İSTATİSTİKLERİ

| Metrik | Değer |
|--------|-------|
| Toplam Satır | 517 |
| HTML Satır | ~140 |
| CSS Satır | ~275 |
| JavaScript Satır | ~90 |
| Fonksiyon Sayısı | 4 (`toggleOtelSecenekleri`, `toggleSertifika`, `formatTL`, `hesapla`) |
| DOM Manipülasyonu | 6 getElementById + innerHTML/innerText |
| Event Handler | 3 (`onclick` × 2, `onchange` × 2, `onerror` × 1) |
| Harici Bağımlılık | 1 (FontAwesome CDN) |
| Yerel Dosya Bağımlılığı | 2 (POLVAK LOGO.png, POLVAK MAX Logo.png) |

---

## 21. SON YAPILAN DEĞİŞİKLİK (27 Şubat 2026)

`index.html` dosyasında, **PDF/yazdırma çıktısı** için banka hesapları bölümünün başlık tipografisi ve başlık-kart aralığı güncellenmiştir.

### 21.1 Uygulanan Güncelleme
- `@media print` altında `.bank-accounts h3` yazı boyutu artırıldı (**17px**).
- `@media print` altında `.bank-accounts h4` yazı boyutu artırıldı (**14px**).
- Başlık ile kartlar arasındaki görsel boşluk artırıldı (`h4` alt marjı **5mm**).
- `@media print` altında `.bank-cards` için üst boşluk düzenlendi (`margin-top: 0`) ve yeni başlık boşluğu korunacak şekilde hizalandı.

### 21.2 Etki Analizi
- Değişiklik yalnızca yazdırma/PDF görünümünü etkiler; ekran (normal görüntü) düzeni ve hesaplama mantığı etkilenmez.
- Amaç: PDF çıktısında başlık okunabilirliğini artırmak ve başlık-kart geçişini daha dengeli hale getirmek.

---

*Bu rapor, `maliyet_hesaplaV5 2026.html` dosyasının tüm yapısını, fonksiyonlarını, butonlarını, koşullu davranışlarını ve hesaplama mantığını kapsamaktadır.*
