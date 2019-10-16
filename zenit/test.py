n = int(input())
x = list(map(int, input().split()))
suc = 0
for i in range(n):
    suc += x[i]
print(suc)