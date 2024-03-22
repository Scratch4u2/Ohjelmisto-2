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


h1 = Hissi(0,7)
h1.siirry_kerrokseen(5)