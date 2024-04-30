class Kirjasto:
    def __init__(self, numero, nimi):
        self.numero = numero
        self.nimi = nimi
    def print_i(self):
        print(self.numero, self.nimi)
class Kirja(Kirjasto):
    def __init__(self, numero, nimi, kirjailija):
        super().__init__(numero, nimi)
        self.kirjailija = kirjailija
    def print(self):
        super().print_i()
        print(self.kirjailija)

class Sarjakuva(Kirjasto):
    def __init__(self, numero, nimi, kuvittaja):
        Kirjasto.__init__(self, numero, nimi)
        self.kuvittaja = kuvittaja
    def print_i(self):
        Kirjasto.print_i(self)
        print(self.kuvittaja)

kirjasto = Kirjasto(1,"Tikkurilan Kirjasto")
sarjakuva1 = Sarjakuva(123,"Aku Ankka", "Don Rosa")
kirja1 = Kirja(123,"Sinuhe", "Mika Waltari")

kirja1.print_i()
sarjakuva1.print_i()
kirjasto.print_i()