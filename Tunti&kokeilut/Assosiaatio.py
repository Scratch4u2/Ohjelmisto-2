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

koulu1 = Koulu("Metropolia")
koulu2 = Koulu("Laurea")

oppilas1 = Oppilas("Rene", koulu1)
oppilas1.print_info()