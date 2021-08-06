#coding:utf-8

import sys

print(" ")
print("                     EPREUVE DU FEU BONUS : TRI PAR SELECTION\n")

TriParSelection = list(sys.argv[1:])

def tri_selection(TriParSelection):

    for i in range(len(TriParSelection)):

        # TROUVER LE MIN
        min = i

        for j in range(i+1, len(TriParSelection)):
            if TriParSelection[min] > TriParSelection[j]:
                min = j

        tmp = TriParSelection[i]
        TriParSelection[i] = TriParSelection[min]
        TriParSelection[min] = tmp

    return TriParSelection

# PROGRAMME PRINCIPALE POUR TESTER LE CODE CI-DESSUS
tri_selection(TriParSelection)

for i in range(len(TriParSelection)):
    print(TriParSelection[i])