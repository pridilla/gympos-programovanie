import sys

suborr = open('../lib/dialog.txt', 'r', encoding="cp1250")
farby = ["\033[1;31m", "\033[1;34m", "\033[1;36m", "\033[0;32m"]

while True:
    cislo = suborr.readline()
    if cislo == '':
        break
    cislo = cislo.strip()
    cislo = int(cislo)
    farba = farby[cislo-1]

    text = suborr.readline()
    if text == '':
        break
    
    sys.stdout.write(farba)
    print(text, end = '')

print("\n")
suborr.close()