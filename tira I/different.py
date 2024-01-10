from time import time

def eroava_taulukossa(v, v2):
    for l in v:
        found = l in v2
        if not found:
            return l

def eroava_hajataulussa(v, v2):
    h = set(v2)
    for l in v:
        found = l in h
        if not found:
            return l

def eroava_jarjestyksessa(v, v2):
    s = sorted(v)
    s2 = sorted(v2)
    for i in range(len(s)):
        if s[i] != s2[i]:
            return s[i]

if __name__ == "__main__":
    v = open("vocabulary.txt").readlines()
    v2 = open("vocabulary2.txt").readlines()
    t1 = time()
    print(eroava_taulukossa(v, v2))
    t2 = time()
    print(eroava_hajataulussa(v, v2))
    t3 = time()
    print(eroava_jarjestyksessa(v, v2))
    t4 = time()
    print(t2-t1, t3-t2, t4-t3)
