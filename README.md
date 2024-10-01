# Dashboard Analisis Data E-Commerce

Ini adalah dashboard yang dibangun menggunakan Streamlit yang menyediakan analisis data E-Commerce, termasuk perilaku pelanggan, pesanan, produk, dan pembayaran. Dashboard ini memvisualisasikan metrik kunci dan memungkinkan penyaringan berdasarkan kategori produk dan pengeluaran minimum.

## Fitur

- Distribusi pesanan per pelanggan
- Total pengeluaran per pelanggan
- Kategori produk teratas berdasarkan pendapatan
- Analisis korelasi antara harga, nilai pengiriman, dan nilai pembayaran

## Persiapan dan Instalasi

### Prasyarat

Untuk menjalankan proyek ini, Anda memerlukan perangkat lunak berikut yang terinstal di mesin Anda:

- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)
- [Streamlit](https://docs.streamlit.io/) (kerangka kerja Python untuk membangun dashboard)

## Setup Environment - Anaconda
conda create --name main-ds
conda activate main-ds
pip install -r requirements.txt

## Setup Environment - Shell/Terminal
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

## Run steamlit app
streamlit run streamlit_dashboard.py
