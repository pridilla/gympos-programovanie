x = input()
vpohode = ["1", "3", "4", "7"]
maVpohode = False

obratene = x[::-1]
obratene = obratene.replace("9", "x")
obratene = obratene.replace("6", "9")
obratene = obratene.replace("x", "6")

for i in x:
    if(vpohode.count(i) > 0):
        maVpohode = True
        break

if(maVpohode):
    print("nie")
elif(x == obratene):
    print("nie")
else:
    print("ano")