#1
cisla = [5, 3, 8, 12, 4, 2]
nasobky = [i * 2 for i in cisla]
print(nasobky)
input()
#2
slova = ['world', 'love', 'health', 'happy', 'peace', 'future', 'people']
z1 = [len(slovo) for slovo in slova]
z2 = [slovo[:3] for slovo in slova]
z3 = [slovo.upper() for slovo in slova]
z4 = [slovo[0].upper() for slovo in slova]
z5 = [slovo + slovo for slovo in slova]
#3
z6 = [-1 * i for i in range(20)]
z7 = [5 * i for i in range(1, 11)]
z8 = [str(i) for i in range(10)]
z9 = [str(i)+str(i) for i in range(10)]

print(slova)
print(z1)
print(z2)
print(z3)
print(z4)
print(z5)
input()

print(z6)
print(z7)
print(z8)
input()
#4
z = [chr(i) for i in range(97, 123)]
print(z)
input()
z = [[chr(i), i] for i in range(97, 123)]
print(z)
input()
z = [len(p) for p in ('Adam', 'Alena', 'Romana', 'Jรกn' )]
print(z)
input()
#6
z = [chr(i) if i%2 == 0 else i for i in range(97, 123)]
print(z)
input()
z = [chr(i) if i%2 == 0 else chr(i-32) for i in range(97, 123)]
print(z)
input()
