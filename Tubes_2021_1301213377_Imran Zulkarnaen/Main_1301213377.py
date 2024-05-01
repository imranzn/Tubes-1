#Membuka dan Membaca file
file = open("File.txt", "r")
teks = file.readlines()

#Pembuatan List kosong
penjualan = []

#Pembuatan List "penjualan"
for baris in teks:
    penjual,Senin,Selasa,Rabu,Kamis,Jumat = baris.split()
    penjualan.append({penjual:[int(Senin)*1000,int(Selasa)*1000,int(Rabu)*1000,int(Kamis)*1000,int(Jumat)*1000]})       

#Pembuatan fungsi "penghasilan"
def penghasilan(list_penjualan,nama_penjual):
    for penjual in list_penjualan:
        for nama,perhari in penjual.items():
            if nama_penjual in nama:
                jumlah_penghasilan = 0
                indeks = 0
                #Senin
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah_penghasilan += 100000 + (cek_hari*0.025)
                else:
                    jumlah_penghasilan += 100000
                #Selasa
                indeks +=1
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah_penghasilan += 100000 + (cek_hari*0.025)
                else:
                    jumlah_penghasilan += 100000
                #Rabu
                indeks +=1
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah_penghasilan += 100000 + (cek_hari*0.025)
                else:
                    jumlah_penghasilan += 100000
                #Kamis
                indeks +=1
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah_penghasilan += 100000 + (cek_hari*0.025)
                else:
                    jumlah_penghasilan += 100000
                #Jumat
                indeks += 1
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah_penghasilan += 100000 + (cek_hari*0.025)
                else:
                    jumlah_penghasilan += 100000
                    

                return jumlah_penghasilan

                
#Pembuatan fungsi "bonus"
def bonus(list_penjualan):
    for penjual in list_penjualan:
        for nama in penjual:
            jumlah_penjualan = sum(penjual[nama])
            if jumlah_penjualan > 20000000:
                dapat_bonus = int(penghasilan(penjualan,nama)+1000000)
                print(nama, "Dengan Total Penjualan dalam Seminggu adalah Rp.{:,} Mendapatkan bonus sebanyak Rp.1.000.000, sehingga mendapatkan total penghasilan Rp.{:,}".format(jumlah_penjualan,dapat_bonus))
            
    

#Main Program
print("Data Penjual dan Penjualan Perhari:")
for mydict in penjualan:
    for k,v in mydict.items():
        print(k, v)

print()

print("Total Penghasilan:")
for mydict in penjualan:
    for k,v in mydict.items():
        print(k, "Mendapatkan Rp.{:,}".format(int(penghasilan(penjualan,k))))

print()

print("Bonus:")
bonus(penjualan)

#Menutup file
file.close()
