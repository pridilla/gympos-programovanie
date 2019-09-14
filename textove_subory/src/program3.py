import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters

subor = open('../lib/prislovia.txt','r')
suborw = open('../lib/program3.txt','w').close()
suborw = open('../lib/program3.txt','a')

text = subor.read()
subor.close()

slovo = ""

i = 0
while i < len(text):
    while i < len(text) and ascii_letters.count(text[i]) != 0:
        slovo = slovo + text[i]
        i = i + 1
    slovo_stred = slovo[1:-1]
    slovo_stred = ''.join(random.sample(slovo_stred,len(slovo_stred)))
    if len(slovo) > 1:
        suborw.write(str(slovo[0]) + slovo_stred + str(slovo[len(slovo)-1]))
    elif len(slovo) == 1:
        suborw.write(slovo)
    while i < len(text) and ascii_letters.count(text[i]) == 0:
        suborw.write(text[i])
        i = i + 1
    slovo = ""

suborw.close()
