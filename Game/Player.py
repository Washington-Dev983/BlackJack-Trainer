from Deck import Card

class Player:
    """
    Represents a Blackjack Player

    Attributes
    ----------
    name: str:
        Name of the player
    
    busted: boolean:
        If hand value is > 21
    
    blackJack: boolean:
        If hand consists of face card and ace
    
    hand: list[Card]:
        player's current hand
    """
    name: str
    hand: list[Card]
    bankroll: int

    def __init__(self, bankroll: int = 100, name: str = "Player"):
        """
        Parameters
        ----------
        bankroll: int
            starting number of chips
        name: str 
            Name of the player
        """
        self.name = name
        self.hand = []
        self.bankroll = bankroll

    def receiveCard(self, card: Card) -> None:
        self.hand.append(card)
    
    def getHandValue(self) -> int:
        aceCount: int = 0
        handVal: int = 0

        for card in self.hand:
            cardValue: int = card.getValue()

            handVal += cardValue
            if (cardValue == 11):
                aceCount += 1
        
        while(aceCount > 0 and handVal > 21):
            aceCount -= 1
            handVal -= 10
        
        return handVal
    
    def resetHand(self) -> None:
        self.hand = []