
"""Nama : avifah hasna nur fadila
    nim : L200170072"""

#Soal 1
#A

class Pesan(object):        
    """Sebuah kelas bernama pesan .
        untuk memeriksa suatu str terkandung di dlmnya atau tidak"""
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print ("Kalimatku mempunyai " , len(self.teks), 'karakter.')
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, a):
        if a in self.teks:
            return True
        else:
            return False

#B
    def hitungKonsonan(self): 
        a = 0
        x = 'aiueoAIUEO'
        for i in self.teks:
            if i  not in x :
                a += 1
        return a

#C
    def hitungVokal(self): 
        a = 0
        x = 'aiueoAIUEO'
        for i in self.teks:
            if i in x:
                a += 1
        return a


#Soal 2
    # A . Metode mengambil kota tempat tinggal
class mahasiswa(object):
    "berisi biodata mahasiswa"
    def __init__(self, nama, KotaTinggal, UangSaku):
        self.nama = nama
        self.KotaTinggal = KotaTinggal
        self.UangSaku = UangSaku
    def ambilKotaTinggal(self):
        print(self.KotaTinggal)

    #B . Metode untuk memperbarui kota tinggal
    def perbaruiKotaTinggal(self, stringBaru):
        self.KotaTinggal = stringBaru
    def ambilUangSaku(self):
        print (self.UangSaku)

    #C. metod menambah uang saku
    def tambahUangSaku(self, intBaru): 
        x = self.UangSaku + intBaru
        return x
        
m9= mahasiswa ('avifah' , 'solo', 5000)
m9.ambilKotaTinggal



#Soal 3
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2


class Mahasiswa(Manusia):
    """Class yang dibangun dari class Mahasiswa"""

    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
        
    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUangSaku):
        self.us = self.us + tambahUangSaku
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'

a = input("Masukkan nama: ")
b = input("Masukkan nim: ")
c = input("Masukkan kota tinggal: ")
d = input("Masukkan uang saku: ")

x = Mahasiswa(a,b,c,d)
print (x)



#Soal 4
class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, e):
        """Metode ini menutupi metode 'makan'-nya class manusia.
           Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s, "Sambil belajar.")
        self.keadaan = 'kenyang'

    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal = ubah
    def tambahUangSaku(self, tambah):
        self.uangSaku += tambah

    listKuliah = []
    def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
    


#Soal 5
class Mahasiswa(Manusia):
    """Class yang dibangun dari class Mahasiswa"""

    def __init__(self, nama, NIM, kota, us, lk = []):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nim = NIM
        self.kota = kota
        self.us = us
        self.listkuliah = lk

    def __str__(self):
        s = self.nama +', NIM '+str(self.nim)\
            +'. Tinggal di '+ self.kota \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap bulannya.'
        return s
    
    def ambilNama(self):
        return self.nama
    def ambilNim(self):
        return self.nim
    def ambilUangSaku(self):
        return self.us
    def tambahUangSaku(self, tambahUang):
        self.us = self.us + tambahUang
    def ambilKotaTinggal(self):
        return self.kota
    def perbaruiKotaTinggal(self, kotabaru):
        self.kota = kotabaru
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau sambil belajar ."""
        print("Saya baru saja makan",s,"sambil belajar")
        self.keadaan = 'kenyang'
    def ambilKuliah(self, ambil):
        self.listkuliah.append(ambil)
    def hapusListKuliah(self, hapus):
        for x in self.listkuliah:
            if hapus in self.listkuliah:
                self.listkuliah.remove(hapus)
            else:
                print("Maaf mata kuliah tidak ada dalam list mata kuliah yang diambil")

m1 = Mahasiswa('avifah', 111, 'Surakarta', 700000)
m2 = Mahasiswa('pipo', 909, 'skh', 450000)
m3 = Mahasiswa('fida', 876, 'pwd', 900000)



#Soal 6
from datetime import date
class Manusia(object):
    """Class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = 'lapar'
    
    def __ini__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print('Salam, namaku',self.nama)
    def makan(self, s):
        print('Saya baru saja makan', s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print('Saya baru saja latihan', k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self, nama, NISN, umur, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.nisn = NISN
        self.umur = umur
        self.us = us
        
    def __str__(self):
        s = self.nama +', NIS '+str(self.nisn)\
            +'. Berumur '+ str(self.umur) \
            +'. Uang saku Rp. '+ str(self.us)\
            +' tiap harinya.'
        return s

    def tahunlahir(self):
        thnskr = date.today().year
        tl = thnskr - self.umur
        return tl

#Soal 7
    
Class Manusia = Parent Class
Mahasiswa = SubClass dari Manusia
MhsTIF = SuBclass dari Class Mahasiswa, Class (MhsTIF) ini parent classnya(Manusia)
**
    Manusia-> ParentClass (SuperClass)
    Mahasiswa-> SubClass induknya adalah Class (Manusia)
    MhsTIF -> SubClass induknya adalah Class(Mahasiswa)

a.NIM = """ Untuk Membuat Object Yang Akan Menampilkan Nim Mahasiswa yang hanya bisa menampilkan parameter yang ada di def __init__ yang Berada
            di class Mahasiswa """

a.ambilNim = """Untuk Membuat Object Yang Akan Menjalankan methods ambilNim(self) Mahasiswa yang Ada di class Mahasiswa yang akan meminta data dari fungsi
            def __init__ yang berada di class Mahasiswa"""

a.ambilNama = """Untuk Membuat Object Yang Akan Menjalankan methods ambilNama(self) Mahasiswa yang Ada di class Mahasiswa yang akan meminta data dari fungsi
                def __init__ yang berada di class Mahasiswa"""

a.ambilUangSaku = """Untuk Membuat Object Yang Akan Menjalankan methods ambiUangSaku(self) Mahasiswa yang Ada di class Mahasiswa yang akan meminta data dari
                    fungsi def __init__ yang berada di class Mahasiswa"""

a.katakanPy = """Untuk Membuat Object Yang Akan Menjalankan methods katakanPy(self) yang Berada di class MhsTIF """

a.keadaan = """Untuk Membuat Object Yang Akan Menjalankan ClassVariable, dan akan menampilkan sisi dari ClassVariable tersebut, ClassVariable Tersebut Berada
            di dalam Class Manusia"""

a.kotaTinggal = """Untuk Membuat Object Yang Akan Menampilkan kotaTinggal Mahasiswa yang hanya bisa menampilkan parameter yang ada di def __init__ yang Berda
                    di class Mahasiswa"""

a. Makan = """ Untuk Membuat Object Yang Akan Menjalankan methods Makan(self) yang Berada di dalam class Mahasiswa """

a.mengalikanDenganDua = """ Untuk Membuat Object Yang Akan Menjalankan methods mengalikanDenganDua(self) yang Berada di dalam class Manusia, Karena Methods tersebut
                        tidak ada di class Mahasiswa, demikian class MhsTIF bisa mengakses methods tersebut di class Manusia """

a.nama = """ Untuk Membuat Object Yang Akan Menampilkan Nama Mahasiswa yang hanya bisa menampilkan parameter yang ada di def __init__ yang Berada
            di class Mahasiswa """

        

