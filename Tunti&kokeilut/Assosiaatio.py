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

koulu1 = Koulu("Metropolia")
koulu2 = Koulu("Laurea")

class Oppilas:
    def __init__(self,nimi,koulu):
        self.koulu = koulu
        self.nimi = nimi

Oppilas1 = Oppilas(koulu1,"Rene")
