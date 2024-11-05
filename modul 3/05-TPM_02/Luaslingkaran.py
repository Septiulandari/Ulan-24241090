import math

# Fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(radius):
    return math.pi * radius ** 2

# Input radius dari pengguna
radius_input = input("Masukkan radius lingkaran: ")

# Konversi input dari string ke float
radius_float = float(radius_input)

# Hitung luas lingkaran
luas_lingkaran = hitung_luas_lingkaran(radius_float)

# Tampilkan hasil luas lingkaran
print("Luas lingkaran dengan radius", radius_float, "adalah:", luas_lingkaran)

