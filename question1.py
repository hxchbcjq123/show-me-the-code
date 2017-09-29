import string
import random
def choice_acsii(n=5):
    a=[]
    b=string.ascii_letters+'0123456789'
    for i in range(n):
        s=random.choice(b)
        a.append(s)
    b=''.join(a)
    return b
def generatecode(time=200):
    i=0
    c=[]
    while i<time:
        for j in range(4):
            a=choice_acsii()
            c.append(a)
            c.append('-')
        c.pop()
        c.append('\n')
        i+=1
    d=''.join(c)
    print(d)

if __name__=='__main__':
    generatecode(200)
    
