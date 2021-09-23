import sys

print(" ")
print("                         EPREUVE DU FEU : RECTANGLE\n")


sudoku = [[1, 9, 5, 7, 8, 4, 2, 0, 0],
          [3, 0, 6, 5, 2, 9, 1, 4, 7],
          [4, 7, 2, 1, 0, 3, 9, 8, 5],
          [6, 3, 7, 8, 5, 2, 4, 1, 9],
          [8, 5, 9, 6, 0, 1, 7, 3, 2],
          [2, 1, 4, 3, 9, 7, 6, 5, 8],
          [9, 2, 0, 4, 1, 8, 5, 7, 6],
          [5, 0, 8, 9, 7, 6, 3, 2, 1],
          [7, 6, 1, 2, 3, 5, 8, 0, 4]  
           ] 


def n_valide(y, x, n):
    #Test les lignes
    for x0 in range(9):
        if sudoku[y][x0] == n:
            return False
        
    for y0 in range(9):
        if sudoku[y0][x] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0+i][x0+j] == n:
                return False
        return True

def resolu():
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1, 10):
                    if n_valide(y, x, n):
                        sudoku[y][x] = n
                        resolu()
                        sudoku[y][x] = 0
                return

    for i in sudoku:
        for j in i:
            print(j, end=" ")
        print()

resolu()
                        
