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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, c_nopeus, kuljettu_matka, akku_kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus, c_nopeus, kuljettu_matka)
        self.akku_kapasiteetti = akku_kapasiteetti
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, c_nopeus, kuljettu_matka, bensatankin_koko):
        super().__init__(rekisteritunnus, huippunopeus, c_nopeus, kuljettu_matka)
        self.bensatankin_koko = bensatankin_koko

sahkoauto = Sahkoauto("ABC-15", 180,100,0, 52.5)
bensaauto = Polttomoottoriauto("ACD-123", 165,120,0, 32.3)

sahkoauto.kulje(3)
sahkoauto.print_info()

bensaauto.kulje(3)
bensaauto.print_info()
