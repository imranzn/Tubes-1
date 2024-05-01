# Membuka dan Membaca file
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
                jumlah = 0
                indeks = 0
                total_penjualan = 0
                #Senin
                cek_hari = perhari[indeks]
                if cek_hari >= 0 :
                    total_penjualan += (cek_hari*0.025)
                    jumlah =  total_penjualan + 100000
                else:
                    jumlah += 100000
                indeks +=1
                #Selasa
                cek_hari = perhari[indeks]
                if cek_hari >= 0 :
                    total_penjualan += (cek_hari*0.025)
                    jumlah =  total_penjualan + 100000
                else:
                    jumlah += 100000
                indeks +=1
                #Rabu
                cek_hari = perhari[indeks]
                if cek_hari >= 0 :
                    total_penjualan += (cek_hari*0.025)
                    jumlah =  total_penjualan + 100000
                else:
                    jumlah += 100000
                indeks +=1
                #Kamis
                cek_hari = perhari[indeks]
                if cek_hari >= 0 :
                    total_penjualan += (cek_hari*0.025)
                    jumlah =  total_penjualan + 100000
                else:
                    jumlah += 100000
                indeks +=1
                #Jumat
                cek_hari = perhari[indeks]
                if cek_hari >= 0 :
                    total_penjualan += (cek_hari*0.025)
                    jumlah =  total_penjualan + 100000
                else:
                    jumlah += 100000
                indeks +=1
                
                
                return jumlah

                
#Pembuatan fungsi "bonus"
def bonus(list_penjualan):
    for penjual in list_penjualan:
        for nama in penjual:
            jumlah_penjualan = sum(penjual[nama])
            if jumlah_penjualan > 20000000:
                dapat_bonus = int(penghasilan(penjualan,nama)+1000000)
                print(nama, "Dengan Total Penjualan dalam Seminggu adalah Rp.{:,} Mendapatkan bonus Rp.1.000.000, sehingga total penghasilannya Rp.{:,}".format(jumlah_penjualan,dapat_bonus))
            
    

#Main Program
print("PRAMUNIAGA".center(140))
print("Data Penjual dan Penjualan Perhari")
for mydict in penjualan:
    for k,v in mydict.items():
        print(k, v)

print()

print("Total Penghasilan")
for mydict in penjualan:
    for k,v in mydict.items():
        print(k, "Mendapatkan Rp.{:,}".format(int(penghasilan(penjualan,k))))

print()

print("Bonus")
bonus(penjualan)

#Menutup file
file.close()
