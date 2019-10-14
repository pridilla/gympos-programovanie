subor=open("vstupp2.txt","r")
subor2=open("sutaziaci.txt","r")

text=subor.read()
riadky=()
hlasy=[]
body=()

for riadok in subor2:
    riadky+= (riadok,)
    
##print(riadky)

for i in range(0,len(riadky),2):
    a=(riadky[i].strip())
    b=(riadky[i+1].strip())
##    print(a+"="+b)

k=text.count("\n")+1
for i in range(0,k):
    hlasy.append(i)
    if i in hlasy:
         body=1
    else:
        hlasy.append(i)
    print(hlasy)


subor.close()
subor2.close()
