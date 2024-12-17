# menghitungan BMI 

# input data tetap
# Data tetap
berat = 55  # berat badan dalam kilogram
tinggi = 171  # tinggi badan dalam sentimeter

# Mengonversi tinggi dari cm ke meter
tinggi = tinggi / 100

# Menghitung BMI
bmi = berat / (tinggi ** 2)

# Menentukan kategori BMI
if bmi < 18.5:
    kategori = "Kekurangan berat badan"
elif 18.5 <= bmi < 24.9:
    kategori = "Normal"
elif 25 <= bmi < 29.9:
    kategori = "Kelebihan berat badan"
else:
    kategori = "Obesitas"

# Menampilkan hasil
print(f"skor BMI Anda adalah: {bmi:.2f}")
print(f"Kategori: {kategori}")

