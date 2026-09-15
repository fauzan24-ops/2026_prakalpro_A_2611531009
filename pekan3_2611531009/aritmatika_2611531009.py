angka1_1009 = int(input("input angka-1: "))
angka2_1009 = int(input("input angka-2: "))

# Penjumlahan
hasil_1009 = angka1_1009 + angka2_1009
print("\nOperator Penjumlahan")
print("Hasil =", hasil_1009)

# Pengurangan
hasil_1009 = angka1_1009 - angka2_1009
print("\nOperator Pengurangan")
print("Hasil =", hasil_1009)

# Perkalian
hasil_1009 = angka1_1009 * angka2_1009
print("\nOperator Perkalian")
print("Hasil =", hasil_1009)

# Pembagian, pembagian buat, dan sisa bagi
if angka2_1009 != 0:
    hasil_1009 = angka1_1009 / angka2_1009
    print("\nOperator Pembagian")
    print("Hasil =", hasil_1009)
    
    hasil_1009 = angka1_1009 // angka2_1009
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1009)
    
    hasil_1009 = angka1_1009 % angka2_1009
    print("\nOperator Sisa Bagi")   
    print("Hasil =", hasil_1009)
else:
    print("Angka kedua tidak boleh bernilai 0.")
    
# Pangkat
hasil_1009 = angka1_1009 ** angka2_1009
print("\nOperator Pangkat")
print("Hasil =", hasil_1009)
