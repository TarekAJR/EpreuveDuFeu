import sys

print(" ")
print("                         EPREUVE DU FEU : FACTORIEL LE RETOUR\n")

Parametre = int(sys.argv[1])
FACTO = 1

for i in range(1, Parametre+1):
    FACTO = FACTO * i


print(FACTO)