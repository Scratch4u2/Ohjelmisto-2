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
    def __init__(self,species, size,latin_name, fur_type):
        Animal.__init__(self, species, size, latin_name)
        self.fur_type = fur_type
    def printInfo(self):
        Animal.printInfo(self)
        print("Fur type: " + self.fur_type)

# Example usage:
otter1 = Otter("Sea Otter", "Medium", "Lutra lutra")
otter1.printInfo()
lynx1 = Lynx("Arctic lynx", "Medium", "Lynx lynx", "Thick")
lynx1.printInfo()
