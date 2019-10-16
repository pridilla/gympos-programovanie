import string
def je_palindrom(s):
    if(len(s) < 2):
        return True
    if(s[0] == s[-1]):
        print(s)
        return je_palindrom(s[1:-1])
    return False

print(je_palindrom(input("Zadajte retazec: ")))