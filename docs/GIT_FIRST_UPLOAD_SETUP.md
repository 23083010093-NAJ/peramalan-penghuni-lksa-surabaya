# Setup Upload Pertama Kali ke GitHub

## 1. Persiapan
1. Ekstrak folder project starter.
2. Buka folder utama di Visual Studio Code.
3. Pastikan terminal berada di direktori yang sama dengan README.md.
4. Buat repository kosong di GitHub dengan nama `peramalan-penghuni-lksa-surabaya`. Jangan menambahkan README, .gitignore, atau License dari GitHub karena file tersebut sudah ada di proyek lokal.

## 2. Konfigurasi Identitas Git (sekali per komputer)
```powershell
git config --global user.name "Nama Anda"
git config --global user.email "email-github-anda"
```

## 3. Inisialisasi dan Upload Awal
Jalankan satu per satu:

```powershell
git init
git branch -M main
git add .
git status
git diff --cached --stat
git commit -m "chore: initial project setup"
git remote add origin https://github.com/23083010093-NAJ/peramalan-penghuni-lksa-surabaya.git
git push -u origin main
```

Saat diminta autentikasi, selesaikan melalui metode autentikasi GitHub yang tersedia di komputer.

## 4. Verifikasi
Buka repository:
https://github.com/23083010093-NAJ/peramalan-penghuni-lksa-surabaya

Pastikan README, requirements.txt, konfigurasi Git, dan direktori proyek tampil.

## Catatan
- Perintah `git init` dan `git remote add origin` hanya dilakukan saat setup lokal pertama kali.
- Jangan masukkan password atau token ke file proyek.
- Periksa `git status` sebelum commit.
