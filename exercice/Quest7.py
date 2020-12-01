
# Level 2

# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

# # My Solution
print("Escribe el # de Filas: ")
Y = int(input())
print("Escribe el # de Columnas: ")
X = int(input())
print(X, Y)

mtx = [list(range(X)) for _ in range(Y)] # _ funciona como variable y es muy utilizada en loops de una sola linea

for i in range(X):  # tuve problemas a la hora de definir columnas y filas, la solución era intercambiar las posiciones,
    for j in range(Y):
        mtx[j][i] = i*j

print(mtx)
#NOTAS: 
    # Estar atento a las posiciones de las filas y las columnas, me mostraba un error de lista fuera de rango, y eso solo se solucionaba cambiano las posiciones

# # Solution Master
# input_str = input()
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=dimensions[0]
# colNum=dimensions[1]
# multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# for row in range(rowNum):
#     for col in range(colNum):
#         multilist[row][col]= row*col

# print(multilist)