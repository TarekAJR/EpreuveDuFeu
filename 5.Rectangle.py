import sys

print(" ")
print("                         EPREUVE DU FEU : RECTANGLE\n")


File1 = open(sys.argv[1], "r").read()
File2 = open(sys.argv[2], "r").read()

File1 = [list(i) for i in File1.split("\n")[:-1]]
File2 = [list(i) for i in File2.split("\n")[:-1]]

Curseur = 0
Coord = list()
for y in range(len(File2)):
    try:
        for i in range(len(File2[y])):
            if File2[y][i] == File1[Curseur][0]:
                if File2[y][i+1] == File1[Curseur][1]:
                    if File2[y][i+2] == File1[Curseur][2]:
                        print(File2[y][i:i+3])
                        Curseur+=1
                        Coord.append((i,y))
                        
    except:
        pass
print(Coord[0])


