import pytest
from libs.deck import Deck
from libs.player import Player

def test_initial_setting():
    p = Player()
    assert p.cards == []
    assert p.score == 0


@pytest.fixture
def default_deck():
    return Deck()

@pytest.mark.parametrize("deck, expected_card, expected_score", [
    (
        [('Clubs', 'Ace'), ('Spades', 2), ('Diamonds', 5), ('Hearts', 3)],
        ('Clubs', 'Ace'),
        4
    ),
    (
        [('Diamonds', 'King'), ('Hearts', 3), ('Clubs', 'Ace'), ('Spades', 2)],
        ('Diamonds', 'King'),
        26
    )
])
def test_draw(default_deck, deck, expected_card, expected_score):
    default_deck.cards = deck
    p = Player()
    p.draw(default_deck)

    assert p.cards[0] == expected_card
    assert p.score == expected_score
