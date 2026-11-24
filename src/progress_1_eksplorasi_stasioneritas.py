"""PROGRESS 1: Eksplorasi data dan pemeriksaan stasioneritas awal."""
import matplotlib.pyplot as plt
import pandas as pd
from _common import (
    load_and_clean_raw, make_monthly, OUTPUT_DIR, run_adf_kpss,
    save_monthly, DATA_FILE, MONTH_ID,
)


def main():
    raw_original = pd.read_csv(DATA_FILE, sep=";", encoding="utf-8-sig")
    raw = load_and_clean_raw()
    monthly = make_monthly(raw)

    print("=== PROGRESS 1: EKSPLORASI DAN STASIONERITAS ===")
    print(f"Baris CSV awal: {len(raw_original)} | Setelah hapus duplikasi identik: {len(raw)}")
    print(
        f"Periode: {MONTH_ID[monthly.index.min().month]} {monthly.index.min().year} "
        f"s.d. {MONTH_ID[monthly.index.max().month]} {monthly.index.max().year}"
    )
    print(f"Jumlah observasi bulanan: {len(monthly)}")
    print("Jumlah bulan kosong:", int(monthly["jumlah_penghuni"].isna().sum()))

    if monthly["jumlah_penghuni"].isna().any():
        raise ValueError("Ada bulan yang hilang. Periksa sumber data sebelum melanjutkan.")

    y = monthly["jumlah_penghuni"].astype(float)
    save_monthly(monthly)

    # Grafik 1: deret waktu aktual.
    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.plot(y.index, y.values, marker="o", linewidth=2, label="Jumlah penghuni")
    ax.set(
        title="Jumlah Penghuni LKSA Kota Surabaya per Bulan",
        xlabel="Periode",
        ylabel="Jumlah penghuni (orang)",
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "p1_grafik_time_series.png", dpi=180)
    fig.savefig(OUTPUT_DIR / "p1_grafik_time_series.svg", format="svg")
    plt.show()

    # Grafik 2: rolling statistics (jendela 3 bulan, untuk deskripsi eksploratif).
    roll_mean = y.rolling(window=3).mean()
    roll_std = y.rolling(window=3).std()
    fig, ax = plt.subplots(figsize=(11, 4.8))
    ax.plot(y.index, y.values, marker="o", alpha=0.45, label="Aktual")
    ax.plot(roll_mean.index, roll_mean.values, linewidth=2, label="Rolling mean (3 bulan)")
    ax.plot(roll_std.index, roll_std.values, linewidth=2, label="Rolling std (3 bulan)")
    ax.set(
        title="Rolling Mean dan Rolling Standard Deviation",
        xlabel="Periode",
        ylabel="Jumlah penghuni",
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "p1_rolling_statistics.png", dpi=180)
    fig.savefig(OUTPUT_DIR / "p1_rolling_statistics.svg", format="svg")
    plt.show()

    # Grafik 3: first difference untuk melihat perubahan bulanan.
    diff1 = y.diff().dropna()
    fig, ax = plt.subplots(figsize=(11, 3.8))
    ax.axhline(0, color="black", linewidth=1)
    ax.plot(diff1.index, diff1.values, marker="o", linewidth=1.8)
    ax.set(
        title="First Difference Jumlah Penghuni",
        xlabel="Periode",
        ylabel="Perubahan penghuni (orang)",
    )
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "p1_first_difference.png", dpi=180)
    fig.savefig(OUTPUT_DIR / "p1_first_difference.svg", format="svg")
    plt.show()

    results = [
        run_adf_kpss(y, "Data level"),
        run_adf_kpss(diff1, "First difference"),
    ]
    result_df = pd.DataFrame(results)
    result_df.to_csv(OUTPUT_DIR / "p1_hasil_adf_kpss.csv", index=False)
    print("\nHasil ADF dan KPSS (alpha 5%):")
    print(
        result_df[
            ["seri", "n", "adf_p_value", "kpss_p_value", "interpretasi"]
        ].to_string(index=False)
    )
    print(
        "\nCatatan: hasil uji pada 22 observasi bersifat terbatas; "
        "jangan menyimpulkan nonstasioner hanya dari grafik."
    )
    print(f"Output tersimpan di: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
