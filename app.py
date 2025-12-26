import streamlit as st
import time
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Untuk Kamu Sayang ❤️",
    page_icon="🌹",
    layout="centered"
)

# --- CSS SEDERHANA UNTUK TAMPILAN CANTIK --
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F5;
    }
    h1 {
        color: #D63384;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }
    p {
        font-size: 18px;
        color: #555;
    }
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# --- VARIABEL YANG HARUS KAMU GANTI ---
NAMA_DIA = "Nadia Sayang"  # Ganti dengan panggilan sayang dia
TANGGAL_JADIAN = datetime(2025, 12, 16) # Format: Tahun, Bulan, Tanggal
URL_FOTO_COVER = "https://cdn.discordapp.com/attachments/1424029736090472558/1453993479989362853/WhatsApp_Image_2025-12-26_at_13.07.44.jpeg?ex=694f7873&is=694e26f3&hm=ff5aef37f1bf2321d819518eb2a7c50fc039d18df262ab7386ea2e1416ac981f&" # Bisa ganti link foto kalian berdua
URL_LAGU = "https://open.spotify.com/embed/track/0z7jhodL97W88al5OI1zh1?utm_source=generator" # Link Embed Spotify (Opsional)

# --- FUNGSI HITUNG HARI ---
def hitung_waktu():
    sekarang = datetime.now()
    selisih = sekarang - TANGGAL_JADIAN
    hari = selisih.days
    return hari

# --- HALAMAN UTAMA ---
st.title(f"Hai, {NAMA_DIA}🌹")

# Tab Menu
tab1, tab2, tab3 = st.tabs(["🏠 Home", "💌 Surat", "📸 Galeri Kita"])

with tab1:
    st.image(URL_FOTO_COVER, caption="Kita Berdua ❤️", use_column_width=True)
    
    st.write("### Udah berapa lama kita bareng?")
    col1, col2, col3 = st.columns(3)
    with col2:
        hari = hitung_waktu()
        st.metric(label="Total Hari", value=f"{hari} Hari")
        st.caption(f"Sejak {TANGGAL_JADIAN.strftime('%d %B %Y')}")

    st.write("---")
    st.write("Coba tekan tombol di bawah ini:")
    if st.button("Pencet Aku Sayang"):
        st.balloons()
        time.sleep(1)
        st.success("Aku Sayang Banget Sama Kamu! ❤️❤️❤️")

with tab2:
    st.header("Surat Kecil Untukmu 📝")
    # Ganti isi surat di bawah ini
    isi_surat = """
    Sayang,
    
    Aku cuma mau bilang makasih udah nemenin aku sampai hari ini.
    Maaf ya kalau aplikasinya sederhana, tapi ini aku buat khusus buat kamu biar kamu tau
    betapa spesialnya kamu buat aku.
    
    Jangan lupa senyum hari ini ya!
    
    Love,
    Pacarmu
    """
    st.text_area("", value=isi_surat, height=250, disabled=True)
    
    # Musik (Opsional - Copy Embed Code dari Spotify)
    st.write("Dengerin lagu ini ya:")
    st.markdown(f'<iframe style="border-radius:12px" src="{https://open.spotify.com/embed/track/0z7jhodL97W88al5OI1zh1?utm_source=generator}" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>', unsafe_allow_html=True)

with tab3:
    st.header("Kenangan Kita 📸")
    st.write("Ini adalah momen-momen favoritku sama kamu.")
    
    # Ganti Link Gambar di bawah ini dengan link foto asli kalian
    # Tips: Upload foto ke imgur.com atau taruh file foto di folder yang sama dengan app.py
    col_a, col_b = st.columns(2)
    with col_a:
        st.image("https://cdn.discordapp.com/attachments/1424029736090472558/1453993479431651493/WhatsApp_Image_2025-12-26_at_13.07.44_1.jpeg?ex=694f7873&is=694e26f3&hm=7dfd4336997981d92761673eaa000e04944b2b872635cf6b5ab22828877206f8&", caption="Waktu kita jalan-jalan")
    with col_b:
        st.image("https://cdn.discordapp.com/attachments/1424029736090472558/1453993480819839069/WhatsApp_Image_2025-12-26_at_13.07.45_1.jpeg?ex=694f7873&is=694e26f3&hm=4d2538908ed0758e65898e70f135d48f70feec7679aa07567aab0f74cbe16203&", caption="Senyum kamu manis banget")
    with col_b:
        st.image("https://cdn.discordapp.com/attachments/1424029736090472558/1453993483793596446/WhatsApp_Image_2025-12-26_at_13.07.46.jpeg?ex=694f7874&is=694e26f4&hm=545b9ec2e60181b09e37a7e8fbb71a796160a3110b66b4c7c0466ed8a095699f&", caption="Mylovely Nadia")

    st.write("---")
    alasan = st.selectbox("Kenapa aku sayang kamu?", 
                 ["Pilih alasannya...", "Kamu baik banget", "Senyum kamu bikin tenang", "Kamu selalu ada buat aku", "Masakan kamu enak"])
    
    if alasan != "Pilih alasannya...":
        st.write(f"Iya bener! **{alasan}** itu yang bikin aku jatuh cinta setiap hari.")
        st.snow()

# Footer
st.write("---")
st.caption("Dibuat dengan ❤️ menggunakan Hatinya Faza")
