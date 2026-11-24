# Analisis dan Peramalan Jumlah Penghuni LKSA Kota Surabaya

Repository ini disiapkan sebagai kerangka awal proyek analisis data dan peramalan jumlah penghuni Lembaga Kesejahteraan Sosial Anak (LKSA) di Kota Surabaya.

Pada tahap awal, repository memuat struktur proyek dan dokumentasi setup. Kode analisis, notebook, metode, evaluasi, visualisasi, serta hasil setiap tahap pekerjaan akan ditambahkan secara bertahap setelah repository awal dibuat.

## Tujuan umum

Proyek ini bertujuan mengolah dan menganalisis data LKSA Kota Surabaya serta mengembangkan pendekatan peramalan jumlah penghuni berdasarkan data yang tersedia. Definisi variabel, tahapan analisis, metode, skenario eksperimen, dan metrik evaluasi akan didokumentasikan ketika pekerjaan terkait mulai dikembangkan.

## Dataset awal

- **Nama dataset:** Banyaknya Panti Asuhan, Kapasitas dan Penghuni Per Kecamatan.
- **Instansi sumber:** Dinas Sosial Kota Surabaya.
- **Portal data:** [Satu Data Surabaya](https://ckan.surabaya.go.id/id/dataset/banyaknya-panti-asuhan-kapasitas-dan-penghuni-per-kecamatan).
- **Lokasi file yang direncanakan:** `data/raw/07-panti-asuhan-per-kecamatan.csv`.
- **Catatan sumber dan penggunaan:** [docs/SUMBER_DATA.md](docs/SUMBER_DATA.md).

Periksa metadata pada portal resmi sebelum memperbarui dataset. Jangan menganggap file lokal otomatis mencerminkan versi terbaru di portal.

## Struktur repository

```text
peramalan-penghuni-lksa-surabaya/
├── data/
│   ├── raw/                  # Dataset sumber
│   └── processed/            # Data hasil pemrosesan
├── docs/                     # Dokumentasi proyek dan panduan Git
├── notebooks/                # Notebook analisis
├── src/                      # Kode sumber
├── tests/                    # Pengujian kode
├── output/                   # Grafik, tabel, dan hasil analisis
├── .gitattributes
├── .gitignore
├── requirements.txt
└── README.md
```

Folder kerangka dipertahankan dengan file README agar terlihat di GitHub. Implementasi pekerjaan akan ditambahkan sesuai perkembangan proyek.

## Program dan teknologi

### Perangkat lunak
| Program | Kegunaan |
|---|---|
| Python 3.11 | Bahasa pemrograman utama |
| Visual Studio Code | Editor kode dan dokumentasi |
| Jupyter Notebook | Lingkungan analisis interaktif |
| Git | Version control |
| GitHub | Hosting repository dan riwayat perubahan |

### Pustaka Python
| Pustaka | Kegunaan |
|---|---|
| pandas | Membaca CSV, membersihkan data, manipulasi tabel, dan agregasi |
| NumPy | Komputasi numerik |
| Matplotlib | Visualisasi data |
| statsmodels | Uji ADF/KPSS dan model deret waktu seperti ARIMA serta Holt-Winters |
| Jupyter | Menjalankan notebook |
| IPykernel | Kernel Python untuk Jupyter |

## Instalasi

Disarankan menggunakan Python 3.11. Dari terminal PowerShell pada direktori utama proyek:

```powershell
python --version
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name lksa-surabaya --display-name "Python (LKSA Surabaya)"
jupyter notebook
```

Git, GitHub, dan Visual Studio Code merupakan perangkat pengembangan terpisah dan tidak dipasang melalui pip.

## Panduan GitHub

- [Setup upload pertama kali](docs/GIT_FIRST_UPLOAD_SETUP.md)
- [Workflow Git umum](docs/GIT_WORKFLOW_GENERAL.md)
- [Update berdasarkan enam progress](docs/GIT_UPDATE_PER_PROGRESS.md)
- [Program dan teknologi](docs/PROGRAM_DAN_TEKNOLOGI.md)
- [Sumber data](docs/SUMBER_DATA.md)
- [Struktur proyek](docs/PROJECT_STRUCTURE.md)

Sebelum melakukan commit, periksa file yang akan diunggah. Jangan memasukkan password, token, API key, file `.env`, kredensial, atau data pribadi. Pastikan ketentuan penggunaan dataset mengizinkan pembagian ulang.

## Status repository

**Tahap:** Project starter. Belum berisi implementasi analisis, pemodelan, evaluasi, maupun hasil eksperimen. Enam progress penelitian akan ditambahkan secara bertahap.
