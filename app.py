import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="POLVAK Eğitim Maliyet Hesaplayıcı", layout="centered")

# Başlık
st.title("🔥 Yangın Eğitimi Maliyet Hesaplama")
st.markdown("---")

# --- 1. GİRDİLER ---
st.header("1. Temel Bilgiler")

# Asgari Ücret
asgari_ucret = st.number_input("Brüt Asgari Ücret (TL)", value=35180.0, step=100.0)

# İşletme Türü Seçimi
isletme_turu = st.radio("İşletme Türü", ("Otel / Turistik Tesis", "Diğer İşletmeler (Küçük İşletme)"))

# Otel Sınıfı Seçimi
otel_sinifi = None
oranlar = {}

if isletme_turu == "Otel / Turistik Tesis":
    otel_secim = st.selectbox(
        "Otel Sınıfı",
        [
            "1 Yıldız / Bungalov",
            "2 Yıldız",
            "3 Yıldız / Özel Belgeli / 2. Sınıf T.K.",
            "4 Yıldız / Butik Otel",
            "5 Yıldız / 1. Sınıf T.K."
        ]
    )
    
    # Otel Oranları
    if "1 Yıldız" in otel_secim:
        oranlar = {"sabit": 0.10, "kisi_basi": 0.01, "denetim": 0.60}
    elif "2 Yıldız" in otel_secim:
        oranlar = {"sabit": 0.10, "kisi_basi": 0.011, "denetim": 0.65}
    elif "3 Yıldız" in otel_secim:
        oranlar = {"sabit": 0.15, "kisi_basi": 0.012, "denetim": 0.70}
    elif "4 Yıldız" in otel_secim:
        oranlar = {"sabit": 0.20, "kisi_basi": 0.013, "denetim": 0.75}
    elif "5 Yıldız" in otel_secim:
        oranlar = {"sabit": 0.25, "kisi_basi": 0.015, "denetim": 0.80}

else:
    # Küçük İşletme Oranları
    oranlar = {"sabit": 0.10, "kisi_basi": 0.01, "denetim": 0.60}

# Personel Bilgileri
col1, col2 = st.columns(2)
with col1:
    toplam_personel = st.number_input("Toplam Personel Sayısı (Paket 1 İçin)", min_value=1, value=10, step=1)
with col2:
    paket_secimi = st.selectbox("Alınacak Paket", ["Paket 1 (Temel)", "Paket 2 (Tatbikat)", "Paket 3 (Denetim)", "Paket 4 (Full + Sertifika)"])

# İlk Müdahale Ekibi
ilk_mudahale_sayisi = 0
if paket_secimi == "Paket 4 (Full + Sertifika)":
    st.info("Paket 4 seçildiği için Sertifikalı Personel sayısını giriniz.")
    ilk_mudahale_sayisi = st.number_input("İlk Müdahale Ekibi Sayısı (Sertifika Alacaklar)", min_value=1, value=5)

# --- 2. HESAPLAMA MOTORU ---

maliyet_p1 = (asgari_ucret * oranlar["sabit"]) + (toplam_personel * asgari_ucret * oranlar["kisi_basi"])
maliyet_p3 = asgari_ucret * oranlar["denetim"]
maliyet_sertifika = ilk_mudahale_sayisi * (asgari_ucret * 0.10)

final_tutar = 0.0
indirim_tutari = 0.0
aciklama = ""

if paket_secimi == "Paket 1 (Temel)":
    final_tutar = maliyet_p1
    aciklama = "Temel Yangın Eğitimi"

elif paket_secimi == "Paket 2 (Tatbikat)":
    final_tutar = maliyet_p1 + asgari_ucret
    aciklama = "Paket 1 + Tatbikat (1 Asgari Ücret Farkı)"

elif paket_secimi == "Paket 3 (Denetim)":
    final_tutar = maliyet_p3
    aciklama = "Sadece Denetim ve Raporlama"

elif paket_secimi == "Paket 4 (Full + Sertifika)":
    ham_toplam = maliyet_p1 + asgari_ucret + maliyet_p3 + maliyet_sertifika
    indirim_orani = 0.35
    indirim_tutari = ham_toplam * indirim_orani
    final_tutar = ham_toplam - indirim_tutari
    aciklama = f"Toplam: {ham_toplam:,.2f} TL üzerinden %35 İndirim uygulandı."

# --- 3. SONUÇ EKRANI ---
st.markdown("---")
st.header("Sonuçlar")

if paket_secimi == "Paket 4 (Full + Sertifika)":
    col_a, col_b = st.columns(2)
    col_a.metric("İndirimsiz Toplam", f"{final_tutar + indirim_tutari:,.2f} TL")
    col_b.metric("İndirim Tutarı (%35)", f"{indirim_tutari:,.2f} TL", delta_color="inverse")

st.success(f"**ÖDENECEK NET TUTAR:** {final_tutar:,.2f} TL")
st.caption(f"Hesaplama Detayı: {aciklama}")
