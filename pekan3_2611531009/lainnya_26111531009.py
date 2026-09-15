print("=================================")
print("1. OPERATOR KEANGGOTAAN")
print("=================================")

input_data_1009 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

data_1009 = [int(angka.strip()) for angka in input_data_1009.split(",")]

nilai_dicari_1009 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1009 = nilai_dicari_1009 in data_1009
print("\nOperator keanggotaan IN")
print(nilai_dicari_1009, "in", data_1009, "=", hasil_1009)

# Operator not in
hasil_1009 = nilai_dicari_1009 not in data_1009
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1009, "not in", data_1009, "=", hasil_1009)

print("\n=================================")
print("2. OPERATOR IDENTITAS")
print("=================================")

objek1_1009 = data_1009

objek2_1009 = objek1_1009

objek3_1009 = data_1009.copy()

print("objek1_1009 =", objek1_1009)
print("objek2_1009 =", objek2_1009)
print("objek3_1009 =", objek3_1009)

# Operator is
hasil_1009 = objek1_1009 is objek2_1009
print("\nOperator Identitas IS")
print("objek1_1009 is objek2_1009 =", hasil_1009)

# Operator is not
hasil_1009 = objek1_1009 is not objek3_1009
print("\nOperator Identitas IS NOT")
print("objek1_1009 is not objek3_1009 =", hasil_1009)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_1009 is objek3_1009 =", objek1_1009 is objek3_1009)
print("objek1_1009 == objek3_1009 =", objek1_1009 == objek3_1009)
