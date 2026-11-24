# Workflow Git Umum

## Melihat status
```powershell
git status
git log --oneline -5
```

## Mengambil perubahan terbaru sebelum bekerja
```powershell
git pull --rebase origin main
```

## Menambahkan perubahan tertentu
```powershell
git add PATH_FILE_ATAU_FOLDER
git diff --cached
```

## Commit dan push
```powershell
git commit -m "tipe: ringkasan perubahan"
git push origin main
```

## Tipe commit yang disarankan
- `feat`: fitur atau implementasi baru.
- `analysis`: analisis data atau eksperimen.
- `docs`: dokumentasi.
- `fix`: perbaikan kesalahan.
- `refactor`: perubahan struktur kode tanpa mengubah fungsi utama.
- `chore`: konfigurasi dan pemeliharaan proyek.

## Praktik aman
- Gunakan `git status` sebelum commit.
- Periksa isi staging dengan `git diff --cached`.
- Jangan commit token, password, file .env, atau virtual environment.
- Lakukan commit dengan satu tujuan perubahan yang jelas.
