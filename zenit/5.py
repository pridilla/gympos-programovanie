sur = [int(x) for x in input().split()]

y = sur[1]
x = sur[0]

siet = []
for i in range(15):
    siet.append([])
    for j in range(15):
        if(j == 0 or j == 14 or i == 0 or i == 14):
            siet[i].append('#')
        else:
            siet[i].append('.')

def zobraz():
    for i in siet:
        stri = ""
        for j in i:
            stri += j
        print(stri)

siet[13][13] = 'D'
siet[x][y] = 'U'

if(x == 13 and y == 13):
    print("Ujo je doma!")
else:
    for i in range(x + 1, 14):
        siet[i][y] = 'x'
    for i in range(y + 1, 13):
        siet[13][i] = 'x'
    zobraz()