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
def penghasilan(list_penjualan):
    for penjual in list_penjualan:
        for nama,perhari in penjual.items():
            jumlah = 0
            indeks = 0
                #Senin
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah += 100000 + (cek_hari*0.025)
                else:
                    jumlah += 100000
                #Selasa
                indeks +=1
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah += 100000 + (cek_hari*0.025)
                else:
                    jumlah += 100000
                #Rabu
                indeks +=1
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah += 100000 + (cek_hari*0.025)
                else:
                    jumlah += 100000
                #Kamis
                indeks +=1
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah += 100000 + (cek_hari*0.025)
                else:
                    jumlah += 100000
                #Jumat
                indeks += 1
                cek_hari = perhari[indeks]
                if cek_hari > 0 :
                    jumlah += 100000 + (cek_hari*0.025)
                else:
                    jumlah += 100000
                    

                return jumlah
                
            print(nama, "\t :Rp.{:,}".format(int(jumlah)))

            #Reset
            indeks = 0
            jumlah = 0
                
#Pembuatan fungsi "bonus"
def bonus(list_penjualan):
    for penjual in list_penjualan:
        for nama in penjual:
            jumlah_penjualan = sum(penjual[nama])
            if jumlah_penjualan > 20000000:
                print(nama, "Dengan Total Penjualan dalam Seminggu adalah Rp.{:,} Mendapatkan bonus sebanyak 1.000.000, sehingga mendapatkan total penghasilan...".format(jumlah_penjualan))
    


#Main Program
print("Total Penghasilan :")
penghasilan(penjualan)
print("Bonus :")
bonus(penjualan)

#Menutup file
file.close()
