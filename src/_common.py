"""Fungsi bersama untuk enam progress analisis panti asuhan Surabaya."""
from pathlib import Path
import warnings
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "raw" / "07-panti-asuhan-per-kecamatan.csv"
OUTPUT_DIR = ROOT / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

MONTH_MAP = {
    "Januari": 1, "Februari": 2, "Maret": 3, "April": 4,
    "Mei": 5, "Juni": 6, "Juli": 7, "Agustus": 8,
    "September": 9, "Oktober": 10, "November": 11, "Desember": 12,
}
MONTH_ID = {v: k for k, v in MONTH_MAP.items()}

REQUIRED_COLUMNS = [
    "Kode Kecamatan Kemendagri", "Kode Kecamatan BPS", "Kecamatan",
    "Jumlah LKSA", "Kapasitas Tampung", "Jumlah Penghuni", "Periode", "Tahun",
]


def load_and_clean_raw(path=DATA_FILE):
    """Membaca CSV, memvalidasi kolom, dan menghapus duplikasi identik."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"File tidak ditemukan: {path}\nSimpan CSV pada folder data/raw di direktori utama proyek."
        )
    raw = pd.read_csv(path, sep=";", encoding="utf-8-sig")
    raw.columns = raw.columns.astype(str).str.strip()
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in raw.columns]
    if missing_cols:
        raise ValueError(f"Kolom wajib tidak ditemukan: {missing_cols}. Kolom tersedia: {raw.columns.tolist()}")

    for col in ["Jumlah LKSA", "Kapasitas Tampung", "Jumlah Penghuni", "Tahun"]:
        raw[col] = pd.to_numeric(raw[col], errors="coerce")
    raw["Periode"] = raw["Periode"].astype(str).str.strip().str.title()
    raw["Kecamatan"] = raw["Kecamatan"].astype(str).str.strip()

    if raw[["Jumlah LKSA", "Kapasitas Tampung", "Jumlah Penghuni", "Tahun"]].isna().any().any():
        raise ValueError("Ada nilai kosong/non-numerik pada kolom numerik. Periksa file CSV sebelum pemodelan.")
    if not raw["Periode"].isin(MONTH_MAP).all():
        invalid = sorted(raw.loc[~raw["Periode"].isin(MONTH_MAP), "Periode"].unique())
        raise ValueError(f"Nama bulan tidak dikenali: {invalid}")

    key_cols = ["Kode Kecamatan BPS", "Periode", "Tahun"]
    duplicate_key_mask = raw.duplicated(key_cols, keep=False)
    duplicate_keys = raw.loc[duplicate_key_mask, key_cols].drop_duplicates()
    if not duplicate_keys.empty:
        exact_dedup = raw.drop_duplicates()
        remaining = exact_dedup.duplicated(key_cols, keep=False)
        if remaining.any():
            conflict = exact_dedup.loc[remaining, key_cols + ["Jumlah LKSA", "Kapasitas Tampung", "Jumlah Penghuni"]]
            raise ValueError(
                "Ditemukan duplikasi kecamatan-bulan dengan isi berbeda. Jangan dijumlahkan otomatis.\n"
                + conflict.head(10).to_string(index=False)
            )
        raw = exact_dedup.copy()

    raw["tanggal"] = pd.to_datetime({
        "year": raw["Tahun"].astype(int),
        "month": raw["Periode"].map(MONTH_MAP).astype(int),
        "day": 1,
    })
    raw = raw.sort_values(["tanggal", "Kode Kecamatan BPS"]).reset_index(drop=True)
    return raw


def make_monthly(raw=None):
    """Agregasi seluruh kecamatan menjadi deret waktu bulanan."""
    if raw is None:
        raw = load_and_clean_raw()
    monthly = (
        raw.groupby("tanggal", as_index=True)
        .agg(
            jumlah_lksa=("Jumlah LKSA", "sum"),
            kapasitas_tampung=("Kapasitas Tampung", "sum"),
            jumlah_penghuni=("Jumlah Penghuni", "sum"),
            jumlah_kecamatan=("Kode Kecamatan BPS", "nunique"),
        )
        .sort_index()
    )
    monthly.index = pd.DatetimeIndex(monthly.index, name="tanggal")
    full_index = pd.date_range(monthly.index.min(), monthly.index.max(), freq="MS", name="tanggal")
    return monthly.reindex(full_index)


def run_adf_kpss(series, label):
    """Menjalankan ADF dan KPSS serta mengembalikan ringkasan yang aman untuk sampel pendek."""
    from statsmodels.tsa.stattools import adfuller, kpss
    s = pd.Series(series).dropna().astype(float)
    result = {
        "seri": label, "n": int(len(s)), "adf_statistik": np.nan,
        "adf_p_value": np.nan, "kpss_statistik": np.nan,
        "kpss_p_value": np.nan, "interpretasi": "Tidak dapat diuji",
    }
    if len(s) < 8 or s.nunique() < 2:
        result["interpretasi"] = "Observasi/variasi data tidak cukup untuk pengujian yang andal"
        return result
    try:
        adf_result = adfuller(s, autolag="AIC")
        result["adf_statistik"] = float(adf_result[0])
        result["adf_p_value"] = float(adf_result[1])
    except Exception as exc:
        result["adf_error"] = str(exc)
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            kpss_result = kpss(s, regression="c", nlags="auto")
        result["kpss_statistik"] = float(kpss_result[0])
        result["kpss_p_value"] = float(kpss_result[1])
    except Exception as exc:
        result["kpss_error"] = str(exc)

    ap, kp = result["adf_p_value"], result["kpss_p_value"]
    if pd.notna(ap) and pd.notna(kp):
        if ap < 0.05 and kp >= 0.05:
            result["interpretasi"] = "Konsisten dengan stasioner (ADF menolak unit root; KPSS tidak menolak stasioneritas)"
        elif ap >= 0.05 and kp < 0.05:
            result["interpretasi"] = "Konsisten dengan nonstasioner"
        else:
            result["interpretasi"] = "Belum konklusif/hasil kedua uji belum memberi bukti yang tegas"
    return result


def save_monthly(monthly, filename="data_bulanan_panti_asuhan.csv"):
    out = monthly.copy().reset_index()
    out.to_csv(OUTPUT_DIR / filename, index=False)
    return OUTPUT_DIR / filename
