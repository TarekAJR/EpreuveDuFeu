#coding:utf-8

import sys

print("                             EPREUVE DU FEU : L'ESCALIER\n\n\n")



ETAGE = sum(map(int, sys.argv[1]))
newETAGE = (sum(map(int, sys.argv[1])) - (sum(map(int, sys.argv[1])) - 1))
ESPACE = (sum(map(int, sys.argv[1])) - 1)
	
while newETAGE != ETAGE :
	print (( ESPACE * " ") + (newETAGE * "#" ))
	ESPACE = ESPACE - 1
	newETAGE = newETAGE + 1
	if newETAGE == ETAGE :
		print (newETAGE * "#")
