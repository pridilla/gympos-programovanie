array = []
with open('../lib/K_PR6.txt','r') as f:
    array = [[int(x) for x in line.split()] for line in f]

for i in array:
    riadok = ""
    for j in range(len(i)):
        if j % 2 == 0:
            for k in range(i[j]):
                riadok = riadok + " "
        if j % 2 == 1:
            for k in range(i[j]):
                riadok = riadok + "*"
    print(riadok)