import sys


print(" ")


Emplacement = "_"

Model = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

Sudoku = open(sys.argv[1])
Sudoku = Sudoku.readlines()


def printBoard(Sudoku):
    for i in range(11):
        for j in range(11):
            print(Sudoku[i][j], end=" ")
        print()

def isPossible(Sudoku, y, x, n):
    for j in range(11):
        if Sudoku[y][j] == n:
            return False

    for i in range(11):
        if Sudoku[i][x] == n:
            return False

    startRow = (y // 3) * 3
    startCol = (x // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if Sudoku[startRow+i][startCol+j] == n:
                return False
    return True

def solve():
    for i in range(11):
        for j in range(11):
            if Sudoku[i][j] == Emplacement:
                for n in range(1, 10):
                    if isPossible(Sudoku, i, j, n):
                        Sudoku[i][j] = str(n)
                        solve()

                        # Bad choice, make it blank and check again
                        Sudoku[i][j] = Emplacement
                return
    # We found a solution, print it            
    printBoard(Sudoku)

solve()