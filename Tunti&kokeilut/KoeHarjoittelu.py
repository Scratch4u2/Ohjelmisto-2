class Animal():  # Capitalized class name
    def __init__(self, species, size, latin_name):
        self.species = species
        self.size = size
        self.latin_name = latin_name

    def printInfo(self):
        print("Species: " + self.species + ", size: " + self.size + ", latin name: " + self.latin_name)


class Otter(Animal):  # Inherits from Animal
    def __init__(self, species, size, latin_name):
        super().__init__(species, size, latin_name)

class Lynx(Animal):
    def __init__(self, latin_name):
        self.latin_name = latin_name
        Animal.__init__(self,None,None,latin_name)


# Example usage:
otter1 = Otter("Sea Otter", "Medium", "Lutra lutra")
otter1.printInfo()
lynx1 = Lynx("Lynx lynx")
lynx1.printInfo()
