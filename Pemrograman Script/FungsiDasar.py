# Fungsi-fungsi dasar Python

# print() → menampilkan output
print("Halo, Dunia!")

# input() → menerima input dari user
nama = input("Masukkan nama Anda: ")
print("Halo,", nama)

# type() → menampilkan tipe data
angka = 42
print("Tipe data angka:", type(angka))

# len() → menghitung panjang data
teks = "Pemrograman Python"
print("Jumlah karakter:", len(teks))

# int(), float(), str() → konversi tipe data
angka_str = "123"
print("String ke Integer:", int(angka_str))
print("String ke Float:", float(angka_str))
print("Integer ke String:", str(456))

# max() dan min() → mencari nilai terbesar dan terkecil
data = [10, 5, 8, 20, 3]
print("Nilai terbesar:", max(data))
print("Nilai terkecil:", min(data))

# sum() → menjumlahkan semua elemen dalam list
print("Jumlah total data:", sum(data))
