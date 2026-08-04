def positivity(i,pos,neg,zero):
    if i > 0:
        return pos
    elif i < 0:
        return neg
    else:
        return zero

def loopsubp(i):
    while i > 0:
        print(i)
        i -= 1

def loopaddp(i,end):
    while i < end:
        i += 1
        print(i)

def looptimep(b,s,tb):
    while s < b:
        print(s)
        s *= tb

def loopdivp(b,s,db):
    while b > s:
        b /= db
        print(b)

def loopdivnrp(b,s,db):
    while b > s:
        b //= db
        print(b)

def loopexpp(b,s,eb):
    while s < b:
        print(s)
        s **= eb

def loopsqurp(b,s,sb):
    ssb = 1/sb
    while b > s:
        print(b)
        b **= ssb

def isgreat(i,than):
    if i > than:
        return True
    else:
        return False

def equal(i,n):
    if i == n:
        return True
    else:
        return False

def equalx3(i,n,m):
    if i == n == m:
        return True
    else:
        return False
    
def equalxl_aut(l,l2):
    if l[l-1] == l[l2-1]:
        return True
    else:
        return False

def func50():
    #no one will know :)#
    import random
    i = random.randint(1,100)
    if i > 50:
        return True
    else:
        return False

def base10to2_aut_str(i):
    return f"{i:b}"

def base10to2_man(i):
    return bin(i)

def base2to10(i):
    if i[0] == "b" and i[1] == "0":
        i = i[2:]
        return int("{i}", 2)
    else:
        return int("{i}", 2)


def palin_check(i,iso,noto):
    stri = str(i)
    revstri = stri[::-1]
    inti = int(stri)
    intrevi = int(revstri)
    if len(str(abs(i))) == 1:
        return iso
    elif inti == intrevi:
        return iso
    else:
        return noto


def catmath_test(i):
    if i == "cat":
        return 1
    elif i == "dog":
        return -1
    else:
        return 0

def math_test(i):
    if i == i:
        return 1
    else:
        return -1