class MhsTIF(object):
    def __init__(self, nama, umur, kota, NIM):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.nim = NIM

    def __str__(self):
        x = self.nim
        return x

    def getnim(self):
        return self.nim

c0 = MhsTIF('pipo', 10, 'Sukoharjo', 'L200170044')
c1 = MhsTIF('pipi', 14, 'Klaten', 'L200170048')
c2 = MhsTIF('papa', 12, 'Surakarta', 'L200170047')
c3 = MhsTIF('popo', 21, 'Wonogiri', 'L200170046')
c4 = MhsTIF('pepe', 20, 'Salatiga', 'L200170042')
c5 = MhsTIF('pupu', 65, 'Purworejo', 'L200170041')
c6 = MhsTIF('pida', 11, 'Bandung', 'L200170045')
c7 = MhsTIF('pidi', 43, 'Surabaya', 'L200170049')
c8 = MhsTIF('pede', 56, 'Purwodadi', 'L2001700139')
c9 = MhsTIF('pada', 15, 'Salatiga', 'L200170040')
c10 = MhsTIF('pudu', 20, 'Purwodadi', 'L200170052')

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos - 1].nim:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

def cetakDaftar(d):
    for i in d:
        print (i)
        
insertionSort(Daftar)
cetakDaftar(Daftar)
