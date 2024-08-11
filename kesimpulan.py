import streamlit as st

def app():
    st.title("Kesimpulan")

    st.subheader("Pertanyaan Bisnis yang Bisa Diajukan:")
    st.subheader("Pertanyaan 1:")
    st.markdown("""
    1. **Apa yang menyebabkan beberapa halaman memiliki bounce rate yang tinggi, dan bagaimana kita bisa mengurangi bounce rate ini?**
    """)

    st.markdown("""
    Terlihat bahwa halaman dengan **pageviews tinggi** cenderung memiliki **bounce rate** yang bervariasi. 
    Terdapat beberapa halaman dengan **bounce rate** rendah yang memiliki **pageviews sangat tinggi**, 
    yang bisa menunjukkan bahwa konten tersebut sangat menarik bagi pengunjung, sehingga mereka 
    tidak langsung keluar dari situs setelah melihat satu halaman.

    Hampir semua titik yang dianalisis berasal dari sumber **`facebook / cpc`** dengan 151 sesi, 
    dengan hanya satu titik yaitu 5 sesi dari **`google / cpc`**. Ini menunjukkan bahwa sebagian besar 
    traffic berasal dari Facebook, yang mungkin berdampak pada pola **bounce rate** dan **pageviews**.

    Standar deviasi (std) dari **`google / cpc`** lebih tinggi (41.18) dibandingkan **`facebook / cpc`** 
    (35.88) yang menunjukkan bahwa terdapat variabilitas yang lebih besar dalam **bounce rate** dari 
    **`google / cpc`**. Dengan kata lain, pengalaman pengguna dari **`google / cpc`** lebih bervariasi walaupun 
    dengan jumlah data yang sedikit, yang bisa disebabkan oleh berbagai faktor seperti relevansi halaman 
    yang dikunjungi atau jenis promosinya.

    Kedua sumber memiliki nilai minimum **0%**, yang menunjukkan bahwa beberapa pengguna tidak mengalami 
    **bounce rate** sama sekali. Nilai maksimum untuk keduanya adalah **100%**, yang berarti beberapa pengguna 
    meninggalkan halaman tanpa melakukan interaksi lain.
    """)

    st.subheader("Pertanyaan 2:")
    st.markdown("""
    2. **Apa faktor yang mempengaruhi jumlah tampilan halaman yang tinggi dan waktu yang dihabiskan di halaman tertentu, dan bagaimana kita bisa mereplikasi kesuksesan ini di halaman lain?**
    """)
    st.markdown("""
    Korelasi tinggi antara **`ga:users`** dan **`ga:pageviews`** menunjukkan bahwa semakin banyak pengguna unik 
    (**`ga:users`**), maka kemungkinan besar jumlah tampilan halaman (**`ga:pageviews`**) juga akan meningkat. 
    Hal ini bisa diartikan bahwa trafik yang lebih tinggi cenderung menghasilkan lebih banyak tampilan halaman.

    Korelasi negatif atau rendah antara **`ga:pageviewsPerSession`** dan metrik lainnya, serta antara 
    **`ga:avgTimeOnPage`** dengan metrik lainnya, menunjukkan bahwa tidak ada hubungan kuat antara banyaknya 
    halaman yang dilihat dalam satu sesi atau waktu rata-rata yang dihabiskan pada halaman dengan metrik 
    lainnya seperti **`ga:users`** atau **`ga:pageviews`**. Ini bisa mengindikasikan bahwa sesi yang lebih panjang 
    atau lebih pendek tidak selalu berkorelasi dengan jumlah pengguna atau tampilan halaman.

    Beberapa halaman memiliki jumlah tampilan yang sangat tinggi, seperti artikel tentang 
    `"Bikin Lambe Turah Diomelin, Nih Si Seksi yang Lengket - lengket sama Gading"` yang memiliki lebih 
    dari **80 ribu** tampilan halaman. Hal ini menunjukkan popularitas konten yang sangat tinggi dan dapat 
    memberikan wawasan mengenai jenis konten yang menarik banyak perhatian pengguna.

    Banyak dari halaman yang masuk ke dalam daftar **10 teratas** berkaitan dengan **topik-topik kontroversial, 
    sensasional, atau berita terkini**, yang menunjukkan bahwa pengguna tertarik pada jenis konten ini.
    """)

if __name__ == "__main__":
    app()
