def suhu_ke_fahrenheit(suhu_celsius):
    # Menghitung suhu dalam Fahrenheit
    return (suhu_celsius * 9/5) + 32

# Meminta input dari pengguna
suhu_celsius = float(input("Masukkan suhu dalam Celsius: "))

# Menghitung suhu dalam Fahrenheit
suhu_fahrenheit = suhu_ke_fahrenheit(suhu_celsius)

# Menampilkan hasil
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit:.2f} °F")
