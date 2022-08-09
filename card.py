from constants import (
    VALID_SUITS,
    VALID_VALUES,
)


class Card(object):
    # TODO: Jokers do not have a suit, so they should be handled in a special way
    suit = str()
    value = str()

    def __init__(self, value: str, suit: str):
        if not isinstance(suit, str) or suit.lower() not in VALID_SUITS:
            raise Exception("Not a valid suit. Must be one of: %s" % " | ".join(list(VALID_SUITS)))
        if not isinstance(value, str) or value.lower() not in VALID_VALUES:
            raise Exception("Not a valid value Must be one of: %s" % " | ".join(list(VALID_VALUES)))
        self.suit = suit.capitalize()
        self.value = value.capitalize()

    def __str__(self):
        return "%s of %s" % (self.value, self.suit)
