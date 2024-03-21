import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, c_nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.c_nopeus = c_nopeus
        self.kuljettu_matka = kuljettu_matka
    def kiihdytä(self, n_muutos):
        self.c_nopeus += n_muutos
        if self.c_nopeus > self.huippunopeus:
            self.c_nopeus = self.huippunopeus
        elif self.c_nopeus < 0:
            self.c_nopeus = 0
        else:
            pass
    def kulje(self, tunnit):
        self.kuljettu_matka = self.kuljettu_matka + (self.c_nopeus * tunnit)
    def print_info(self):
        print(f"Rekisteritunnus:{self.rekisteritunnus}\nHuippunopeus:{self.huippunopeus}kmh\nKuljettu matka:{self.kuljettu_matka}\nTämänhetkinen nopeus: {self.c_nopeus}kmh \n")


auto1 = Auto("ABC-123",142,0,0)
auto1.print_info()
auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
auto1.kiihdytä(-200)
auto1.print_info()
auto1.kulje(1.5)
auto1.print_info()

auto = []

for i in range(1, 11):
    nopeus = random.randint(100, 200)
    i_arvo = f"ABC-{i}"
    auto_i = Auto(i_arvo, nopeus,0,0)
    auto.append(auto_i)

yli_10000 = False
while not yli_10000:
    for i in range(len(auto)):
        n_muutos = random.randint(-10, 15)
        auto[i].kiihdytä(n_muutos)
        auto[i].kulje(1)
        print(auto[i].print_info())
        if auto[i].kuljettu_matka >= 10000:
            yli_10000 = True
            break
