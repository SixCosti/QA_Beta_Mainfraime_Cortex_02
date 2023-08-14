class Bird:
    #def _init_(self, feathersvar, colourvar):
    #self.feathers = feathersvar
    #self.colour = colourvar
    feathers = 0

    def feathers(self):
        self.feathers += 1

class Owl(Bird):
    def feathers(self):
        self.feathers += 150

joe_the_owl = Bird()
joe_the_owl.feathers()
joe_the_owl.feathers()
joe_the_owl.feathers()
print(joe_the_owl.feathers)
