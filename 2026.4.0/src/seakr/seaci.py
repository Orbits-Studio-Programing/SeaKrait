def atbash_uno(text):
    atb_keydict = {
        "a": "z",
        "b": "y",
        "c": "x",
        "d": "w",
        "e": "v",
        "f": "u",
        "g": "t",
        "h": "s",
        "i": "r",
        "j": "q",
        "k": "p",
        "l": "o",
        "m": "n",
        "n": "m",
        "o": "l",
        "p": "k",
        "q": "j",
        "r": "i",
        "s": "h",
        "t": "g",
        "u": "f",
        "v": "e",
        "w": "d",
        "x": "c",
        "y": "b",
        "z": "a",
        "A": "Z",
        "B": "Y",
        "C": "X",
        "D": "W",
        "E": "V",
        "F": "U",
        "G": "T",
        "H": "S",
        "I": "R",
        "J": "Q",
        "K": "P",
        "L": "O",
        "M": "N",
        "N": "M",
        "O": "L",
        "P": "K",
        "Q": "J",
        "R": "I",
        "S": "H",
        "T": "G",
        "U": "F",
        "V": "E",
        "W": "D",
        "X": "C",
        "Y": "B",
        "Z": "A"
    }
    s = ""
    for i in text:
        if i in atb_keydict:
            s += atb_keydict[i]
        else:
            s += i
    return s

def encrypt_int(i):
    enc = i*12332/34*23-2345+34
    return enc

def unencrypt_int(ei):
    uenc = ei-34+2345
    uuenc = uenc/23*34/12332
    return uuenc



def full_scram(i,k):
    import random
    r = random.randint(0,1000000)
    part = r/i
    if k == "r":
        return i*r-part
    else:
        kpart = k/i
        return i*k-kpart
