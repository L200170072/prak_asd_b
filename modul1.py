""" Nam  : Avifah Hasna Nur Fadila
    NIM  : L200170072
    Kelas : B"""






#No1
def segitiga():
    for p in range (5):
        for i in range (p+1):
            print ("*", end='')
        print ()
    return(p)
segitiga()

#No2
def kotak(a,b):
    for i in range (a):
        if i == 0 or i == a-1:
            print("@"*a)
        else:
            x = a-b
            print ("@"+" "*(a-2)+"@")
kotak (4,5)


#No3 A
def jmlvokal(string):
    vok= 0
    x = "aiueoAIUEO"
    for car in string.lower():
        if car in x:
            vok +=1
    vokal = len(string)
    return(vokal,vok)

#N03 B
def jmlvok(string):
    vok = 0
    x = "aiueoAIUEO"
    for car in string.lower():
        if car not in x:
            vok += 1
    vokal = len(string)
    return(vokal,vok)


#No4
def rerata(b):
    sum = 0
    for i in b :
        sum += i
    return (sum/len(b))

#No5
from math import sqrt as sq
def apakahprima(n):
    n = int(n)
    assert n>=0
    primakecil = [2,3,5,7,11]
    bukanprkecil = [0,1,4,6,8,9,10]
    if n in primakecil:
        return True
    elif n in bukanprkecil:
        return False
    else:
        #angka=[]
        hasil=[]
        for i in range (2, int(sq(n))+1):
                if i in primakecil:
                    hasil.append(True)
                elif i in bukanprkecil:
                    hasil.append(False)
                #angka.append(i)
        return hasil
print(apakahprima(20))


#No6
low = 2
up = 1000
for num in range(low,up+1):
    if num>1:
        for i in range(2,num):
            if(num%i == 0):
                break
        else:
            print(num)



#nomor7
def faktorPrima(x) : # x adalah bilangan yang diinputkan untuk di dicari faktor prima nya
    a = []  #untuk menyimpan bilangan prima
    b = []  #untuk menyimpan faktor prima dari bilangan yg diinputkan
    hasil = 0
    bil = x
    prima =True
    for i in range(2,x):
        prima = True
        for u in range(2, i) :
            if i % u == 0 :
               prima = False
        if prima :
            a.append(i)     #menambahkan bilangan prima ke variabel a
    idx = 0
    while bil > 1 :      
        try:    #try untuk mengatasi error ketika index out of range,msal list pnya 5 data maka ketika mengindex data ke6 akan error.
            if (bil%a[idx]) == 0 : # a[idx] untuk mengambil bilangan prima dari list a berdasarkan indexing nya
                hasil = bil/a[idx]
                bil = hasil
                b.append(a[idx])#memasukkan faktor primanya ke 'b'
            else :
                idx = idx + 1
        except IndexError :
            break
    print (b)

#nomor8
def apakahTerkandung(h,k):
    return h.lower() in k.lower()

#nomor9
def ProgCetakAngka(n):
    i = 0
    for i in range (n):
        if i % 3 == 2 and i % 5 == 4:
            print("Python UMS")
        elif i % 3 == 2:
            print("Python")
        elif i % 5 == 4:
            print("UMS")
        else:
            print(i + 1)

#nomor10
def selesaikanABC(a,b,c):
    if a <= 0 and b <= 0 and c <= 0:
        print("Determinannya Positif. Persamaan mempunyai akar Real")
    else:
        print("Determinannya Negatif. Persamaan tidak mempunyai akar Real")

#nomor11
import datetime;
def apakahKabisat(n):
    if (n % 4) == 0:
        if (n % 100) == 0:
            if (n % 400) == 0:
                print ("Tahun Kabisat")
            else:
                print("Bukan Tahun Kabisat")
        else:
            print("Tahun Kabisat")
    else:
        print("Bukan Tahun Kabisat")

#nomor12
angka = 25

print("Permainan Tebak Angka")
print("Ssya  Menyimpan Sebuah Angka bulat Antara 1 sampai 100. Coba tebak")

while angka != -1:

    masukkan =  int(input("Masukan Tebakan :>"))

    if masukkan == angka:
        print("Ya. Anda Benar", angka)
        break
    elif masukkan > angka:
        print("Itu Terlalu Besar. Coba Lagi")
    elif masukkan < angka:
        print("Itu Terlalu Kecil. Coba Lagi")

#nomor13
def katakan(bil):
    angka = ["","Satu ","Dua ","Tiga ","Empat ","Lima ","Enam ",
             "Tujuh ","Delapan ","Sembilan ","Sepuluh ","Sebelas "]
    hasil = ""
    n = int(bil)
    if n >= 0 and n <= 11:


        hasil = angka[n]
    elif n < 20:
        hasil = katakan(n-10) + "Belas "
    elif n < 100:
        hasil = katakan(n/10) + "Puluh " + katakan(n%10)
    elif n < 200:
        hasil = "Seratus " + katakan(n-100)
    elif n < 1000:
        hasil = katakan(n/100) + "Ratus " + katakan(n%100)
    elif n < 2000:
        hasil = "Seribu " + katakan(n-1000)
    elif n < 1000000:
        hasil = katakan(n/1000) + "Ribu " + katakan(n%1000) 
    elif n < 1000000000:
        hasil = katakan(n/1000000) + "Juta " + katakan(n%1000000)
    elif n > 1000000000:
        hasil = 'Maaf, program tidak membaca angka lebih dari Satu Milyar'
    return hasil


a = 1
while a != 0:
    a = input(' Masukkan angka dari 1 sd 1.000.000.000: ')
    huruf = katakan(a)
    print(huruf +'Rupiah')
    break

#nomor14
def formatRupiah(n):
    y = str(n)
    if len(y) <= 3 :
        return 'Rp ' + y     
    else :
        p = y[-3:]
        q = y[:-3]
        return   (formatRupiah(q) + '.' + p)
        print ('Rp' +  (formatRupiah(q)) + '.' + p) 


    
