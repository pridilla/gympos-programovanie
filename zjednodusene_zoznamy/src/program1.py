import random
ls = [random.randint(0,150) for i in range(20)]
print("Zoznam vymeškaných hodín: " + str(ls))
print("Kumulatívne vymeškané hodiny za celú triedu: " + str(sum(ls)))
print("Primerný počet vymeškaných hodín na žiaka: " + str(round(sum(ls)/20.0,2)))
print("Žiak " + str(ls.index(max(ls))+1) + " vymeškal " + str(max(ls)) + " hodín. Je to najviac z celej triedy.")
print("Počet žiakov navrhnutých na pochvalu: " + str(ls.count(0)))
if(ls.count(0) > 0):
    print("Zoznam týchto žiakov: " + str([i + 1 for i in range(20) if ls[i] == 0]))