# class padre:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
    
#     def welcome (self):
#         print("Hello", self.name, " ", self.lastname)

# class hija (padre):
#     pass

# x = hija("parce", "jr")
# x.welcome()

### crear init a una clase child y que herede las variables de sus parientes

## existen dos formas de traer las variables
# Forma uno:

# class padre:
#     def __init__(self, name, lastname):
#         self.name = name
#         self.lastname = lastname
    
#     def welcome (self):
#         print("Hello", self.name, " ", self.lastname)

# class hija (padre):
#     def __init__(self, name, lastname):
#         padre.__init__(self, name, lastname)

# x = hija("parce","jr")
# x.welcome()

# forma 2, con una variable nueva y con un metodo
# con la funcion super() no necesitas el parametro self
class padre:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    
    def welcome (self):
        print("Hello", self.name, " ", self.lastname)

class hija (padre):
    def __init__(self, name, lastname, year):
        super().__init__(name, lastname)
        self.year = year
    
    def overpower(self):
        print("HELLO!!", self.name, self.lastname, "you year is:", self.year)

x = hija("John", "Fonseca", "2010")
x.overpower()