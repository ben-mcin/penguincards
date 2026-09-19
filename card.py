from dataclasses import dataclass
from enums import Element, Colour
from power import Power

@dataclass(frozen=True)
class Card:
    element: Element
    number: int
    colour: Colour
    power: Power | None = None

    def __str__(self):
        return f"{self.element.value} {self.number} {self.colour.value}"
    
    def __repr__(self):
        return str(self)

    # Card creation check, can be removed once cards are defined
    def __post_init__(self):
        if not 1 <= self.number <= 12:
            raise ValueError("Card number must be between 1 and 12")
        if self.number >= 10 and self.power is None:
            raise ValueError("Cards numbered 10-12 must have a power")
        if self.number < 10 and self.power is not None:
            raise ValueError("Cards numbered 1-9 cannot have a power")
        