lista = list()
print("escribe datos sin parar: ")
while True:
    holis = input()

    if holis:
        lista.append(holis.upper())
    else:
        break

print(','.join(lista))

## Se ve mejor separado por comas :D
## A tener en cuenta:
#  cuando escribes un while True, dentro tiene que venir una condicional, para que el ciclo se repita, en este caso si habia input, la condición se seguia repitiendo y para detenerla, usamos un break.