"""A module of a card deck and related methods

This module contains the class of a cards deck and the related methods.

Typical usage example:

    d = Desk()
    d.shuffle()
"""

import random

class Deck:
    """A class of a standard 52-card deck.

    A class of a standard 52-card and related methods

    Attributes:
        cards: An array of cards. Each card is a tuple with suits and number,
               such as ("Spades", 2)
    """

    def __init__(self):
        self.cards = []
        self.__build()

    def __build(self):
        """Create a standard 52-card deck."""
        for s in ['Spades', 'Diamonds', 'Hearts', 'Clubs']:
            for i in range(1, 14):
                if i == 1:
                    self.cards.append((s, 'Ace'))
                elif i == 11:
                    self.cards.append((s, 'Jack'))
                elif i == 12:
                    self.cards.append((s, 'Queen'))
                elif i == 13:
                    self.cards.append((s, 'King'))
                else:
                    self.cards.append((s, i))

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def __sort_func(self, c):
        """Custom sorting function combining suits and number of the card."""
        suit_scores = {
            'Spades': 0,
            'Diamonds': 1,
            'Hearts': 2,
            'Clubs': 3
        }

        if c[1] == "Ace":
            return suit_scores[c[0]]*13 + 13
        elif c[1] == "Jack":
            return suit_scores[c[0]]*13 + 10
        elif c[1] == "Queen":
            return suit_scores[c[0]]*13 + 11
        elif c[1] == "King":
            return suit_scores[c[0]]*13 + 12
        else:
            return suit_scores[c[0]]*13 + c[1] - 1

    def sort_cards(self):
        """Sort the deck in ascending order."""
        self.cards.sort(key=self.__sort_func)

    def draw(self):
        """Draw the top card from the deck.

        Returns:
            The top card in the deck or None if there is no card in the deck.
        """
        try:
            return self.cards.pop(0)
        except IndexError as _:
            print("No deck is left")
            return
