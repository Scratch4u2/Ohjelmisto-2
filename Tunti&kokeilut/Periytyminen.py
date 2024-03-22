class Animal:
    def __init__(self, species):
        self.species = species
    def speak(self):
        print("I speak animal")
class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed
    def speak(self):
        print("Wuf, Wuf")

animal1 = Animal("dog")
animal2 = Animal("cat")
dog1 = Dog(animal1, "Bordercollie")
dog2 = Dog(animal1, "Pug")

#dog1.speak()

class Ihminen:
    def __init__(self,nimi,ikä):
        self.nimi = nimi
        self.ikä = ikä
    def tervehdys(self):
        print(f"Hei, nimeni on {self.nimi} ja olen {self.ikä}-vuotta")

ihminen1 = Ihminen("Rene","28")
ihminen1.tervehdys()