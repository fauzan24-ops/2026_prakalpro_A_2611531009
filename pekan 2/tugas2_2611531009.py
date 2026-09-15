print("=== SISTEM REGISTRASI PRAKTIKUM ALPRO 2026 ===")

nama_1009 = input("Masukkan nama Mahasiswa: ")
jenis_kelamin_1009 = input("Masukkan jenis kelamin: ")
umur_1009 = int(input('Masukkan umur: '))
skor_tes_awal_1009 = float(input('Masukkan skor tes awal: '))

print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
 
nama_1009 = 'Muhammad Fauzan'
jenis_kelamin_1009 = 'L'
alamat_domisili_1009 = """
    Jl. Bypass Km.15
    Air Pacah,
    Koto Tangah
"""
umur_1009 = '18'
skor_tes_awal_1009 = '82.5'
id_token_sinyal = "100 +300j"

print('Nama Mahasiswa : ', nama_1009)
print('Jenis Kelamin :', jenis_kelamin_1009)
print('Alamat Domisili :', alamat_domisili_1009)
print('Umur :', umur_1009)
print('Skor Tes Awal :', skor_tes_awal_1009)
print('ID Token Sinyal: ', id_token_sinyal)

print("=== STATUS KELULUSAN PRAKTIKUM ===")

batas_nilai_1009 = input('Batas Minimum Nilai : ')
print("skor_tes_awal_1009 >= batas_nilai_1009: ", "true")