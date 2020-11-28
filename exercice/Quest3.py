# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()

### existen dos formas de crear diccionarios

# x = dict(
#     name = "jhon",
#     age = 36,
#     country = "Norway",
#     country = "Liverpool"
# )

## Diccionarios es como una lista desordenada que no permite llaves iguales, en este ejemplo al tener 2 ciudades, bota error

# y = {
#     "name": "jhon",
#     "age": 36,
#     "country": "Norway",
#     "country": "Liverpool"
#     }
# print(y)
## en esta forma remplaza el valor de la llave country


## My Solution
print("escribe un numero entero")
valor = int(input())

diccionario = dict()
print(type(valor))

i = 1
while i <= valor:
    diccionario[i] = i * i
    i += 1

print(diccionario)

## Solution Master:

# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i

# print(d)