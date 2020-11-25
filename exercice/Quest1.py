for x in range(2000, 3201):
    if(x % 7 == 0 and x % 5 != 0):
        print(x)

# Solution Master
l = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l)) # join anexa un separador por cada elemento, en este caso una coma

