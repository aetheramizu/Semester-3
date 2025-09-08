# Fungsi tanpa parameter dan tanpa nilai kembali
def sapa():
    print("Halo, selamat datang di kelas pemrograman!")

# Contoh penggunaan
sapa()

# Fungsi dengan parameter dan tanpa nilai kembali
def sapa_nama(nama):
    print(f"Halo {nama}, have a nice day twin")

# Contoh penggunaan
sapa_nama("Alief")
sapa_nama("Rex")

# Fungsi tanpa parameter tetapi dengan nilai kembali
def ambil_nama():
    return "Alief"

# Contoh penggunaan
nama = ambil_nama()
print(f"Nama yang diambil adalah: {nama}")

# Fungsi dengan parameter dan dengan nilai kembali
def tambah(a, b):
    return a + b

# Contoh penggunaan
hasil = tambah(6, 7)
print(f"Hasil penjumlahan adalah: {hasil}")
