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
Contoh file yang dapat ditambahkan setelah dibuat:
```powershell
git add notebooks/progress_1_eksplorasi.ipynb
git add src/progress_1/
git commit -m "analysis: add data exploration and stationarity tests"
git push origin main
```

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
