a1_1009 = input("Input nilai boolean_1 (True/False): ").strip().lower() == "True"
a2_1009 = input("Input nilai boolean_2 (True/False): ").strip().lower() == "True"

print("\nA1 =", a1_1009)
print("A2 =", a2_1009)

# konjungsi : bernilai true jika kedua operand bernilai true
hasil_1009 = a1_1009 and a2_1009
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_1009)

# Disjungsi : bernilai true jika salah satunya true
hasil_1009 = a1_1009 or a2_1009
print("\nDisjungsi (OR)")
print("A1 or A2=", hasil_1009)

hasil_1009 = not a1_1009
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_1009)

hasil_1009 = not a2_1009
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_1009)

hasil_1009 = a1_1009 != a2_1009
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2 =", hasil_1009)
