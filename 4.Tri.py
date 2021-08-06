#coding:utf-8

import sys

print(" ")
print("                             EPREUVE DU FEU : TRI\n")


Tri = list(sys.argv[1:])

# METTRE LA LISTE DANS L'ORDRE NORMAL CROISSANT
Tri.sort()

# PRENDRE DANS L'ORDRE INVERSE DE L'ORDRE PRECEDENT
Tri.reverse()

# METTRE DANS LE RENDUE SOUHAITER
Rendue = " ".join(Tri)

print(Rendue)
prin(" ")