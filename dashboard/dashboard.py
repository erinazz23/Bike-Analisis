import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO

# Menonaktifkan peringatan PyplotGlobalUse
st.set_option('deprecation.showPyplotGlobalUse', False)

# Mendownload dataset dari URL
url = "https://raw.githubusercontent.com/erinazz23/Bike-Analisis/master/data/day.csv"
response = requests.get(url)

# Membaca file CSV
bike_sharing = pd.read_csv(StringIO(response.text))

# Menampilkan judul dashboard
st.title('Dashboard Data Sepeda')

# Menambahkan gambar sebagai latar belakang
st.image('https://2.bp.blogspot.com/-6fmf2YxAA_Y/Wye5EHhaS2I/AAAAAAAAPys/IrxgQxpLERoC9aqGQvHUtYZbloTfIFfEgCLcBGAs/s1600/sepda.jpg', use_column_width=True)

# Menampilkan beberapa baris pertama dari dataset
st.subheader('Data Sepeda')
st.write(bike_sharing.head())

# Menampilkan visualisasi jumlah penyewa sepeda per musim dan stok sepeda
st.subheader('Hubungan Penyewa Sepeda dengan Banyaknya Sepeda')
seasonal_inventory = bike_sharing.groupby('season')['cnt'].sum()
season_names = ['Spring', 'Summer', 'Fall', 'Winter']
seasonal_renters = bike_sharing.groupby('season')['cnt'].mean()
fig, ax = plt.subplots()
ax.bar(season_names, seasonal_inventory, color='skyblue', label='Stok Sepeda')
ax.plot(season_names, seasonal_renters, color='orange', marker='o', linestyle='-', linewidth=2, label='Penyewa Sepeda')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah')
ax.set_title('Hubungan Penyewa Sepeda dengan Banyaknya Sepeda')
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)  # Menambahkan garis-garis grid pada sumbu y
st.pyplot(fig)

# Membaca data sepeda
bike_data = pd.read_csv("https://raw.githubusercontent.com/erinazz23/Bike-Analisis/master/data/day.csv")

# Mengonversi kolom tanggal menjadi tipe data datetime
bike_data['tanggal'] = pd.to_datetime(bike_data['dteday'])

# Mengatur kolom tanggal sebagai indeks
bike_data.set_index('tanggal', inplace=True)

# Resampling data menjadi data bulanan dan menghitung total penggunaan sepeda per bulan
monthly_bike_usage = bike_data['cnt'].resample('M').sum()

# Membaca data tambahan
additional_data = pd.read_csv("https://raw.githubusercontent.com/erinazz23/Bike-Analisis/master/data/day.csv")

# Mengonversi kolom tanggal menjadi tipe data datetime
additional_data['tanggal'] = pd.to_datetime(additional_data['dteday'])

# Mengatur kolom tanggal sebagai indeks
additional_data.set_index('tanggal', inplace=True)

# Resampling data tambahan menjadi data bulanan dan menghitung total penggunaan sepeda per bulan
monthly_additional_usage = additional_data['cnt'].resample('M').sum()

# Menggabungkan kedua dataset
merged_data = pd.concat([monthly_bike_usage, monthly_additional_usage], axis=1)
merged_data.columns = ['Penggunaan Awal', 'Penggunaan Tambahan']


# Muat dataset dari URL
url = "https://raw.githubusercontent.com/erinazz23/Bike-Analisis/master/data/day.csv"
bike_data = pd.read_csv(url)

# Hitung jumlah pengguna yang memenuhi setiap kriteria diskon
discount_counts = {
    'Diskon 10% (≤30 kali)': len(bike_data[bike_data['cnt'] >= 50]),
    'Diskon 20% (≥30 kali)': len(bike_data[bike_data['cnt'] >= 60]),
}

# Hitung total jumlah diskon
total_discounts = sum(discount_counts.values())

# Tampilkan judul aplikasi
st.header('Analisis Diskon Pengguna Sepeda')

# Tampilkan total jumlah diskon
st.subheader('Total Jumlah Diskon:')
st.write(total_discounts)

# Tampilkan detail diskon per kriteria
st.subheader('Detail Diskon per Kriteria:')
for k, v in discount_counts.items():
    st.write(f"{k}: {v}")

# Tampilkan dalam diagram batang
st.subheader('Diagram Batang Jumlah Penerima Diskon Berdasarkan Kriteria')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(discount_counts.keys(), discount_counts.values(), color=['skyblue', 'lightgreen'])
ax.set_xlabel('Kriteria Diskon')
ax.set_ylabel('Jumlah Penerima Diskon')
ax.set_title('Jumlah Penerima Diskon Berdasarkan Kriteria')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)


# Menampilkan plot tren jangka panjang penggunaan sepeda
st.subheader('Tren Jangka Panjang Penggunaan Sepeda')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(merged_data.index, merged_data['Penggunaan Awal'], color='skyblue', marker='o', label='Penggunaan Awal')
ax.plot(merged_data.index, merged_data['Penggunaan Tambahan'], color='orange', marker='o', label='Penggunaan Tambahan')
ax.set_title('Tren Jangka Panjang Penggunaan Sepeda')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penggunaan Sepeda')
ax.legend()
ax.grid(True)
st.pyplot(fig)
