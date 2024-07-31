kasir = input("Masukkan Nama Kasir : ")
pembeli = input("Masukkan Nama Pembeli : ")
jenis = int(input("Masukkan Jenis Kopi Yang Akan Dibeli : "))

kode = []
jumlah = []
harga = []
nama = []
total = []

i = 0

while i < jenis:
    print("Data Ke-", i + 1)
    kode.append(int(input("Masukan Kode Kopi : ")))
    jumlah.append(int(input("Masukan Jumlah Pembelian : ")))
    if kode[i] == 1:
        nama.append("Espressoo")
        harga.append(15000)
        total.append(jumlah[i]*15000)
    elif kode[i] == 2:
        nama.append("FlatWhite")
        harga.append(30000)
        total.append(jumlah[i]*30000)
    elif kode[i] == 3:
        nama.append("Piccolooo")
        harga.append(35000)
        total.append(jumlah[i]*35000)
    elif kode[i] == 4:
        nama.append("Macchiatoo")
        harga.append(45000)
        total.append(jumlah[i]*45000)
    elif kode[i] == 5:
        nama.append("Cold Brew")
        harga.append(50000)
        total.append(jumlah[i] * 50000)
    else:
        nama.append("Jenis Kopi Tidak Tersedia")
        harga.append(0)
        total.append(0)
    
    i = i + 1 

print("-------------------------------------------------------")
print("                      El's Coffee")
print("-------------------------------------------------------")
print("=======================================================")
print("=== Nama Kasir        :",kasir)
print("=== Nama Pembeli      :",pembeli)
print("=======================================================")
print("Kode   Nama         Harga     Jumlah    Total  ")
print("=======================================================")
totalbayar = 0
a = 0
while a < jenis:
    totalbayar += total[a]
    print("%i      %s    %i       %i       %i "% (kode[a], nama[a], harga[a], jumlah[a], total[a]))
    a += 1
print("=======================================================")
print("Anda Harus Membayar   : Rp.", totalbayar)
uang = int(input("Masukan Uang Bayar    : "))
kembalian = uang - totalbayar
print("Kembalian             :",kembalian)
print("======= Terima kasih Sudah Mengunjungi Toko Kami =======")
