import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters

subor = open('../lib/prislovia.txt','r')
suborw = open('../lib/program5.txt','w').close()
suborw = open('../lib/program5.txt','a')

text = subor.read()
subor.close()

slovo = ""
dlzky = []
najdlhsie = 0

i = 0
while i < len(text):
    while i < len(text) and ascii_letters.count(text[i]) != 0:
        slovo = slovo + text[i]
        i = i + 1
    dlzka = len(slovo)
    if(dlzka > 0):
        if(dlzka > najdlhsie):
            najdlhsie = dlzka
        dlzky.append(dlzka)
    while i < len(text) and ascii_letters.count(text[i]) == 0:
        i = i + 1
    slovo = ""

for i in range(najdlhsie):
    suborw.write("Počet slov s dĺžkou " + str(i+1) + ": " + str(dlzky.count(i+1)) + "\n")
suborw.close()
