def perus(luvut, erotus, m):
    if m == len(luvut):
        return erotus == 0
    else:
        if branch(luvut, erotus+luvut[m], m+1):
            return True
        else:
            return branch(luvut, erotus-luvut[m], m+1)

def branch(luvut, erotus, m):
    if (m == len(luvut)):
        return (erotus == 0)
    if abs(erotus) > sum(luvut[m:]):
        return False
    if branch(luvut, erotus+luvut[m], m+1):
        return True
    else:
        return branch(luvut, erotus-luvut[m], m+1)

def jarjestetty(luvut,erotus,m):
    return branch(sorted(luvut,reverse=True), erotus, m)
    

from timeit import default_timer as timer
import random

if __name__ == "__main__":
    n = 23
    toistot = 20
    ylaraja = 99999999
    random.seed()
    ajat = [[], [], []]
    for i in range(toistot):
        luvut = [random.randint(1, ylaraja) for i in range(n)]
        alku = timer()
        jako = perus(luvut, 0, 0)
        loppu = timer()
        ajat[0].append(loppu-alku)
        print('Perus algoritmi, {0:f} sekuntia, ratkaisu: {1}'.format(loppu-alku, jako))
        alku = timer()
        jako = branch(luvut, 0, 0)
        loppu = timer()
        ajat[1].append(loppu-alku)
        print('Branch and bound, {0:f} sekuntia, ratkaisu: {1}'.format(loppu-alku, jako))
        alku = timer()
        jako = jarjestetty(luvut, 0, 0)
        loppu = timer()
        ajat[2].append(loppu-alku)
        print('BnB + järjestäminen, {0:f} sekuntia, ratkaisu: {1}\n'.format(loppu-alku, jako))
    print("Keskivertoajat:")
    print(f"Perus: {sum(ajat[0])/len(ajat[0])}")
    print(f"BnB: {sum(ajat[1])/len(ajat[1])}")
    print(f"BnB + järjestäminen: {sum(ajat[2])/len(ajat[2])}")