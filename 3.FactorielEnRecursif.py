#coding:utf-8

import sys

print(" ")
print("                             EPREUVE DU FEU : FACTORIEL EN RECURSIF\n\n\n")


Parametre = int(sys.argv[1])
FACTO = 1

for i in range(1, Parametre+1):
    FACTO = FACTO * i

print(FACTO)

