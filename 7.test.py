import sys

print(" ")
print("                                 EPREUVE DU FEU : SUDOKU\n")


ModelLine = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '|', '|']
ModelColumn = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '-']
Solution = []
setmodelLine = set(ModelLine)
setmodelColumn = set(ModelColumn)
Emplacement = '_'
Exclure = '---+---+---'
Exclure1 = '|||+|||+|||'
Sudoku = open(sys.argv[1],"r").read()
i = 0
x = 0


line = 0
Cols = 0
Rows = 0

ListCols = []
ListRows = []
COORDS = []


Sudoku = [list(i) for i in Sudoku.split()]
newSudoku = list()
z=0
i=0
def Resolve():

        ToutSolution = []
        for i in range(0, 11):
                Probleme = [ z for z in Sudoku[i]]
                Solution = list(set(ModelLine) - set(Sudoku[i]))
                if 0 < len(Solution) < 3 :
                        str(Solution)
                        ToutSolution.append(Solution)
                        print(ToutSolution)
                        

                       
       
                
        
print('\n\n')


for x,line in enumerate(Sudoku):
                print(line)
                for i,y in enumerate(line):
                        if y == Emplacement:
                                str((x,i))
                                COORDS.append((x,i))
                                print(COORDS)




Resolve()

def Remplire():
        for Emplacement in Sudoku :
                for c in range(COORDS):
                        for s in range(ToutSolution):
                                newSudoku = Sudoku.replace(c,s)
                                print(newSudoku)
Remplire()                             

                        # CIBLER UN UNDERSCORE POUR L'EXEMPLE


#for (x,i) in enumerate(Sudoku):
        #Sudoku = [item.replace(Cord, "*") for item in Sudoku]
        #Sudoku = list(map(lambda st: str.remplace(st, Cord, '*'),Sudoku))
        #print(Sudoku)
        

                        # POUR SOUSTRAIRE LES DEUX LISTES ET EN TIRER LES CHIFFRES-SOLUTIONS

#print(Sudoku[:1])
#setL = set(Sudoku(1))
#resultat = setmodelLine - setmodelColumn
#print(resultat)

                        # POUR EXTRAIRE LES LIGNES ET POSSEDANT UN UNDERSCOR

#while i < len(Sudoku):
        #print(Sudoku[i][1])
        #i = i+1
print("\n\n\n")
i = 0
for Cols in range(len(Sudoku)):
    for i in range(len(Sudoku[i])):
    #print([Sudoku[i][i]]) Permet de prendre la diagonal WTF
        print(Sudoku[i][Cols])



                      
print("        \n\n\n         ")

for Rows in range(len(Sudoku)):
    for i in range(len(Sudoku[i])):
        print(Sudoku[Rows][i])
        

print("        \n\n\n         ")


z=0
  



        
"""
for i in Sudoku:
                Solution = Sudoku[i] + ModelLine
                if Solution.count(i) == 1 :
                        print(i) 
                        
"""
