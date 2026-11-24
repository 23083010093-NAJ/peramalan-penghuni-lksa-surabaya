# Progress 1 — Eksplorasi Data dan Uji Stasioneritas

## Tujuan
Melakukan pemeriksaan awal dataset, membersihkan duplikasi identik, membentuk deret waktu agregat bulanan, memvisualisasikan tren, dan menguji stasioneritas menggunakan Augmented Dickey-Fuller (ADF) serta Kwiatkowski-Phillips-Schmidt-Shin (KPSS).

## Dataset dan target
- Nama file yang diperlukan: \`data/raw/07-panti-asuhan-per-kecamatan.csv\`
- Unit observasi sumber: kecamatan per bulan.
- Target deret waktu: total \`Jumlah Penghuni\` seluruh kecamatan pada setiap bulan.
- Periode yang diperiksa: Januari 2025–Oktober 2026.
- Sumber dataset: [Satu Data Surabaya](https://ckan.surabaya.go.id/id/dataset/banyaknya-panti-asuhan-kapasitas-dan-penghuni-per-kecamatan).

**Catatan dataset:** file CSV mentah belum ditambahkan ke repository. Unduh dataset dari sumber resmi, lalu simpan dengan nama \`07-panti-asuhan-per-kecamatan.csv\` pada folder \`data/raw/\` sebelum menjalankan script.

## Langkah pengolahan
1. Membaca CSV dengan pemisah titik koma dan encoding UTF-8-SIG.
2. Memvalidasi kolom yang diperlukan serta mengubah kolom jumlah dan tahun menjadi numerik.
3. Menghapus baris duplikat identik. Duplikasi dengan isi berbeda pada kunci kecamatan-bulan akan dihentikan dengan pesan kesalahan untuk pemeriksaan manual.
4. Mengagregasikan jumlah LKSA, kapasitas tampung, dan jumlah penghuni per bulan.
5. Memeriksa bulan yang hilang.
6. Membuat grafik deret waktu, rolling mean/standard deviation (jendela 3 bulan), dan first difference.
7. Menjalankan ADF dan KPSS pada data level dan first difference dengan taraf signifikansi 5%.

## Hasil eksekusi lokal
| Pemeriksaan | Hasil |
|---|---:|
| Baris CSV awal | 713 |
| Baris setelah deduplikasi identik | 682 |
| Observasi bulanan | 22 |
| Rentang waktu | Januari 2025–Oktober 2026 |
| Bulan kosong pada deret waktu | 0 |

### Hasil uji stasioneritas
| Seri | n | ADF p-value | KPSS p-value | Interpretasi program |
|---|---:|---:|---:|---|
| Data level | 22 | 0.999047 | 0.100000 | Belum konklusif/hasil kedua uji belum memberi bukti yang tegas |
| First difference | 21 | 0.009292 | 0.100000 | Konsisten dengan stasioner menurut kombinasi hasil ADF dan KPSS |

Catatan: nilai p-value KPSS 0.100000 adalah batas atas pelaporan yang dikembalikan prosedur uji pada konfigurasi ini; bukan estimasi p-value presisi di atas 0,10. Sampel hanya memiliki 22 observasi bulanan, sehingga interpretasi uji perlu mempertimbangkan keterbatasan ukuran sampel.

## Berkas hasil
- \`output/data_bulanan_panti_asuhan.csv\`
- \`output/p1_hasil_adf_kpss.csv\`
- \`output/p1_grafik_time_series.png\` dan \`.svg\`
- \`output/p1_rolling_statistics.png\` dan \`.svg\`
- \`output/p1_first_difference.png\` dan \`.svg\`

Grafik PNG dan SVG dihasilkan saat script dijalankan. Dua tabel CSV hasil eksekusi lokal turut dicatat di repository.

## Cara menjalankan
Dari direktori utama repository:

\`\`\`powershell
python src/progress_1_eksplorasi_stasioneritas.py
\`\`\`

Kebutuhan Python terdapat pada \`requirements.txt\` di direktori utama repository. Kode Progress 1 menggunakan \`src/_common.py\` sebagai fungsi bantu bersama.
