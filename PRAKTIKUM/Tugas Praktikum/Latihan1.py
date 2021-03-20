import random

# String merupakan bentuk data yang biasa dipakai dalam bahasa pemrograman
# untuk keperluan menampung dan memanipulasi data teks, misalnya untuk menampung
# dan menyimpan suatu kalimat

# SOAL NOMOR SATU
Nama = str(input('Nama: '))
Nim = str(input('NIM: '))
about_string = str(input('Tentang String: '))
lowercase = about_string.lower()
hitung_vokal = {}
for vokal in 'aiueo':
    count = lowercase.count(vokal)
    hitung_vokal[vokal] = count
print('\n1.')
print(hitung_vokal)

# SOAL NOMOR 2
lastNIm = (int(Nim[-2:]))
orda= ord(max(about_string))
huruf = 'a'
vokal = about_string.lower()
jmlh_vokal= ''
for i in vokal:
    if i in huruf:
        jmlh_vokal+= i
vokal = len(jmlh_vokal)
jumlah = orda - lastNIm * vokal//2
print('\n2.')
print(jumlah)

# SOAL NOMOR 3
n = random.randint(10,20)
rnd_acak = random.choices(about_string,k=n)
hasil = (''.join(rnd_acak))
print('\n3.')
print(hasil)

# SOAL NOMOR 4
bil = random.randint(1, 3)
word = []
for i in rnd_acak:
    if i == rnd_acak[bil]:
        i = i.upper()
        word.append(i) 
    else:
        word.append(i)
print('\n4.')
print(''.join(word))

# SOAL NOMOR 5
nim_nama = Nama + Nim
R_place = nim_nama.replace(' ', '').replace('a','o').replace('i','o').replace('u','o').replace('e','o')
print('\n5.')
print(R_place)