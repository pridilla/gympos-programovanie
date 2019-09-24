import string

subor_sifra = open("../lib/sifra.txt", "r")
sifra = int(subor_sifra.readline().strip())
subor_sifra.close()

subor = open("../lib/text.txt", "r")
text = subor.read()
subor.close()

subor = open("../lib/text.txt", "a")
subor.write("\n")

def premen(znak, posun):
    posledne = 'z'
    if(string.ascii_lowercase.count(znak) == 0):
        posledne = 'Z' 
    dl_abcd = ord('z') - ord('a')
    dl_abcd += 1
    posun = posun % dl_abcd
    novy_znak = ord(znak) + posun
    while novy_znak > ord(posledne):
        novy_znak -= dl_abcd
    return chr(novy_znak)

for i in text:
    if(string.ascii_letters.count(i) == 0):
        subor.write(i)
    else:
        subor.write(premen(i, sifra))

subor.close()