cisla = [ int(x) for x in input().split() ]
sum = 0
for i in cisla:
    if(i == 6):
        sum += 1
    elif(i == 1):
        sum -= 1

if(sum > 0):
    print("Alicka")
elif(sum == 0):
    print("Remiza")
else:
    print("Barborka")