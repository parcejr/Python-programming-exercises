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

### QUEST
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