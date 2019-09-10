file = open('../lib/program2_samohlasky.txt','w').close()
file = open('../lib/program2_spoluhlasky.txt','w').close()

file_samo = open('../lib/program2_samohlasky.txt','a')
file_spolu = open('../lib/program2_spoluhlasky.txt','a')
file = open("../lib/prislovia.txt")
text = file.read()

samohlasky = ['a','e','i','o','u','y']
spoluhlasky = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

for i in range(len(text)):
    if samohlasky.count(text[i].lower()) > 0:
        file_samo.write(text[i])
        file_spolu.write(' ')
    elif spoluhlasky.count(text[i].lower()) > 0:
        file_samo.write(' ')
        file_spolu.write(text[i])
    else:
        file_samo.write(text[i])
        file_spolu.write(text[i])

file_samo.close()
file_spolu.close()
