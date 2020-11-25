pregunta = [1,2,3,4]
pregunta[1] = 5
# print(pregunta)

listones = [1,2,4,2,1,4,5,67,7,7686,5,34543523]
listones.sort(reverse = True)
# print(listones)

abv = [1,2,3,4,5]
asd = abv
copymethod = abv.copy()
listamethod = list(abv)
abv.append(6)
print(asd)
print(copymethod)
print(listamethod)

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])