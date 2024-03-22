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
    def kulje(self, tunnit):
        self.kuljettu_matka += self.c_nopeus * tunnit
    def print_info(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}, Huippunopeus: {self.huippunopeus} km/h, Kuljettu matka: {self.kuljettu_matka} km, Tämänhetkinen nopeus: {self.c_nopeus} km/h")

class Kilpailu:
    def __init__(self, nimi, pituus_km, auto_lista):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.auto_lista = auto_lista
    def tunti_kuluu(self):
        for auto in self.auto_lista:
            n_muutos = random.randint(-10, 15)
            auto.kiihdytä(n_muutos)
            auto.kulje(1)
            auto.print_info()
    def tulosta_tilanne(self):
        for auto in self.auto_lista:
            auto.print_info()
    def kilpailu_ohi(self):
        for auto in self.auto_lista:
            if auto.kuljettu_matka >= self.pituus_km:
                return True
        return False

autolist = []
for i in range(1, 11):
    nopeus = random.randint(100, 200)
    i_arvo = f"ABC-{i}"
    auto_i = Auto(i_arvo, nopeus, 0, 0)
    autolist.append(auto_i)

kilpailu1 = Kilpailu("Suuri Romuralli", 8000, autolist)

while kilpailu1.kilpailu_ohi() != True:
    kilpailu1.tunti_kuluu()
    kilpailu1.kilpailu_ohi()
    for i in range(0,11):
        if kilpailu1.kilpailu_ohi() == True:
            print("\nLopullinen tilanne\n")
            kilpailu1.tulosta_tilanne()
            break
        if i == 10:
            print("\nVälikatsaus\n")
            kilpailu1.tulosta_tilanne()
            i -= 10
