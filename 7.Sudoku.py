# Step 1 : JE DECLARE LES LISTES DITE MODEL, D'AUTRE VARIABLE 
# Step 2 : JE LIE LE FICHIER ENTRER EN PREMIER PARAMETTRE ET JE SPLIT LE BACKSLASH
# Step 3 : JE DEFINIE TOUT LES COORDONNEES DES UNDERSCORS DANS LE SUDOKU
# Step 4 : JE DEFINIE LA FONCTION RESOLVE() QUI ME PERMET DE SOUSTRAIRE LES LIGNES COMPORTANT UN UNDERSCORE
#          AVEC UNE LISTE MODEL POUR EN RETOURNER LES CHIFFRES SOLUTIONS


import sys

print(" ")
print("                                 EPREUVE DU FEU : SUDOKU\n")

# Step 1 : JE DECLARE LES LISTES DITE MODEL, D'AUTRE VARIABLE 

ModelLine = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '|', '|']
ModelColumn = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '-']

setmodelLine = set(ModelLine)
setmodelColumn = set(ModelColumn)
Emplacement = '_'
Exclure = '---+---+---'
Exclure1 = '|||+|||+|||'
Sudoku = open(sys.argv[1],"r").read()
newSudoku = []


i = 0
line = 0
Cols = 0
Rows = 0

# Step 2 : JE LIE LE FICHIER ENTRER EN PREMIER PARAMETTRE ET JE SPLIT LE BACKSLASH

Sudoku = [list(i) for i in Sudoku.split()]

# Step 3 : JE DEFINIE TOUT LES COORDONNEES DES UNDERSCORS DANS LE SUDOKU

for x,line in enumerate(Sudoku):
        print(line)
        for i,y in enumerate(line):
                if y == Emplacement:
                        print([(x,i)])

print('\n\n')

# Step 4 : JE DEFINIE LA FONCTION RESOLVE() QUI ME PERMET DE SOUSTRAIRE LES LIGNES COMPORTANT UN UNDERSCORE
#          AVEC UNE LISTE MODEL POUR EN RETOURNER LES CHIFFRES SOLUTIONS
                        
def Resolve():
        z=0
        i=0
        for i in range(0, 11):
                Probleme = [ z for z in Sudoku[i]]
                Solution = list(set(ModelLine) - set(Sudoku[i]))
                if 0 < len(Solution) < 3 :
                        print(Probleme)
                        print(Solution)
                        
              

Resolve()


print('\n\n')
                        # Pour extraire les lignes et column possedant underscore

#while i < len(Sudoku):
        #print(Sudoku[i][1])
        #i = i+1


for Cols in range(len(Sudoku)):
                for i in range(len(Sudoku[Cols])):
                #print([Sudoku[i][i]]) Permet de prendre la diagonal WTF
                        print([Sudoku[i][Cols]])
                      
print("      ////////           ")

for Rows in range(len(Sudoku)):
                for i in range(len(Sudoku[Rows])):
                        print([Sudoku[Rows][i]])

print("\n\n\n")





                     
"""
a = [1,3,4,5, 7,8, 9, 10]
b = [x for x in range(a[0], a[-1] + 1)]
a = set(a)
print (list(a ^ set(b)))`
[2,6]
        """