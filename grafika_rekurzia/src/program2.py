import random

def hod():
    return random.randint(1,6)

def hod_kockou(s = ""):
    i = hod()
    if(i == 6):
        return "6"
    s = str(i) + hod_kockou(s = s)
    return s

print(hod_kockou())
    

