import pytest
import random
from libs.deck import Deck

@pytest.fixture
def default_deck():
    return Deck()

def test_default_deck_setting(default_deck):
    assert len(default_deck.cards) == 52


    suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    for s in range(4):
            for i in range(1, 14):
                if i == 1:
                    assert default_deck.cards[s*13+i-1][0] == suits[s]
                    assert default_deck.cards[s*13+i-1][1] == 'Ace'
                elif i == 11:
                    assert default_deck.cards[s*13+i-1][0] == suits[s]
                    assert default_deck.cards[s*13+i-1][1] == 'Jack'
                elif i == 12:
                    assert default_deck.cards[s*13+i-1][0] == suits[s]
                    assert default_deck.cards[s*13+i-1][1] == 'Queen'
                elif i == 13:
                    assert default_deck.cards[s*13+i-1][0] == suits[s]
                    assert default_deck.cards[s*13+i-1][1] == 'King'
                else:
                    assert default_deck.cards[s*13+i-1][0] == suits[s]
                    assert default_deck.cards[s*13+i-1][1] == i

@pytest.mark.parametrize("seed, deck, expected", [
    (10,
     [('Spades', 2), ('Diamonds', 5), ('Hearts', 3), ('Clubs', 'Ace')],
     [('Clubs', 'Ace'), ('Hearts', 3), ('Diamonds', 5), ('Spades', 2)]),
    (0,
     [('Spades', 2), ('Diamonds', 5), ('Hearts', 3), ('Clubs', 'Ace')],
     [('Hearts', 3), ('Spades', 2), ('Diamonds', 5), ('Clubs', 'Ace')])
])
def test_shuffle(seed, deck, expected):
    random.seed(seed)
    d = Deck()
    d.cards = deck

    d.shuffle()

    

    for i in range(len(d.cards)):
        assert d.cards[i] == expected[i]

def test_sort_cards():
    d = Deck()
    d.cards = [
        ('Spades', 2),
        ('Diamonds', 5),
        ('Spades', 'King'),
        ('Spades', 'Jack'),
        ('Spades', 'Ace'),
        ('Spades', 'Queen'),
        ('Hearts', 3),
        ('Clubs', 'Ace')
    ]

    d.sort_cards()

    expected_cards = [
        ('Spades', 2),
        ('Spades', 'Jack'),
        ('Spades', 'Queen'),
        ('Spades', 'King'),
        ('Spades', 'Ace'),
        ('Diamonds', 5),
        ('Hearts', 3),
        ('Clubs', 'Ace')
    ]

    for i in range(len(d.cards)):
        assert d.cards[i] == expected_cards[i]

@pytest.mark.parametrize("deck, expected", [
    ([('Spades', 2), ('Diamonds', 5), ('Hearts', 3), ('Clubs', 'Ace')], ('Spades', 2)),
    ([], None)
])
def test_draw(deck, expected):
    d = Deck()
    d.cards = deck
    drawed_card = d.draw()

    assert drawed_card == expected
