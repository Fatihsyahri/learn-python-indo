# Latihan perhitungan konversi suhu
# dari Fahrenheit ke Kelvin

# print("\nPROGRAM LATIHAN KONVERSI\n")
 
Fahrenheit = float(input('Masukan Suhu Fahrenheit : '))

# #celcius
Celscius = 5/9 * (Fahrenheit - 32)

# Konversi ke Kelvin
Kelvin = Celscius + 273
print("Suhu Dalam Kelvin adalah ",Kelvin, "Kelvin")

# Kelvin Ke Fahrenheit
Kelvin = float(input('Masukan Suhu Kelvin : '))

Celscius = Kelvin - 273

# Konversi Kelvin Ke Fahrenheit
Fahrenheit = 9/5*Celscius + 32

print("Suhu Dalam Fahrenheit adalah ",Fahrenheit, "Fahrenheit")

