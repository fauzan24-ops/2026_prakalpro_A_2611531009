print("=== SISTEM TRANSAKSI TOKO ===")

nama_pelanggan_1009 = input("Masukkan Nama Pelanggan : ")
status_pelanggan_1009 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_1009 = int(input("Masukkan Total Belanja : "))
jumlah_barang_1009 = int(input("Masukkan Jumlah Barang : "))
promo_1009 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan                      : ", nama_pelanggan_1009)
print("Status Pelanggan (member/nonmember) : ", status_pelanggan_1009)
print("Total Belanja                       : RP ", total_belanja_1009)
print("Jumlah Barang                       : ", jumlah_barang_1009)
print("Kode Promo                          : ", promo_1009)

kode_promo_1009 = ["HEMAT1", "HEMAT2", "GRATISONGKIR"]

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {total_belanja_1009 >= 200000}")
print(f"Jumlah Barang >= 3         : {jumlah_barang_1009 >= 3}")
print(f"Status Member              : {status_pelanggan_1009 == 'member'}")
print(f"Kode Promo Tersedia        : {promo_1009 in kode_promo_1009}")
print(f"Mendapatkan Diskon         : {jumlah_barang_1009 >= 3 or total_belanja_1009 >= 200000}")
print(f"Mendapatkan Promo          : {promo_1009 in kode_promo_1009}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                     : RP{0.15 * total_belanja_1009}")
print(f"Total Pembayaran           : RP{total_belanja_1009 - 0.15 * total_belanja_1009}")
print(f"Rata-rata Harga Barang     : RP{(total_belanja_1009 - 0.15 * total_belanja_1009) / jumlah_barang_1009}")

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses                         : ...")
print(f"Member Access                          : {status_pelanggan_1009 == 'member'}")
print(f"Promo Access                           : {promo_1009 in kode_promo_1009}")
print("Free Shipping Access                   : ...")

print("\n=== OPERASI BITWISE ===")
print("\n=== Kode Status Transaksi ===")
print(f"{format(int(status_pelanggan_1009 == 'member'), '04b')} | {format(int(total_belanja_1009 >= 200000) << 1, '04b')} | {format(int(jumlah_barang_1009 >= 3) << 2, '04b')} | {format(int(promo_1009 in kode_promo_1009) << 3, '04b')}")
print(f"Kode Biner : {format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3, '04b')}")
print(f"Kode Desimal : {int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3, '04b')} & {format(int(status_pelanggan_1009 == 'member') << 0, '04b')}")
print(f"Hasil Biner   : {format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3 & int(status_pelanggan_1009 == 'member') << 0, '04b')}")
print(f"Hasil Desimal : {int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3 & int(status_pelanggan_1009 == 'member') << 0}")

print("Cek Promo")
print(f"{format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3, '04b')} & {format(int(promo_1009 in kode_promo_1009) << 3, '04b')}")
print(f"Hasil Biner   : {format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3 & int(promo_1009 in kode_promo_1009) << 3, '04b')}")
print(f"Hasil Desimal : {int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3 & int(promo_1009 in kode_promo_1009) << 3}")

print("\n=== Perbandingan Status ===")
print(f"Kode transaksi : {format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3, '04b')}")
print("Kode Referensi : 1011")
print(f"{format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3, '04b')} ^ 1011 ")
print(f"Hasil Biner   : {format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3 ^ 1011, '04b')}")
print(f"Hasil Desimal : {int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3 ^ 1011}")

print("\n=== Shift ===")
print(f"{format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3, '04b')} << 1 ")
print(f"Hasil Biner   : {format(int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3 << 1, '04b')}")
print(f"Hasil Desimal : {int(status_pelanggan_1009 == 'member') << 0 | int(total_belanja_1009 >= 200000) << 1 | int(jumlah_barang_1009 >= 3) << 2 | int(promo_1009 in kode_promo_1009) << 3 << 1}")

print("\n=== SELESAI ===")

# == Penjelasan ==
# 1. Operator aritmatika

# Program menggunakan operator *, /, -, dan %.
# ("*") dan ("/") digunakan untuk menghitung diskon serta harga rata-rata barang.
# ("-") digunakan untuk menghitung total pembayaran setelah diskon.
# ("%") digunakan untuk mencari sisa pembagian total belanja dengan jumlah barang.

# 2. Perbedaan operator and, or, dan not

# * and digunakan jika semua kondisi harus terpenuhi. Contohnya, pelanggan harus menjadi member dan berbelanja minimal Rp200.000 untuk mendapatkan diskon.
# * or digunakan jika salah satu kondisi sudah terpenuhi.
# * not digunakan untuk membalik nilai kondisi, dari True menjadi False atau sebaliknya.

# 3. Fungsi operator in dan not in

# * in digunakan untuk memeriksa apakah kode promo terdapat dalam daftar promo.
# * not in digunakan untuk memeriksa apakah kode promo tidak terdapat dalam daftar.

# Contohnya, kode HEMAT1 terdapat dalam daftar promo, sehingga hasil pemeriksaan dengan in adalah True.

# 4. Perbedaan is dan == pada Python

# * is digunakan untuk memeriksa apakah dua variabel menunjuk objek yang sama.
# * == digunakan untuk membandingkan nilai dua variabel.

# Jadi, is membandingkan identitas objek, sedangkan == membandingkan isi atau nilainya.

# 5. Penggunaan operator bitwise untuk menentukan hak akses

# Operator bitwise digunakan untuk menyimpan kondisi pelanggan dalam bentuk biner.

# * | digunakan untuk menggabungkan beberapa kondisi.
# * & digunakan untuk memeriksa kondisi tertentu.
# * ^ digunakan untuk membandingkan dua nilai biner.
# * << digunakan untuk menggeser bit ke kiri.

# Contohnya, kode 1111 menunjukkan bahwa semua kondisi pelanggan terpenuhi.

