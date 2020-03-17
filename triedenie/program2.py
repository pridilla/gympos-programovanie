import time, random, sys
poler = [random.randint(1,1000) for i in range(1000)]
sys.setrecursionlimit(1005)


def utriedSelectionSortX(pole):
    if len(pole) == 0:
        return []
    najmensie = pole[0]
    index = 0
    for i in range(len(pole)):
        if najmensie > pole[i]:
            najmensie = pole[i]
            index = i
    pole[index]=pole[0]
    npole = [najmensie]
    rpole = utriedSelectionSortX(pole[1:])
    return npole + rpole

ms = time.time_ns() / 1000000
u = utriedSelectionSortX(poler)
print("Čas: " + str(time.time_ns() / 1000000 - ms) + " mikrosekund")