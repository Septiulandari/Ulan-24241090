# Input data pelanggan

nama = input("Masukkan nama anda: ")
member_status = input("Apakah memiliki kartu member? (ya/tidak): ").strip().lower()
total_belanja_awal = float(input("Masukkan total belanja: "))

# Inisialisasi diskon
diskon_persen = 0

# Logika perhitungan diskon
if member_status == "ya":
    if total_belanja_awal > 500000:
        diskon_persen = 10
    elif 100000 < total_belanja_awal <= 499999:
        diskon_persen = 5
    elif total_belanja_awal <= 100000:
        diskon_persen = 3
else:
    if total_belanja_awal > 100000:
        diskon_persen = 3

# Menghitung diskon dalam rupiah
diskon_rupiah = total_belanja_awal * (diskon_persen / 100)

# Menghitung total belanja setelah diskon
total_belanja_setelah_diskon = total_belanja_awal - diskon_rupiah

# Menampilkan hasil
print("\n========== Rincian Belanja ==========")
print(f"Nama Pelanggan           : {nama}")
print(f"Status Kartu Member      : {'Ya' if member_status == 'ya' else 'Tidak'}")
print(f"Total Belanja Sebelum Diskon: Rp {total_belanja_awal:,.2f}")
print(f"Diskon (dalam Persen)    : {diskon_persen}%")
print(f"Diskon (dalam Rupiah)    : Rp {diskon_rupiah:,.2f}")
print(f"Total Belanja Setelah Diskon: Rp {total_belanja_setelah_diskon:,.2f}")

