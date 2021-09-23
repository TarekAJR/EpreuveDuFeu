import numpy as np
import csv

with open("7.s.txt") as Sudoku:
    reader = csv.reader(Sudoku, delimiter ="\t")
    Sudoku = list(reader)

Sudoku = np.loadtxt("7.s.txt")


def Ciblage():
    Coords = []
    for i in range(Sudoku.shape[0]):
        for l in range(Sudoku.shape[1]):
            if (Sudoku[i,l] == "_"):
                Coords.append((i,l))
    return Coords

def Vérification(l):
    return set(range(1,10)) - set(l)

def Remplire():
    Cible = Ciblage()

    for i in Cible :
        v_colone = Vérification(Sudoku[i[0],:])
        v_ligne = Vérification(Sudoku[:,i[1]])
        cellule = Sudoku[i[0]//3*3:1[0]//3*3+3,i[1]//3*3:i[1]//3*3+3]
        v_cellule = Vérification(cellule.flat)
        Coords = v_cellule.intersection(v_colone).intersection(v_ligne)
        Coords = list(Coords)[0]
        Sudoku[i[0],i[1]] = Coords
    return (Sudoku)
print(Remplire())