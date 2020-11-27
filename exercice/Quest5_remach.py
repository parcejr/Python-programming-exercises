class oli:
    def __init__(self): 
        self.l = ""
    
    def getInput(self):
        print("Escribe algo")
        self.l = input()
    
    def mostrar(self):
        x = self.l
        print(x.upper())

h = oli()
h.getInput()
h.mostrar()