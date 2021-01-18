from libs.deck import Deck
from libs.player import Player

d = Deck()
d.shuffle()

player_1 = Player()
player_2 = Player()

for i in range(3):
    player_1.draw(d)
    player_2.draw(d)

if player_1.score > player_2.score:
    print("Player 1 wins")
elif player_1.score < player_2.score:
    print("Player 2 wins")
else:
    print("Tie")
