# di python juga menggunakan aritmetika sederhana yaitu aritmatik operator
# =====ARITMETIK OPERATOR======
# "+" = penjumlahan
# "-" = pengurangan
# "*" = pengkalian
# "/" = pembagian dengan hasil ada komanya contoh 5/2 = 2.5
# "//" = pembagian juga hanya saja hasilnya integer alias tak berkoma contoh 5//2 = 2
# "%" = artinya sendiri 'sisa bagi' cnth: 7 % 3 maka sisa baginya = 1
# "**" = lebih dikenal dengan 'pangkat'

angka1 = 10
angka2 = 5

print("hasil penjumlahan: " + str(angka1+angka2))
print(angka1%angka2)
print(10**5)

# ===== Assignment Operator=====
# ini kurang lebih sama kayak sebelumnya hanya saja bagian ini seperti penyingkatan syntax 
# untuk operator saya lampirkan fotonya

angka = 5
print("angka sebelum ditambah: " + str(angka))

angka += 10
print("angka setelah ditambah: " + str(angka))


# python juga memiliki module atau library yg disebut Math
# ===== MATH ========
import math #panggil dulu library nya
# Using methods
print(math.pow(2, 3)) #ini makksdnya adalah 2 pangkat 3
print(math.ceil(3.2)) #ini untuk membulatkan keatas
print(math.floor(3.2)) # ini membulatkan kebawah
print(math.sqrt(36)) #ini untuk akar dari

# Using Constants
print(math.pi)

# prioritas perhitungan juga sama seperti matematika pada umumnya, contoh
x = 3
y = 4
z = 5
'''
1. ()
2. exponen **
3. Perkalian dkk seperti * // ** % /
4. Pertambahan dan pengurangan
'''
hasil = (x - y) * z
print(x,"-",y,"*",z,"=",hasil)

