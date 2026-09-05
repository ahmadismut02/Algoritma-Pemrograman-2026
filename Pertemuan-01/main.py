import math
# Input
r = float(input("masukkan jari-jari lingkaran (r)"))

# Proses perhitungan
luas = math.pi * (r ** 2)
keliling = 2 * math.pi * r

# Output
print (f"\nHasil Perhitungan:")
print (f"Jari-jari          :{r} ")
print (f"Luas Lingkaran     :{luas:.2f}")
print (f"Keliling Lingkaran :{keliling:.2f}")