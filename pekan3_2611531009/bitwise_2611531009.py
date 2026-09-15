print("\n================================")
print("3. OPERATOR BITWISE")
print("================================")

angka1_1009 = int(input("Masukkan angka bitwise-1: "))
angka2_1009 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_1009 =", angka1_1009, "| biner =", bin(angka1_1009))
print("angka2_1009 =", angka2_1009, "| biner =", bin(angka2_1009))

# Bitwise AND
hasil_1009 = angka1_1009 & angka2_1009
print("\nBitwise AND (&)")
print(angka1_1009, "&", angka2_1009, "=", hasil_1009)
print("Biner hasil_1009 =", bin(hasil_1009))
print("Biner hasil (8 bit) =", format(hasil_1009, "08b"))

# Bitwise OR
hasil_1009 = angka1_1009 | angka2_1009
print("\nBitwise OR (|)")
print(angka1_1009, "|", angka2_1009, "=", hasil_1009)
print("Biner hasil =", bin(hasil_1009))
print("Biner hasil (8 bit) =", format(hasil_1009, "08b"))
