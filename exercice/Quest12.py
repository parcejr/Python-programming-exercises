# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

## MY SOLUTION
# lista = list()

# for i in range(1000,3001):
#     if i % 2 == 0:
#         l = str(i)
#         lista.append(l)

# print(','.join(lista))

listaDeDatos = list()
print("escribe un numero de 1000 a 3000")
dato = input()
# print(type(dato))

if int(dato) >= 1000 | int(dato) <= 3000:
    for i in dato:
        if int(i) % 2 == 0:
            listaDeDatos.append(i)

print(','.join(listaDeDatos))

## SOLUTION MASTER

# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))