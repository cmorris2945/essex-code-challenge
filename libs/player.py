"""A module of a card player and related methods

This module contains the class of a card player and the related methods.

Typical usage example:

    p = Player()
    p.draw()
"""

class Player:
    """A class of a player of the card game.

    A class of a player of the card game and related methods

    Attributes:
        cards: An array of cards in the player's hand. Each card is a tuple with
               suits and number, such as ("Spades", 2)
        score: The score of the cards in the player's hand
    """

    def __init__(self):
        self.cards = []
        self.score = 0

    def draw(self, deck):
        """Draw the card to the player's hand and calculate the total score of
           the cards in the hand.

        Args:
            deck: the deck available to draw
        """

        draw_card = deck.draw()
        self.cards.append(draw_card)

        suit_scores = {
            'Spades': 1,
            'Diamonds': 2,
            'Hearts': 3,
            'Clubs': 4
        }

        if draw_card[1] == "Ace":
            self.score = self.score + suit_scores[draw_card[0]]*1
        elif draw_card[1] == "Jack":
            self.score = self.score + suit_scores[draw_card[0]]*11
        elif draw_card[1] == "Queen":
            self.score = self.score + suit_scores[draw_card[0]]*12
        elif draw_card[1] == "King":
            self.score = self.score + suit_scores[draw_card[0]]*13
        else:
            self.score = self.score + suit_scores[draw_card[0]]*draw_card[1]
