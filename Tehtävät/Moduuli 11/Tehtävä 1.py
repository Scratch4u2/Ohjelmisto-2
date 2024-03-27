class Julkaisu:
    def __init__(self, tyyppi, nimi):
        self.tyyppi = tyyppi
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"Tyyppi: {self.tyyppi}\nNimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self, tyyppi, nimi, kirjoittaja, sivumaara):
        super().__init__(tyyppi, nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja : {self.kirjoittaja}\nSivumaara : {self.sivumaara}\n")

class Lehti(Julkaisu):
    def __init__(self, tyyppi, nimi, paatoimittaja):
        super().__init__(tyyppi, nimi)
        self.paatoimittaja = paatoimittaja
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}\n")


AkuAnkka = Lehti("Lehti", "Aku_Ankka","Aki Hyyppä")
Hytti_n6 = Kirja("Kirja", "Hytti_n6", "Rosa Liksom", 200)

AkuAnkka.tulosta_tiedot()
Hytti_n6.tulosta_tiedot()