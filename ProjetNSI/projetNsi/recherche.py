import time
import random

maxVal = 10
#Val = 100
#listeNombres = random.choices(range(maxVal),k=nVal)

def rechercheNaive(L: list, elt: int)-> int:
    for i, element in enumerate (L) :   #enumerate permet d'isoler la position (i) et l'élément (element)
        if elt == element :
            return i
    return False,i


def rechercheDicho(L: list, elt: int)-> int:
    #tps1 = time.time()
    tr = False
    deb = 0
    fin = len(L)-1
    comp = 0
    while tr == False and deb <= fin :
        comp += 1
        mil = (deb+fin)//2
        if L[mil] == elt :
            tr = True
        elif elt > L[mil] :
            deb = mil + 1
        else :
            fin = mil - 1
    #tps2 = time.time() - tps1
    return tr, comp

xValeurs = [10**i for i in range (1, 8) ]

#print(listeNombres)
tDicho = []
tnaive = []
listeNombres = random.choices(range(maxVal),k=nVal)
a = sorted(listeNombres)
for nVal in xValeurs :
    tps1 = time.time()
    rechercheDicho( a,-1)
    tps2 = time.time() 
    tDicho.append (tps2 -tps1)
    
    tps3 = time.time()
    rechercheNaive(listeNombres ,-1)
    tps4 = time.time() 
    tDicho.append (tps4-tps3)
    
#for nVal in xValeurs :
#   listeNombres = random.choices(range(maxVal),k=nVal)
#   tps3 = time.time()
#   rechercheNaive(listeNombres ,-1)
#   tps4 = time.time() 
#   print (tps4 - tps3, '= recherche Naive, pour un tableau de' , nVal , 'valeurs')
print(tDicho, tnaive)
print(xValeurs)


from matplotlib.pyplot import*
loglog(xValeurs, tnaive, '-b')
loglog(xValeurs, tDicho, '-r')
show()
