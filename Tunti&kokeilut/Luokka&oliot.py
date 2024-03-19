class Player:
    def __init__(self, nimi, s_location):
        print("Luodaan uusi pelaaja")
        self.nimi = nimi
        self.score = 0
        self.location = s_location

p1 = Player("Joni", "Suomi")
p2 = Player("Onni", "Ruotsi")
p3 = Player("Rene","Ranska")

print(f"Nimi:{p1.nimi}, Score:{p1.score}, Location:{p1.location} ")

