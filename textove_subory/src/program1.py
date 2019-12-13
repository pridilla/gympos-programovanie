import random
from string import ascii_lowercase
from string import ascii_uppercase

subor = open('../lib/prislovia.txt','r')
zoznam = subor.readlines()
subor.close()

subor = open('../lib/prislovia.txt','r')
text = subor.read()
subor.close()

print("Pocet riadkov: " + str(len(zoznam)))
print("Pocet znakov: " + str(len(text)))
print("Pocet znakov bez medzier: " + str(len(text.replace(' ', ''))))

analyza = []

for letter in ascii_lowercase:
     analyza.append("Pocet znakov " + letter + ": " + str(text.count(letter) + text.count(chr(ord(letter) - 32))))

subor = open('../lib/program1_vystup.txt','w')
subor.write('')
subor.close()

subor = open('../lib/program1_vystup.txt','a')
for i in analyza:
    print(i)
    subor.write(i + '\n')
subor.close()
    
print(zoznam[random.randint(0,len(zoznam)-1)])


