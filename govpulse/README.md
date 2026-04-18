![GovPulse Banner](file:///C:/Users/LENOVO/.gemini/antigravity/brain/9052f237-973b-460f-94f6-4ec35022ae1e/govpulse_banner_1776518218315.png)

# GovPulse: Advanced Public Policy AI Suite

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-v0.95.1-009688)](https://fastapi.tiangolo.com/)
[![ML Framework](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)

**GovPulse** adalah platform analitik cerdas yang dirancang untuk mendukung pengambilan kebijakan publik berbasis data (*Evidence-Based Policy*). Platform ini mengintegrasikan Machine Learning canggih untuk menganalisis sentimen masyarakat dan mensimulasikan dampak indikator pembangunan secara riil.

---

## 📋 Table of Contents
- [Visi & Misi](#-visi--misi)
- [Metodologi Analisis](#-metodologi-analisis)
- [Fitur Utama](#-fitur-utama)
- [Arsitektur Proyek](#-arsitektur-proyek)
- [Panduan Instalasi](#-panduan-instalasi)

---

## 🎯 Visi & Misi
Membantu pemerintah dan pengambil kebijakan untuk:
1.  **Mendengar**: Memahami opini publik secara objektif melalui NLP (Natural Language Processing).
2.  **Memprediksi**: Menggunakan data historis dunia untuk memproyeksikan skor kesejahteraan.
3.  **Mensimulasikan**: Melakukan uji coba "What-If" terhadap anggaran dan dukungan sosial sebelum kebijakan diterapkan.

---

## 🧠 Metodologi Analisis (6 Tahapan)
Setiap analisis dalam GovPulse mengikuti standar profesional data science untuk kebijakan publik:
1.  **Data Collection**: Integrasi silo data (Dukcapil, Ekonomi, Sosial) secara otomatis dari internet.
2.  **Data Cleaning**: Validasi data pemerintah yang berantakan, penanganan *missing values*, dan deteksi anomali.
3.  **Descriptive Analysis**: Visualisasi distribusi statistik lapangan (Peta Dunia & Regional).
4.  **Feature Engineering**: Pemilihan variabel strategis (GDP, Social Support, Corruption Index).
5.  **Predictive Modeling**: Pelatihan model (Gradient Boosting/Random Forest) dengan Cross-Validation.
6.  **Prescriptive Simulation**: Rekomendasi kebijakan berdasarkan proyeksi dampak numerik.

---

## 🚀 Fitur Utama
- **Public Sentiment Engine**: Klasifikasi aspirasi publik menjadi sentimen positif/negatif untuk pemetaan opini.
- **Policy Impact Predictor**: Model AI yang mampu memprediksi indeks kebahagiaan (Happiness Score) dengan akurasi tinggi.
- **Explainable AI (XAI)**: Transparansi penuh menggunakan *Feature Importance* untuk menjelaskan dasar rekomendasi kebijakan.
- **Interactive Dashboards**: Visualisasi berbasis Plotly yang dinamis dan informatif.

---

## 📂 Struktur Proyek
```text
govpulse/
├── backend/
│   ├── app/
│   │   ├── api/          # REST API Endpoints (Swagger Docs)
│   │   ├── core/         # Global Configurations & Models
│   │   ├── ml/           # Core AI Engine (Sentiment & Predictor)
│   │   ├── schemas/      # Pydantic Data Validation
│   │   └── services/     # Business & ML Logic Layer
│   ├── models/           # Pre-trained Production Models
│   ├── Dockerfile        # Container Deployment Profile
│   └── main.py           # Application Entry Point
└── notebooks/
    └── governance_ml_experiments.ipynb # Advanced ML Research Suite
```

---

## 🛠️ Panduan Instalasi

### Prasyarat
- Python 3.10+
- Pip (Python Package Manager)

### Langkah-langkah
1.  **Clone Repository**
    ```bash
    git clone https://github.com/username/govpulse.git
    cd govpulse
    ```
2.  **Instalasi Backend**
    ```bash
    cd backend
    pip install -r requirements.txt
    ```
3.  **Menjalankan Server**
    ```bash
    python main.py
    ```
    *Akses API di `http://localhost:8000/docs`*

4.  **Menjalankan Eksperimen (Jupyter)**
    ```bash
    cd notebooks
    jupyter notebook governance_ml_experiments.ipynb
    ```

---

## 📊 Transparansi & Akurasi
Model di GovPulse divalidasi menggunakan **5-Fold Cross-Validation** untuk menjamin stabilitas prediksi. Transparansi model dijamin melalui analisis *residual* dan *feature importance* yang tertanam langsung dalam pipeline eksperimen.

---
*Developed for a Better Governance and Evidence-Based Decision Making.*
