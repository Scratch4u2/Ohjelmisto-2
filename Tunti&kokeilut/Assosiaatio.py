class Koira:
    def __init__(self,nimi):
        self.nimi = nimi
    def __repr__(self):
        return "Tämä on kiva koira"

class Kauppalista:
    def __init__(self,lista):
        self.lista = lista

#lista1 = Kauppalista(["Gurg","Babrik",3,"Juusto",5])
#print(lista1.lista)

class Koulu:
    def __init__(self, nimi):
        self.nimi = nimi

class Oppilas:
    def __init__(self, nimi, koulu):
        self.koulu = koulu
        self.nimi = nimi
    def print_info(self):
        print(f"Nimi: {self.nimi}\nKoulu: {self.koulu.nimi}")

#koulu1 = Koulu("Metropolia")
#koulu2 = Koulu("Laurea")

#oppilas1 = Oppilas("Rene", koulu1)
#oppilas1.print_info()

class Kirja:
    def __init__(self,title):
        self.title = title

class Kirjasto:
    def __init__(self,nimi):
        self.nimi = nimi
        self.kirjalista = []
    def add_kirjalista(self,kirja):
        self.kirjalista.append(kirja)
    def print_info(self):
        print(f"Nimi: {self.nimi}")
        for kirja in self.kirjalista:
            print(kirja)
        print("\n")

kirja1 = Kirja("Onnin kivikirja")
kirja2 = Kirja("Renen röökikirja")
kirja3 = Kirja("Patrikin patrikirja")
kirja4 = Kirja("Jonin Ponikirja")

kirjasto1 = Kirjasto("Oodi kirjasto")
kirjasto1.add_kirjalista(kirja1.title)
kirjasto1.add_kirjalista(kirja2.title)

kirjasto2 = Kirjasto("Tikkurilan kirjasto")
kirjasto2.add_kirjalista(kirja3.title)
kirjasto2.add_kirjalista(kirja4.title)

kirjasto1.print_info()
kirjasto2.print_info()

