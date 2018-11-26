#python 2.7
from fractions import gcd

def coprime(a):
    if gcd(a,26)==1:
        return a
    return 0

while True:
    plain = raw_input("")
    a = input()
    b = input()
    crypt=[]
    plain=plain.lower()
    plain = plain.replace(" ","")
    m = coprime(a)
    if m == 0:
        print "enter a coprime"
    else:
        for char in plain:
            x = ord(char)-97
            ascii = (x*m+b)%26
            tamga = chr(ascii+97)
            crypt.append(tamga)
    list = ''.join(crypt)
    print(list)

