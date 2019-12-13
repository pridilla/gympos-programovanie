import random

def priklad (operacia):
    vysledok = 0
    x = random.randint(1,10)
    y = random.randint(1, 10)
    text = ""
    if(operacia == 1):
        if (x < y):
            y = random.randint(1,x)
        vysledok = x - y
        text = str(x) + " - " + str(y)
    if(operacia == 2):
        vysledok = x*y
        text = str(x) + " * " + str(y)
    if(operacia == 3):
        vysledok = x+y
        text = str(x) + " + " + str(y)
    inp = int(input(text + " = "))

    if(vysledok == inp):
        return "Spravne!"
    else:
        return "Nespravne!"

print(priklad(random.randint(1,3)))
        