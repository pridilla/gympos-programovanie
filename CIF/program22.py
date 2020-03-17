tyzden_dni = ["pondelok", "utorok", "streda", "stvrtok", "piatok", "sobota", "nedela"]
mesiace = ["januar", "februar", "marec", "april", "maj", "jun", "jul", "august", "september", "oktober", "november", "december"]
mesiace_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

### dnes je piatok 14.2.2020

s = input("Zadajte datum v tvare dd.mm.rrrr: ")
sdata = s.split(".")
sden = int(sdata[0])
smesiac = int(sdata[1]) - 1
srok = int(sdata[2])

den = 14
mesiac = 1
rok = 2020

tyzden_den = 4

def jePriestupny():
    global rok
    if(rok%4==0 and rok%100 != 0):
        return True
    return False

def porovnajDatum():
    global den,mesiac,rok, sden, smesiac, srok
    if(rok > srok):
        return "neskor"
    elif (rok < srok):
        return "skor"
    if(mesiac > smesiac):
        return "neskor"
    elif (mesiac < smesiac):
        return "skor"
    if(den > sden):
        return "neskor"
    elif (den < sden):
        return "skor"
    return "dnesok"

def zvacsiDen():
    global den, mesiac, rok, mesiace_dni, tyzden_den
    den += 1
    priestupnyden = 0
    if(mesiac == 1 and jePriestupny()):
        priestupnyden = 1
    if(mesiace_dni[mesiac] + priestupnyden < den):
        den = 1
        mesiac += 1
        if(mesiac == 12):
            mesiac = 0
            rok +=1
    tyzden_den += 1
    if(tyzden_den == 7):
        tyzden_den = 0

def zmensiDen():
    global den, mesiac, rok, tyzden_den
    den -= 1
    priestupnyden = 0
    if(den == 0):
        mesiac-=1
        if(mesiac == -1):
            mesiac = 11
            rok-=1
        if(mesiac == 1 and jePriestupny()):
            priestupnyden = 1
        den = mesiace_dni[mesiac] + priestupnyden
    tyzden_den -= 1
    if(tyzden_den == -1):
        tyzden_den = 6


def najdiDenTyzden():
    x = porovnajDatum()
    while(x != "dnesok"):
        if(x=="neskor"):
            zmensiDen()
        else:
            zvacsiDen()
        x = porovnajDatum()

najdiDenTyzden()
print(str(den)+"."+mesiace[mesiac]+"."+str(rok) + " " + tyzden_dni[tyzden_den])