angka1_1009 = int(input("input angka-1: "))
angka2_1009 = int(input("input angka-2: "))

print("\nNilai awal angka1_1009 =")
print("Nilai angka2_1009 =", angka2_1009)

# Assignment Biasa
hasil_1009 = angka1_1009 
print("\nAssignment Biasa (=)") 
print("Hasil =", hasil_1009)

# Assignment Penjumlahan (+=)
hasil_1009 = angka1_1009 
hasil_1009 += angka2_1009
print("\nAssignment Penjumlahan (+=)")
print("Hasil =", hasil_1009)

# Assignment Pengurangan (-=)
hasil_1009 = angka1_1009
hasil_1009 -= angka2_1009
print("\nAssignment Pengurangan (-=)")
print("Hasil =", hasil_1009)

# Assignment Perkalian (*=)
hasil_1009 = angka1_1009
hasil_1009 *= angka2_1009
print("\nAssignment Perkalian (*=)")
print("Hasil =", hasil_1009)
 
# Assignment Pembagian, pembagian bulat, dan sisa bagi 
if angka2_1009 != 0:
    hasil_1009 = angka1_1009
    hasil_1009 /= angka2_1009
    print("\nAssignment Pembagian (/=)")
    print("Hasil =", hasil_1009)
    
    hasil_1009 = angka1_1009
    hasil_1009 //= angka2_1009
    print("\nAssignment Pembagian Bulat (//=)")
    print("Hasil =", hasil_1009)
    
    hasil_1009 = angka1_1009
    hasil_1009 %= angka2_1009
    print("\nAssignment Sisa Bagi (%=)")   
    print("Hasil =", hasil_1009)
else:
    print("Pembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")
    
# Assignment Pangkat (**=)
hasil_1009 = angka1_1009
hasil_1009 **= angka2_1009
print("\nAssignment Perpangkatan (**=)")
print("Hasil =", hasil_1009)

