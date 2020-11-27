# class Quest5:
#     def __init__(self, valor):  
#         self.valor = valor
     
#     def printString(self):
#         print(self.valor)

# print("Cual es tu nombre")
# result = input()
# invo = Quest5(result)
# print(invo.printString())

### Solution:
class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

strObj = InputOutString()
strObj.getString()
strObj.printString()