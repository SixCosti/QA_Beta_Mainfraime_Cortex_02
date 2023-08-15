class Bird:

    def __init__(self, feathersvar, colourvar):
        self.feathers = feathersvar
        self.colour = colourvar
    #feathers = 0

    def increase_feathers(self):
        self.feathers += 1

    def eating(self):
        pass

class Owl(Bird):
    def increase_feathers(self):
        self.feathers += 150

class Dodo(Bird):
    def __init__(self, feathersvar, colourvar):
        Bird.__init__(self, feathersvar, colourvar)  # Calling parent class constructor
        self.extinct = True

    def eating(self):
       return 'Fish'


joe_the_owl = Owl(150, "Flamingo Pink")
albert_the_dodo = Dodo(200, "Stellar Blue")
#joe_the_owl.increase_feathers()
#joe_the_owl.increase_feathers()
#joe_the_owl.increase_feathers()
#print(joe_the_owl.feathers)


# Use the 4 OOP principles
# 1. Encapsulation: Access attributes through methods
joe_the_owl.increase_feathers()
albert_the_dodo.increase_feathers()

# 2. Inheritance: Owl and Dodo inherit from Bird
print(joe_the_owl.colour)  
print(albert_the_dodo.feathers)  

# 3. Polymorphism: Same method name behaves differently in Owl and Dodo
print(joe_the_owl.feathers)  # Prints Owl's implementation
print(albert_the_dodo.feathers)  # Prints Dodo's inherited feathers + 1

# 4. Abstraction: Having an abstract attribute in the parent class then creating it within a child class
print(albert_the_dodo.extinct)  # Accessing encapsulated attribute
print(albert_the_dodo.eating())


print(albert_the_dodo.colour) 

