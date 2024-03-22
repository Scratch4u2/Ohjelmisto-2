

#Tehtävät 1-3 moduuli 10

class Hissi():
    def __init__(self,alin_kerros,ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nyt_kerros = alin_kerros
    def kerros_ylös(self):
        self.nyt_kerros += 1
    def kerros_alas(self):
        self.nyt_kerros -= 1
    def siirry_kerrokseen(self,kerrosnumero):
        print(f"Olet nyt kerroksessa: {self.nyt_kerros}")
        if kerrosnumero < self.nyt_kerros:
            while kerrosnumero < self.nyt_kerros:
                self.kerros_alas()
                print(F"Kerros:{self.nyt_kerros}")
        else:
            while kerrosnumero > self.nyt_kerros:
                self.kerros_ylös()
                print(F"Kerros:{self.nyt_kerros}")
        print(f"Olet nyt kerroksessa: {self.nyt_kerros}")



#h1 = Hissi(0,7)
#h1.siirry_kerrokseen(5)

class Talo():
    def __init__(self, alin_kerros, ylin_kerros, hissimaara):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissim = hissimaara
        self.hissilista = []
        for i in range(0, hissimaara):
            hissi_i = Hissi(alin_kerros,ylin_kerros)
            self.hissilista.append(hissi_i)
    def aja_hissiä(self, hissinumero, kohdekerros):
        self.hissinumero = hissinumero
        self.kohdekerros = kohdekerros
        hissinumero = self.hissilista[hissinumero]
        hissinumero.siirry_kerrokseen(kohdekerros)
    def palohalytys(self):
        for i in range(len(self.hissilista)):
            self.hissilista[i].siirry_kerrokseen(0)

talo1 = Talo(0,7,3)
talo1.aja_hissiä(2,3)
talo1.palohalytys()
