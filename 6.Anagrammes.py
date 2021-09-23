import sys

print(" ")
print("                         EPREUVE DU FEU : ANAGRAMMES\n")


File1 = open(sys.argv[2],"r").read()
File1 = File1.split("\n")

Parametre = sorted(sys.argv[1])

for Anagramme in File1 :
    if Parametre == sorted(Anagramme):
        print(Anagramme)