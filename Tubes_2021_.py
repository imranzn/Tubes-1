## Open & Read File
file = open("file teks.txt","r")
teks = file.readlines()

## Pembuatan Dictionary Kosong
klasemen={}

## Pembuatan Dictionary "klasemen"
for baris in teks:
    club1, goal1, goal2, club2 = baris.split()
    
    #KLUB KIRI
    if club1 in klasemen:
        #Total Main
        klasemen[club1][0] += 1

        #Total Menang, seri, kalah
        if int(goal1) > int(goal2):
            klasemen[club1][1] += 1
        elif int(goal1) == int(goal2):
            klasemen[club1][2] += 1
        elif int(goal1) < int(goal2) :
            klasemen[club1][3] += 1

        #Total Memasukkan gol
        klasemen[club1][4] += int(goal1)

        #Total Kemasukan gol
        klasemen[club1][5] += int(goal2)

        #Selisih Gol
        klasemen[club1][6] = int(klasemen[club1][4]) - int(klasemen[club1][5])
        if klasemen[club1][6]>0:
            klasemen[club1][6] = "+",str(klasemen[club1][6])
            klasemen[club1][6] = "".join(klasemen[club1][6])

        #Total Poin
        if int(goal1) > int(goal2):
            klasemen[club1][7] += 3
        elif int(goal1) == int(goal2):
            klasemen[club1][7] += 1
            
    #Klub yang belum terdaftar sebagai key    
    else:
        selisih = 0
        selisih = int(goal1)-int(goal2)
        if selisih>0:
            #Menambahkan "+" pada selisih gol, bahkan jika jumlah pertandingan cuma sekali
            selisih = "+",str(selisih)
            selisih = "".join(selisih)
            if int(goal1) > int(goal2):
                klasemen[club1] = [1, 1, 0, 0, int(goal1), int(goal2),selisih,3]
            elif int(goal1) == int(goal2):
                klasemen[club1] = [1, 0, 1, 0, int(goal1), int(goal2),selisih,1]
            elif int(goal1) < int(goal2):
                klasemen[club1] = [1, 0, 0, 1, int(goal1), int(goal2),selisih,0]
        else:
            if int(goal1) > int(goal2):
                klasemen[club1] = [1, 1, 0, 0, int(goal1), int(goal2),selisih,3]
            elif int(goal1) == int(goal2):
                klasemen[club1] = [1, 0, 1, 0, int(goal1), int(goal2),selisih,1]
            elif int(goal1) < int(goal2):
                klasemen[club1] = [1, 0, 0, 1, int(goal1), int(goal2),selisih,0]

    #KLUB KANAN    
    if club2 in klasemen:
        #Total Main
        klasemen[club2][0] += 1

        #Total Menang, seri, kalah
        if int(goal2) > int(goal1):
            klasemen[club2][1] += 1
        elif int(goal1) == int(goal2):
            klasemen[club2][2] += 1
        elif int(goal2) < int(goal1) :
            klasemen[club2][3] += 1

        #Total Memasukkan gol
        klasemen[club2][4] += int(goal2)

        #Total Kemasukan gol
        klasemen[club2][5] += int(goal1)

        #Selisih Gol
        klasemen[club2][6] = int(klasemen[club2][4]) - int(klasemen[club2][5])
        if klasemen[club2][6]>0:
            klasemen[club2][6] = "+",str(klasemen[club2][6])
            klasemen[club2][6] = "".join(klasemen[club2][6])

        #Total Poin
        if int(goal2) > int(goal1):
            klasemen[club2][7] += 3
        elif int(goal1) == int(goal2):
            klasemen[club2][7] += 1

    #Klub yang belum terdaftar sebagai key         
    else:
        selisih = 0
        selisih = int(goal2)-int(goal1)
        if selisih>0:
            #Menambahkan "+" pada selisih gol, bahkan jika jumlah pertandingan cuma sekali
            selisih = "+",str(selisih)
            selisih = "".join(selisih)
            if int(goal2) > int(goal1):
                klasemen[club2] = [1, 1, 0, 0, int(goal2), int(goal1),selisih,3]
            elif int(goal1) == int(goal2):
                klasemen[club2] = [1, 0, 1, 0, int(goal2), int(goal1),selisih,1]
            elif int(goal2) < int(goal1):
                klasemen[club2] = [1, 0, 0, 1, int(goal2), int(goal1),selisih,0]
        else:
            if int(goal2) > int(goal1):
                klasemen[club2] = [1, 1, 0, 0, int(goal2), int(goal1),selisih,3]
            elif int(goal1) == int(goal2):
                klasemen[club2] = [1, 0, 1, 0, int(goal2), int(goal1),selisih,1]
            elif int(goal2) < int(goal1):
                klasemen[club2] = [1, 0, 0, 1, int(goal2), int(goal1),selisih,0]

## Main Program
#Lebar Tabel = 71
#Panjang Tabel = Sesuai input
print("KLASEMEN PREMIER LEAGUE".center(71))
print("+", "-"*17, "+", "-"*51, "+", sep="")
print("|", "Nama Klub".center(17), "|", "MN".center(6), "|", "M".center(5), "|", "S".center(5), "|", "K".center(5), "|", "MG".center(6), "|","KG".center(6), "|", "SG".center(6), "|", "P".center(5), "|", sep="")
print("+", "-"*17, "+", "-"*51, "+", sep="")

#Print Isi Value dan Mengurutkannya berdasarkan value
for tim,poin in (sorted(klasemen.items(), key =lambda kv:(kv[1], kv[0]),reverse=True)):
    print("|", " ", tim.title().replace("_"," ").ljust(16), "|",
          (str(poin[0]).center(6)), "|",
          (str(poin[1]).center(5)), "|",
          (str(poin[2]).center(5)), "|",
          (str(poin[3]).center(5)), "|",
          (str(poin[4]).center(6)), "|",
          (str(poin[5]).center(6)), "|",
          (str(poin[6]).center(6)), "|",
          (str(poin[7]).center(5)), "|",
          sep="")
    
print("+", "-"*17, "+", "-"*51, "+", sep="")

## Close File
file.close()
