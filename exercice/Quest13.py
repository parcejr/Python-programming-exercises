# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


## MY SOLUTION
print("escribe lo que quiera: ", end="")
dato = input()
newdata = dato.replace(" ", "")
# print(newdata)
LETTERS = 0
DIGITS = 0                   

for i,x in enumerate(newdata):
    lista = {"1","2","3","4","5","6","7","8","9","0"}
    contador = DIGITS
    for j in lista:
        if x == j:
            DIGITS += 1
    if contador == DIGITS:
        LETTERS += 1

print(f"LETTER: {LETTERS}")
print(f"DIGITS: {DIGITS}")

##SOLUTION MASTER
# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit(): # insdigit es un metodo que identifica si un caracter es un entero
#         d["DIGITS"]+=1
#     elif c.isalpha(): # identifica si un caracter es una letra
#         d["LETTERS"]+=1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])