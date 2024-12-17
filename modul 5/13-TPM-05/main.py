# Program untuk menentukan diskon berdasarkan kartu member dan jumlah belanja

# Input dari pengguna
kartu_member = input("Apakah Anda punya kartu member? (ya/tidak): ").strip().lower()
belanja = float(input("Berapa total belanja Anda? (dalam rupiah): "))

# Logika perhitungan diskon
if kartu_member == "ya":
    if belanja > 500000:
        diskon = 50000
    elif belanja > 100000:
        diskon = 15000
    else:
        diskon = 0
else:
    if belanja > 100000:
        diskon = 10000
    else:
        diskon = 0

# Output hasil
if diskon > 0:
    print(f"Selamat! Anda mendapatkan diskon sebesar Rp{diskon}.")
else:
    print("Maaf, Anda tidak mendapatkan diskon.")