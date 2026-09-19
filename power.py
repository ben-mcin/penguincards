from dataclasses import dataclass
from enums import Element, Colour
from enum import Enum, auto


class PowerType(Enum):
    LOWEST_WINS = auto()
    #BONUS_PLAYER = auto()
    #DEBUFF_OPPONENT = auto()
    #ELEMENT_DISCARD = auto()
    #COLOUR_DISCARD_ONE = auto()
    #COLOUR_DISCARD_ALL = auto()
    #BUFF_ELEMENT = auto()
    #BLOCK_ELEMENT = auto()


@dataclass(frozen=True)
class Power:
    type: PowerType
    # Used by powers that need a number
    amount: int | None = None

    # Used by powers that target an element
    element: Element | None = None

    # Used by powers that target a colour
    colour: Colour | None = None