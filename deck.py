from card import Card, Element, Colour, Power
import random


starter_deck_regular_cards = [Card(Element.FIRE, 3, Colour.BLUE),
                              Card(Element.FIRE, 6, Colour.PURPLE),
                              Card(Element.FIRE, 2, Colour.YELLOW),
                              Card(Element.SNOW, 2, Colour.RED),
                              Card(Element.SNOW, 3, Colour.ORANGE),
                              Card(Element.SNOW, 7, Colour.YELLOW),
                              Card(Element.WATER, 5, Colour.BLUE),
                              Card(Element.WATER, 2, Colour.GREEN),
                              Card(Element.WATER, 4, Colour.PURPLE),]

starter_deck_power_cards = [Card(Element.FIRE, 10, Colour.YELLOW, Power.PLACEHOLDER),
                            Card(Element.WATER, 10, Colour.YELLOW, Power.PLACEHOLDER),
                            Card(Element.SNOW, 10, Colour.GREEN, Power.PLACEHOLDER)]



class Deck:
    def __init__(self):
        self.cards = starter_deck_regular_cards.copy()
        self.cards.append(random.choice(starter_deck_power_cards))