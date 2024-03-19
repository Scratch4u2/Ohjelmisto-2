class Player:
    player_count = 0
    def __init__(self, nimi, s_location):
        Player.player_count += 1
        print(f"Luodaan uusi pelaaja, pelaaja: {Player.player_count}")
        self.nimi = nimi
        self.score = 0
        self.level = 1
        self.location = s_location
    def move_to_location(self, target):
        self.location = target
    def up_level(self):
        self.level = self.level + 1
    def add_score(self):
        self.score += self.level * 10
    def print_info(self):
        print(f"Nimi:{self.nimi}, Score:{self.score}, Location:{self.location} ")


p1 = Player("Joni", "Suomi")
p2 = Player("Onni", "Ruotsi")
p3 = Player("Rene","Ranska")

print(Player.player_count)

p1.move_to_location("Norja")
p1.up_level()
p1.add_score()

print(f"Nimi:{p1.nimi}, Score:{p1.score}, Location:{p1.location} ")
p1.print_info()


players_l = []
players_l.append(Player("Aku", "Ankkalinna"))
players_l.append(p1)

for p in players_l:
    p.print_info()
