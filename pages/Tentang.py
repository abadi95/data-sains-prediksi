import streamlit as st
from PIL import Image

st.title("Boku no Hero Academia")

image = Image.open("Team logo/1325999.jpeg")

new_size = (1000, 600)

resized_image = image.resize(new_size)

st.image(resized_image)

st.write("Boku no Hero Academia (Jepang: 僕のヒーローアカデミア, Hepburn: Boku no Hīrō Akademia), yang diterbitkan di Indonesia dengan judul My Hero Academia, adalah sebuah seri manga shōnen Jepang bertema pahlawan super yang ditulis dan diilustrasikan oleh Kōhei Horikoshi.")
st.write("Manga ini mulai dimuat dalam majalah Weekly Shōnen Jump sejak bulan Juli 2014, dan telah dibundel menjadi 37 volume tankōbon hingga bulan Februari 2023. Ceritanya mengisahkan tentang Izuku Midoriya (nama pahlawan: Deku), seorang anak lelaki tanpa kekuatan super (yang disebut quirk) di dunia tempat hal seperti itu sudah menjadi sesuatu yang umum, tetapi masih bercita-cita untuk menjadi seorang pahlawan. Ia kemudian bertemu dengan pahlawan terhebat di Jepang, All Might, yang memberikan quirk miliknya kepada Izuku setelah melihat potensinya, dan kemudian memasukkannya dalam sebuah SMA prestisius yang dikhususkan untuk para pahlawan muda yang sedang dalam pelatihan.")

st.subheader("Izuku Midoriya")

image = Image.open("Team logo/Midoriya.jpeg")

new_size = (200, 400)

resized_image = image.resize(new_size)

st.image(resized_image)

st.info("Izuku Midoriya, juga dikenal sebagai Deku, adalah protagonis utama dari manga dan anime My Hero Academia. ")
st.info("Meskipun Izuku terlahir tanpa Quirk, ia berhasil menarik perhatian pahlawan legendaris All Might, karena kepahlawanan bawaannya dan rasa keadilan yang kuat, dan sejak itu menjadi murid dekatnya, serta siswa di Kelas 1-A. di SMA UA. All Might mewariskan Quirknya yang dapat ditransfer ke Izuku, menjadikannya pemegang One For All yang kesembilan dan saat ini.")
st.info("Setelah Perang Pembebasan Paranormal, dengan Tomura Shigaraki dan All For One secara aktif menargetkan Izuku karena Quirknya, dia memutuskan untuk meninggalkan UA sebelum menyelesaikan tahun pertamanya untuk menjaga teman-teman sekelasnya dari bahaya. Setelah mendapat dorongan dan dukungan dari teman-temannya, dia kemudian kembali ke sekolah dan memimpin para pahlawan melawan penjahat dalam satu pertempuran terakhir yang putus asa untuk menyelamatkan dunia.")

st.header("Boku no Hero Academia")
st.info("Semua Tokoh")

##For members
lead=Image.open('Team photos/Preferences de boku no hero.jpeg')
size=(400,400)
lead_image=lead.resize(size)
st.image(lead_image)

st.subheader("Connect with me:")

import streamlit as st

if st.button("Instagram"):
    st.write('[Instagram](https://www.instagram.com/mutaman_abadi/?hl=id)')

if st.button("TikTok"):
    st.write('[TikTok](https://www.tiktok.com/@excited4110)')

if st.button("Twitter"):
    st.write('[Twitter](https://twitter.com/Kazuto9252)')