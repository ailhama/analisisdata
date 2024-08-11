import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

# Set up matplotlib to work with Streamlit
matplotlib.use('Agg')

@st.cache_data
def load_data():
    data = pd.read_excel("data.xlsx")
    data.fillna(data.select_dtypes(include=[np.number]).mean(), inplace=True)
    return data

def app():
    data = load_data()

    st.title("Submission Analisis Data Detik")
    st.write("**by Audi Ilham Atmaja**")

    source_medium = st.sidebar.selectbox(
        "Select Source Medium",
        options=["All", "facebook / cpc", "google / cpc"]
    )

    if source_medium != "All":
        filtered_data = data[data['ga:sourceMedium'] == source_medium]
    else:
        filtered_data = data

    st.subheader("Data Overview")
    st.dataframe(filtered_data)

    st.subheader("Deskripsi Variabel Dataset")
    # Tabs for variable descriptions
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Sumber", "Judul Halaman", "Jumlah Pengguna", "Bounce Rate", 
        "Jumlah Halaman", "Pageviews Per Session", "Waktu Rata-rata di Halaman"
    ])

    with tab1:
        st.info("""Sumber traffic yang mengarahkan pengguna ke halaman tersebut. 
                  Contoh: Facebook / CPC, Google / CPC.""")

    with tab2:
        st.info("""Judul halaman yang ditampilkan di laporan. Ini biasanya 
                  adalah judul konten atau artikel yang dikunjungi pengguna.""")

    with tab3:
        st.info("""Jumlah pengguna unik yang mengunjungi halaman tersebut. 
                  Metrik ini mengukur berapa banyak individu yang berbeda 
                  yang mengunjungi halaman.""")

    with tab4:
        st.info("""Persentase sesi di mana pengguna hanya melihat satu halaman 
                  sebelum meninggalkan situs.""")

    with tab5:
        st.info("""Total jumlah halaman yang dilihat selama sesi. Ini mengukur 
                  seberapa banyak konten yang dikonsumsi oleh pengguna dalam 
                  satu sesi.""")

    with tab6:
        st.info("""Rata-rata jumlah halaman yang dilihat per sesi. Ini memberikan 
                  gambaran tentang seberapa banyak halaman yang biasanya dilihat 
                  pengguna dalam satu sesi.""")

    with tab7:
        st.info("""Rata-rata waktu yang dihabiskan pengguna pada halaman tersebut. 
                  Metrik ini dapat memberikan wawasan tentang seberapa menarik 
                  atau relevan konten halaman tersebut untuk pengguna.""")

    st.subheader("Distribusi Users")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['ga:users'], kde=True, ax=ax)
    ax.set_title('Distribusi Users')
    st.pyplot(fig)

    st.subheader("Distribusi Bounce Rate")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['ga:bounceRate'], kde=True, ax=ax)
    ax.set_title('Distribusi Bounce Rate')
    st.pyplot(fig)

    st.subheader("Distribusi Page Views")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['ga:pageviews'], kde=True, ax=ax)
    ax.set_title('Distribusi Page Views')
    st.pyplot(fig)

    st.subheader("Distribusi Page Views Per Session")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['ga:pageviewsPerSession'], kde=True, ax=ax)
    ax.set_title('Distribusi Page Views Per Session')
    st.pyplot(fig)

    st.subheader("Distribusi Avg Time On Page")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['ga:avgTimeOnPage'], kde=True, ax=ax)
    ax.set_title('Distribusi Avg Time On Page')
    st.pyplot(fig)

    st.subheader("Scatter Plot of Bounce Rate vs. Pageviews")
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x='ga:bounceRate', y='ga:pageviews', hue='ga:sourceMedium', ax=ax)
    ax.set_title('Scatter Plot of Bounce Rate vs. Pageviews')
    st.pyplot(fig)

    st.subheader("Bounce Rate Distribution by Source Medium")
    fig, ax = plt.subplots()
    sns.boxplot(data=filtered_data, x='ga:sourceMedium', y='ga:bounceRate', ax=ax)
    ax.set_title('Bounce Rate Distribution by Source Medium')
    ax.set_xlabel('Source Medium')
    ax.set_ylabel('Bounce Rate (%)')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

    st.subheader("Correlation Matrix of Key Metrics")
    corr = filtered_data[['ga:users', 'ga:pageviews', 'ga:pageviewsPerSession', 'ga:avgTimeOnPage']].corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title('Correlation Matrix of Key Metrics')
    st.pyplot(fig)

    st.subheader("Top 10 Pages by Pageviews")
    top_pages = filtered_data.sort_values(by='ga:pageviews', ascending=False).head(10)
    st.write(top_pages[['ga:pageTitle', 'ga:pageviews']])

    st.subheader("Top 10 Pages by Pageviews Bar Chart")
    fig, ax = plt.subplots()
    sns.barplot(x='ga:pageviews', y='ga:pageTitle', data=top_pages, ax=ax)
    ax.set_title('Top 10 Pages by Pageviews')
    st.pyplot(fig)
