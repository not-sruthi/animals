class Animals (object):
    def __init__(self, name, species, habitat):
        self.name=name
        self.species=species
        self.habitat=habitat

    def diet(self):
        self.food=input (self.name + ": Is this animal a herbivore or a carnivore? ")
        return(self.name + " is a " + self.food)

    def good(self):
        self.isgood=input ("Is " + self.name + " a good boy? (or girl)")
        return("Ah, I see. So your answer is " + self.isgood + ".")


cat = Animals('Cat','Feline','Cat places')
print(cat.diet())
print(cat.good())