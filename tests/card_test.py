import pytest

from card import Card
from exceptions import DeckOfCardsException


def test_exception_is_raised_if_invalid_suit():
    with pytest.raises(DeckOfCardsException):
        Card("Ace", "Pyramids")


def test_exception_is_raised_if_invalid_value():
    with pytest.raises(DeckOfCardsException):
        Card("0", "Hearts")


def test_valid_card_creation():
    card = Card("7", "Hearts")
    assert card.value == "7"
    assert card.suit == "Hearts"
