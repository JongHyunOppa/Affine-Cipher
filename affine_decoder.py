#python 2.7
from fractions import gcd

def coprime(a):
    for i in range(26):
        if((i*a)%26)==1:
            return i
    return 0

while True:
    plain = raw_input("")
    a = input()
    b = input()
    crypt=[]
    plain=plain.lower()
    plain = plain.replace(" ","")
    m = coprime(a)
    for char in plain:
        x = ord(char)-97
        ascii = (m*(x-b))%26
        tamga = chr(ascii+97)
        crypt.append(tamga)
    list = ''.join(crypt)
    if m == 0:
        print "enter a coprime"
    else:
        print(list)

