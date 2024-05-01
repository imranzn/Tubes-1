
#list
a = [3,2,1,5,4,"empat",(6,7)]

print(a[2])
print(a[-1])
print(a[-2])

print(a.index(2))
print(a.index(3))

print(4 in a)
if 4 in a:
    print(4,"sudah ada di dalam list")


sum_int = 0
for i in a:
    if isinstance(i,int):
        sum_int += i
        print("jumlah integer:",sum_int)

my_list = [90,80,95,85,85,100,88,98,79,80,(1,2,3)]
print(my_list[0:5]) # akan mengambil 5 elemen,  yaitu di index ke-0, 1, 2, 3, dan 4 (end-1).
print(my_list[-3:]) # akan mengambil elemen mulai dari index -3, sampai selesai. Jika <end> kosong, maka artinya sampai selesai.
print(my_list[:5])  # jika <start> kosong, maka artinya dimulai dari awal
print(my_list[3:5])




b = [1,"dua",3]
b.append("lima")#Menambah 1 buah elemen di akhir list
print(b)

b.extend(["enam",7,8])#Menambah beberapa elemen sekaligus di akhir elemen
print(b)

b.extend("halo")
print(b)

b.insert(3,"empat")#menambah satu buah item tertentu di posisi tertentu
print(b)

my_list = [90,80,95,85,85,100,88,98,79,80]
my_list[3] = 100000 # update 1 buah nilai
my_list[7:10] = [0,5,7] # update beberapa nilai sekaligus dengan slicing
print(my_list)

my_list = [90,80,95,85,85,100,88,98,79,80]

my_list.remove(80)#Menghapus berdasarkan nilai
print(my_list)

my_list.pop(4)#Menghapus bedasarkan index
print(my_list)

my_list.pop() # menghapus elemen terakhir yaitu 80
print(my_list)

nilai = my_list.pop(1) # pop akan mereturn nilai yang dikeluarkan dari list, sehingga bisa disimpan di sebuah variable untuk diproses lebih lanjut
print(nilai, my_list)

my_list.clear() # hapus semua elemen list
print(my_list)


#Tuple
my_tuple6 = (1, 2, 1, (4, 5), [1, 2])
#index,slicing,iterasi
print(my_tuple6[1])
print(my_tuple6[-1])
print(my_tuple6[3][1])
print(my_tuple6[1:4])
print(my_tuple6.index(2))
print((4, 5) in my_tuple6)

my_tuple = ("immutable", ["mutable1", "mutable2"]) # tuple immutable, namun elemen kedua tersebut adalah sebuah list yang mutable
try:
    my_tuple[1] = ["test", "test"] #akan menimbulkan error
except Exception as e:
    print('Error:', e)
my_tuple[1][0] = "mutable3" # tidak error
print(my_tuple)
my_tuple[1].append("mutable4") # juga diperbolehkan karena mengubah mutable object
print(my_tuple)

#set
my_set = {1, 2, 3}
my_set.add(5)#Menambah satu item 
print(my_set)

my_set.update([6, 7, 8])#Menambah banyak item
print(my_set)
try:
    my_set.add([9, 10])
except Exception as e:
    print('Error:', e)
my_set.add(tuple([9, 10]))
print(my_set)
#remove = menghapus elemen set,discard,pop
my_set = {1, 2, 3, 4}

my_set.remove(1)
print(my_set)
try:
    my_set.remove(5) # menimbulkan exception karena 5 tidak ada dalam set.
except Exception as e:
    print('Error:', e)

my_set.discard(4)
print(my_set)
    
my_set.discard(5) # tidak menimbulkan exception meskipun 5 tidak ada dalam set.
print(my_set)

p = my_set.pop()
print('pop1:', p, my_set)
q = my_set.pop()
print('pop2:', q, my_set)
r = my_set.pop() # menimbulkan exception karena set kosong, tidak ada nilai yang bisa di-pop
print('pop3:', r, my_set)

x = "jalan rumah si badu di samping jalan rumah ayu"
x.count("jalan")

#dictionary
a1 = "Imran,Zulkarnaen,Gagah"
print(a1.upper())

print(a1.lower())

print(a1.capitalize())

print(a1.title())

print(a1.casefold())




