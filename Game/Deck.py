import random

class Card:
    """
    A class representation of a signle card

    Attributes
    ----------
    suit: str 
        Suit of card represented as ["S", "C"," "D", "H"]
        Spades, Clubs, Diamonds, and Hearts

    value: str
        Value of card represented as ["A", "10", "9", "8"... "3", "2"]
    """
    suit: str
    value: str
    
    def __init__(self, suit: str, value: str):
        """
        Parameters
        ----------
        suit: str 
            Suit of card represented as ["S", "C"," "D", "H"]
            Spades, Clubs, Diamonds, and Hearts

        value: str
            Value of card represented as ["A", "10", "9", "8"... "3", "2"]

        """
        self.suit = suit
        self.value = value

    def getValue(self) -> int:
        if self.value in ["K", "Q", "J"]:
            return 10
        
        if self.value == "A":
            return 11
        
        return int(self.value)

    def stringRepresentation(self) -> str:
        lexicalValue: str
        lexicalSuit: str

        match self.value:
            case "K":
                lexicalValue = "King"
            case "Q":
                lexicalValue = "Queen"
            case "J":
                lexicalValue = "Jack"
            case "A":
                lexicalValue = "Ace"
            case _:
                lexicalValue = self.value
        
        match self.suit:
            case "S":
                lexicalSuit = "Spades"
            case "C":
                lexicalSuit = "Clubs"
            case "D":
                lexicalSuit = "Diamonds"
            case "H":
                lexicalSuit = "Hearts"
            case _:
                lexicalSuit = "Invalid Suit"
        
        return lexicalValue + " of " + lexicalSuit
    
class Deck:
    """
    A class representation of decks of cards

    Attributes
    ----------
    cards: list[Card]:
        idk gang a list of cards.
    """
    cards: list[Card] = []

    def __init__(self, size: int = 1, burnCards: int = 0):
        """
        Parameters
        ----------
        size: int
            number of full 52 card decks to include
        """
        SUITS: list[str] = ["D", "S", "C", "H"]
        VALUES: list[str] = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

        for _ in range(size):
            for suit in SUITS:
                for value in VALUES:
                    self.cards.append(Card(suit, value))

        self.shuffle()

        for _ in range(burnCards):
            self.cards.pop()

    def shuffle(self) -> None:
        for i in range(len(self.cards)):
            j = random.randint(0, i)

            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
