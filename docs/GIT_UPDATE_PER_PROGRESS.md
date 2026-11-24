# Panduan Update GitHub per Progress

Panduan ini digunakan setelah repository lokal sudah terhubung ke GitHub. Jalankan perintah dari direktori utama proyek.

## Pola umum setiap kali melakukan update
```powershell
git status
git pull --rebase origin main
git add PATH_FILE_ATAU_FOLDER
git diff --cached --stat
git commit -m "tipe: deskripsi perubahan"
git push origin main
```

Ganti `PATH_FILE_ATAU_FOLDER` dengan path berkas yang benar-benar dibuat. Jangan menjalankan `git add .` apabila ada file lokal yang tidak ingin diunggah.

## Progress 1 — Eksplorasi Data dan Uji Stasioneritas

File Progress 1 yang saat ini sudah ada di repository:
- `src/progress_1_eksplorasi_stasioneritas.py`
- `src/_common.py`
- `docs/PROGRESS_1_EKSPLORASI_STASIONERITAS.md`
- `output/data_bulanan_panti_asuhan.csv`
- `output/p1_hasil_adf_kpss.csv`

Untuk mengunggah perubahan lanjutan Progress 1 dari komputer lokal:
```powershell
git add src/_common.py src/progress_1_eksplorasi_stasioneritas.py
git add docs/PROGRESS_1_EKSPLORASI_STASIONERITAS.md
git add output/data_bulanan_panti_asuhan.csv output/p1_hasil_adf_kpss.csv
git add data/raw/07-panti-asuhan-per-kecamatan.csv
git commit -m "analysis: update progress 1 exploration and stationarity"
git push origin main
```

Catatan: file CSV mentah belum ada di GitHub. Perintah terakhir hanya berhasil jika file sudah diunduh dan tersedia di path tersebut. Pastikan ketentuan sumber data mengizinkan distribusi salinan sebelum mengunggahnya.

## Progress 2 — Deskripsi dan Karakteristik Dataset
```powershell
git add notebooks/progress_2_deskripsi_dataset.ipynb
git add docs/deskripsi_dataset.md
git commit -m "docs: add dataset characteristics"
git push origin main
```

## Progress 3 — Poster: Latar Belakang dan Dataset
```powershell
git add docs/poster/latar_belakang_dataset.md
git add output/poster/
git commit -m "docs: add poster background and dataset section"
git push origin main
```

## Progress 4 — Poster: Metode dan Pemodelan
```powershell
git add src/modeling/
git add notebooks/progress_4_pemodelan.ipynb
git add docs/poster/metode_pemodelan.md
git commit -m "feat: add time series modeling"
git push origin main
```

## Progress 5 — Poster: Evaluasi dan Hasil
```powershell
git add notebooks/progress_5_evaluasi.ipynb
git add output/evaluasi/
git add docs/poster/evaluasi_hasil.md
git commit -m "analysis: add model evaluation results"
git push origin main
```

## Progress 6 — Peramalan, Kesimpulan, dan Finalisasi
```powershell
git add notebooks/progress_6_peramalan.ipynb
git add output/peramalan/
git add docs/poster/kesimpulan.md
git commit -m "docs: finalize forecasts and conclusions"
git push origin main
```

## Catatan penting
- Nama file di atas adalah contoh struktur. Sesuaikan dengan file aktual yang dibuat.
- Pastikan data sensitif, kredensial, cache, dan virtual environment tidak ikut diunggah.
- Jika `git pull --rebase` menghasilkan konflik, selesaikan konflik sebelum melanjutkan push.
- Jangan mengulangi `git init` atau `git remote add origin` untuk update rutin.
