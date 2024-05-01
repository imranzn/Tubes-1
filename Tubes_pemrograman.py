# Membuka dan Membaca file
file = open("File.txt", "r")
teks = file.readlines()

#Pembuatan List kosong
penjualan = []

#Pembuatan List "penjualan"
for baris in teks:
    penjual,Senin,Selasa,Rabu,Kamis,Jumat = baris.split()
    penjualan.append({penjual:[int(Senin),int(Selasa),int(Rabu),int(Kamis),int(Jumat)]})       

#Pembuatan fungsi "penghasilan"
def penghasilan(list_penjualan):
    for penjual in list_penjualan:
        for value in penjual:
            jumlah_penjualan = sum(penjual[value]*1000)
            if jumlah_penjualan > 20000000:
                total_penjualan = "{:,}".format((100000 +(0.025 * jumlah_penjualan)))
            else:
                total_penjualan = "{:,}".format((100000 +(0.025 * jumlah_penjualan)))                  
            total_penjualan = value,":",total_penjualan
            print("\t".join(total_penjualan))
            
#Pembuatan fungsi "bonus"






#Main Program
penghasilan(penjualan)

#Menutup file
file.close()
