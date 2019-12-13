import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters

subor = open('../lib/prislovia.txt','r')
suborw = open('../lib/program4.txt','w').close()
suborw = open('../lib/program4.txt','a')

riadok = subor.readline()

while riadok != '':
    riadok = riadok.rstrip()
    znak = ''
    if riadok[-1] == '.' or riadok[-1] == ',':
        znak = riadok[-1]
        riadok = riadok[:-1]
    for i in range(len(riadok)):
        suborw.write(riadok[-i - 1])
    suborw.write(znak)
    suborw.write('\n')
    riadok = subor.readline()

suborw.close()
subor.close()
