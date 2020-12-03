# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# ## MY SOLUTION
land = list()
print("Escribe una lista de numeros binaries")
dato = input()
land = dato.split(",")
# print(land)
resultado = []

for i in land: 
    datafono = reversed(i) # Al igual que son sort y sorted(), este si devuelve el valor.
    suma = 0
    for y,j in enumerate(datafono):
        if j == "1":
            binario = 2 ** y
            suma += binario
    if suma % 5 != 0:
        resultado.append(i)

print("Tu resultado es: ")
print(",".join(resultado))

## MASTER SOLUTION
# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)

# print(','.join(value))