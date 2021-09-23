import sys

print(" ")
print("                         EPREUVE DU FEU : SUDOKU\n")

"""
Sudoku = open(sys.argv[1], "r").read()
Sudoku = [list(i) for i in Sudoku.split("\n")]"""

Sudoku = [['1', '9', '5', '7', '8', '4', '2', '_', '_'], 
['3', '_', '6', '5', '2', '9', '1', '4', '7'], 
['4', '7', '2', '1', '_', '3', '9', '8', '5'], 
['6', '3', '7', '8', '5', '2', '4', '1', '9'], 
['8', '5', '9', '6', '_', '1', '7', '3', '2'], 
['2', '1', '4', '3', '9', '7', '6', '5', '8'],  
['9', '2', '_', '4', '1', '8', '5', '7', '6'],
['5', '_', '8', '9', '7', '6', '3', '2', '1'], 
['7', '6', '1', '2', '3', '5', '8', '_', '4']]


def n_valide(y, x, n):
    global Sudoku
    #On détermine si le nombre est valide sur la ligne.
    for x0 in range(len(Sudoku)):
        if Sudoku[y][x0] == n:
            return False

    #On détermine si le nombre est valide sur la colonne.
    for y0 in range(len(Sudoku)):
        if Sudoku[y0][x] == n:
            return False

    #On détermine si le nombre est valide dans la cellule.
    x0 = (x//3) * 3
    y0 = (y//3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if Sudoku[y0+i][x0+j] == n :
                return False
    return True


def solve():
    global Sudoku
    for y in range(9):
        for x in range(9):
            if Sudoku[y][x] == "_":
                for n in range(1, 10):
                    if n_valide(y, x, n):
                        Sudoku[y][x] = n
                        solve()
                        Sudoku[y][x] = "_"
                return

    for i in range(9):
        for j in range(9):
            print(Sudoku[i][j], end = " ")
        print()
solve()
