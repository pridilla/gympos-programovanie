import time, random 

pole = [random.randint(1,1000) for i in range(5000)]

def utriedBubbleX(pole, setrenie):
    ms = time.time_ns() / 1000000
    for cp in range(len(pole)-1):
        untouched = True
        for i in range(len(pole)-1, cp, -1):
            if pole[i] < pole[i-1]:
                untouched = False
                pole[i], pole[i-1] = pole[i-1], pole[i]
        if(setrenie and untouched):
            print("Čas: " + str(time.time_ns() / 1000000 - ms) + " mikrosekund")
            return pole
    print("Čas: " + str(time.time_ns() / 1000000 - ms) + " mikrosekund " + str(setrenie))
    return pole

u1 = utriedBubbleX(pole, True)
u2 = utriedBubbleX(pole, False)