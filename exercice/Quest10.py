# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

## Tener en cuenta:
# sort() sirve solo para trabajar con listas y no afecta los datos, sorted() si nos permite ordenar los datos de una determinada manera.

def main():
    ## My Solution
    print("escribe una frase")
    dato = input()
    drydata = set(dato.split(" "))
    dry = sorted(drydata)
    print(" ".join(dry))

    ## Solution master
    # s = input()
    # words = [word for word in s.split(" ")]
    # print(" ".join(sorted(list(set(words)))))



if __name__ == "__main__":
    main()