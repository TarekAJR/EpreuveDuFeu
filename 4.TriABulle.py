#coding:utf-8

import sys

print(" ")
print("                       EPREUVE DU FEU BONUS : TRI DE BULLE\n")

TriABulle = list(sys.argv[1:])

def tri_à_bulles(TriABulle):
    n = len(TriABulle)
    # TRAVERSER TOUS LES ELEMENTS DU TABLEAU 
    for i  in range(n):
       for j in range(0, n-i-1):
           # ECHANGER SI L'ELEMENT TROUVE EST PLUS GRAND QUE LE SUIVANT
           if TriABulle[j+1] < TriABulle[j]:
                TriABulle[j+1], TriABulle[j] = TriABulle[j], TriABulle[j+1]

# PROGRAMME PRINCIPALE POUR TESTER LE CODE CI-DESSUS

tri_à_bulles(TriABulle)

for i in range(len(TriABulle)):
    print(TriABulle[i])