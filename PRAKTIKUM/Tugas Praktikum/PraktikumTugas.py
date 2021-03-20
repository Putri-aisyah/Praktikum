import random as r
while True:
    nim = input('Masukkan NIM: ')
    try:
        int(nim)
        break
    except:
        print('nim tidak valid')

nama = input('Masukkan nama: ')

while True:
    tentangString = input('Apa yang dimaksud string? ')
    # String adalah tipe data yang memuat satu karakter 
    # atau lebih karakter yang diapit oleh tanda petik tunggal

    if len(tentangString) >= 10:
        break
    else:
        print('maaf, inputan minimal 10')

def vowelIdentifier(string):
    vowels = {
        'a' : 0,
        'i' : 0,
        'u' : 0,
        'e' : 0,
        'o' : 0
    }
    for char in string.lower():
        for fow in ['a', 'i', 'u', 'e', 'o']:
            if char == fow:
                vowels[fow] += 1
    return vowels

def nomorDua(string, nim):
    maxAscii = ord(max(string))
    nimLastTwo = nim[-2:]
    aVowels = vowelIdentifier(string)['a']
    result = maxAscii - (int(nimLastTwo) * (aVowels//2))
    return result

def randomPick(string):
    if len(string) > 20:
        loop = r.randint(10,20)
    else:
        loop = r.randint(10, len(string))
    nonCapital = ''
    capital = []
    i = 1
    accessedIndex = []
    while i <= loop:
        randomIndex = r.randrange(0, len(string))
        randomChar = string[randomIndex]
        if randomIndex in accessedIndex:
            loop += 1
        else:
            nonCapital += randomChar
            capital.append(randomChar)
            accessedIndex.append(randomIndex)
        i += 1
    loop= r.randint(1, 3)
    i = 1
    while i <= loop:
        randIndex = r.randrange(0, len(capital))
        randomChar = capital[randIndex].upper()
        if randomChar in capital or randomChar == ' ':
            loop += 1
        capital[randIndex] = randomChar
        i += 1
    capital = ''.join(capital)
    return capital, nonCapital
    
def namaNimJoin(nama, nim):
    result = ''
    for char in nama.replace(' ', ''):
        for fow in ['a', 'i', 'u', 'e', 'o']:
            if char.lower() == fow:
                if char.isupper():
                    result += 'O'
                    break
                else:
                    result += 'o'
                    break
        else:
            result += char
    return result+nim