import random
while True:
    NIM = input('NIM: ')
    try:
        int(NIM)
        break
    except:
        print('NIM-nya yaa...')
nama = input('Nama: ')

while True:
    about_string = input('Apa yang ada ketahui tentang string? ')
    # String adalah tipe data yang memuat satu karakter 
    # atau lebih karakter yang diapit oleh tanda petik tunggal
    if len(about_string) > 1:
        break
    else:
        print('gass')

# SOAL NOMOR SATU
def vokal(string):
    h_vokal = {
        'a' : 0,
        'i' : 0,
        'u' : 0,
        'e' : 0,
        'o' : 0
    }
    for karakter in string.lower():
        for vo in ['a', 'i', 'u', 'e', 'o']:
            if karakter == vo:
                h_vokal[vo] += 1
    return h_vokal

# SOAL NOMOR DUA
def noDua(string, NIM):
    Ascii_maks = ord(max(string))
    nim_akhir = NIM[-2:]
    vokal_a = vokal(string)['a']
    so = Ascii_maks - (int(nim_akhir) * (vokal_a//2))
    return so

# SOAL NOMOR TIGA & EMPAT
def rand_nomor(string):

    # NOMOR 3
    if len(string) > 20:
        ulang = random.randint(10, 20)
    else:
        ulang = random.randint(10, len(string))
    no_Cap = ''
    h_Cap = []
    i = 1
    jalannya = []
    while i <= ulang:
        rand_index = random.randrange(0, len(string))
        rand_karakter = string[rand_index]
        if rand_index in jalannya:
            ulang += 1
        else:
            no_Cap += rand_karakter()
            h_Cap.append(rand_karakter)
            jalannya.append(rand_index)
        i += 1

    # NOMOR 4
    ulang = random.randint(1, 3)
    i = 1
    while i <= ulang:
        rand_index = random.randrange(0, len(h_Cap))
        rand_karakter = h_Cap[rand_index].upper()
        if rand_karakter in h_Cap or rand_karakter == ' ':
            ulang += 1
        h_Cap[rand_index] = rand_karakter
        i += 1
    h_Cap = ''.join(h_Cap)
    return h_Cap, no_Cap

# SOAL NOMOR LIMA
def NNJoin(nama, NIM):
    s = ''
    for karakter in nama.replace(' ', ' '):
        for vo in ['a', 'i', 'u', 'e', 'o']:
            if karakter.lower() == vo:
                if karakter.isupper():
                    s += "O"
                    break
                else:
                    s += "o"
                    break
        else:
            s += karakter
    return s + NIM