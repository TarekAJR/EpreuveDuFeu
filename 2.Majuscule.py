#coding:utf-8

import sys

print(" ")
print("                             EPREUVE DU FEU : MAJUSCULE\n\n\n")


MESSAGE = str(sys.argv[1])
JOINDRE = []
MOT1 = ""
MOT2 = ""
MOT3 = ""
MOT_bien = ""
MOT_le = ""
MOT_bonjour = ""
COUPER = MESSAGE.split()
MOT1 = COUPER[0]
MOT2 = COUPER[1]
MOT3 = COUPER[2]
MOT1 = MOT1.lower()
MOT2 = MOT2.lower()
MOT3 = MOT3.lower()


#Ici je transfrome le mot "Bien" en "bIeN"

for i in range(len(MOT1)):
    inter = i
    LETTRE = MOT1[i]

    if (inter % 2) == 1:
        LETTRE = LETTRE.upper()
    MOT_bien = MOT_bien + LETTRE

#Ici je transfrome le mot "le" en "lE"

for a in range(len(MOT2)):
    alter = a
    LETTRE = MOT2[a]

    if (alter % 2) == 1:
        LETTRE = LETTRE.upper()
    MOT_le = MOT_le + LETTRE

#Ici je transfrome le mot "bonjour" en "bOnJoUr"

for s in range(len(MOT3)):
    subs = s
    LETTRE = MOT3[s]

    if (subs % 2) == 1:
        LETTRE = LETTRE.upper()
    MOT_bonjour = MOT_bonjour + LETTRE

JOINDRE = [MOT_bien, MOT_le, MOT_bonjour]

newMESSAGE = " ".join(JOINDRE)
print(newMESSAGE)