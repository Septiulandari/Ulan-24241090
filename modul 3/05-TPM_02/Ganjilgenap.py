# Meminta input dari pengguna
angka = int(input("Masukkan sebuah angka: "))

# Menentukan apakah angka ganjil atau genap
if angka % 2 == 0:
    hasil = "genap"
else:
    hasil = "ganjil"

# Cetak hasil awal
print("===HASIL Ganjil atau Genap===")
print("Hasil =", hasil, "type =", type(hasil))
