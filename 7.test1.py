import sys

print(" ")
print("                                 EPREUVE DU FEU : SUDOKU\n")


ModelLine = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '|', '|']
ModelColumn = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '-']
Solution = []
setmodelLine = set(ModelLine)
setmodelColumn = set(ModelColumn)
Emplacements = '_'
Exclure = '---+---+---'
Exclure1 = '|||+|||+|||'
Sudoku = open(sys.argv[1],"r").read()


i = 0
line = 0
Cols = 0
Rows = 0

ListCols = []
ListRows = []
Solution = []
newSudoku = []

Sudoku = [list(i) for i in Sudoku.split()]
print(i)


def BonneReponse():
        z=0
        i=0
        for i in range(0, 11):
                Probleme = [ z for z in Sudoku[i]]
                Solution = (list(set(ModelLine) - set(Sudoku[i])))
                
                if 0 < len(Solution) < 3 :
                        print(Solution)
                        

print('\n\n')

for x,line in enumerate(Sudoku):
                print(line)
                for y,Underscore in enumerate(line):
                        if Underscore == Emplacements:
                                print((x,y))
                        
                      

BonneReponse()
print('\n\n')






                        # CIBLER UN UNDERSCORE POUR L'EXEMPLE
"""
i=0
for Emplacement in Sudoku:
        Resultat = ModelLine - (Sudoku[8])
        Sudoku[8] = [Sudoku[8].replace(Emplacement, Resultat)]
        print(Sudoku[8])
"""
                        # POUR SOUSTRAIRE LES DEUX LISTES ET EN TIRER LES CHIFFRES-SOLUTIONS

#print(Sudoku[:1])
#setL = set(Sudoku(1))
#resultat = setmodelLine - setmodelColumn
#print(resultat)

                        # POUR EXTRAIRE LES LIGNES ET POSSEDANT UN UNDERSCOR

#while i < len(Sudoku):
        #print(Sudoku[i][1])
        #i = i+1

i = 0
for Cols in range(len(Sudoku)):
    for i in range(len(Sudoku[Cols])):
        "for Emplacement in Sudoku :"
    #print([Sudoku[i][i]]) Permet de prendre la diagonal WTF
        print([Sudoku[i][Cols]])



                      
print("        \n\n\n         ")

for Rows in range(len(Sudoku)):
    for i in range(len(Sudoku[Rows])):
        print([Sudoku[Rows][i]])

print("        \n\n\n         ")       
print(Sudoku)
print(i)

print("\n\n")



"""
        i=10
        for i in Sudoku[i]:
                if i in ModelLine :
                        Resultat = ModelLine.remove(Sudoku[i])
                        print([Resultat])

"""
"""
        z=11
        while z != 0:
                Solution = Sudoku[z] + ModelLine
                z=-1
                if Solution.count(z) == 1 :
                        print(z) 
                        
        """
        

