sur = [int(x) for x in input().split()]

n = sur[0]
k = sur[1]

strd = (n+1)/2

if(k>strd):
    print(str(k-1))
elif(k<strd):
    print(str(k+1))
elif(n == 1):
    print("1")
else:
    print(str(k+1))