from constants import (
    VALID_SUITS,
    VALID_VALUES,
)
from exceptions import DeckOfCardsException
from typing import Optional


class Card(object):
    value = str()
    suit = None

    def __init__(self, value: str, suit: Optional[str] = None):
        if not isinstance(value, str) or value.lower() not in VALID_VALUES:
            raise DeckOfCardsException("Not a valid value Must be one of: %s" % " | ".join(list(VALID_VALUES)))
        if value.lower() != "joker":
            # Jokers are special. They do not have a suit so don't assign one
            if not isinstance(suit, str) or suit.lower() not in VALID_SUITS:
                raise DeckOfCardsException("Not a valid suit. Must be one of: %s" % " | ".join(list(VALID_SUITS)))
            self.suit = suit.capitalize()
        self.value = value.capitalize()

    def __str__(self):
        return "%s of %s" % (self.value, self.suit)
