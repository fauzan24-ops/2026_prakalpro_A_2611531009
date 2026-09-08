is_lulus = True
is_cumlaude = False

nilai_1009 = 85
batas_lulus_1009 = 75

status_kelulusan_1009 = nilai_1009 >= batas_lulus_1009 #hasilnya true

print("=== Check Keulusan ===")
print("Nilai:", nilai_1009)
print("Apakah lulus?:", status_kelulusan_1009)
if is_lulus and is_cumlaude:
    print("Selamat, anda lulus dengan predikat cumlaude!")
    