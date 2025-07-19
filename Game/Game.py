from Deck import Deck, Card
from Player import Player
from math import floor
from time import sleep # For suspense, remove later

class Game:
    """
    Representation of current blackjack session

    Attributes
    ----------
    dealer: Player:
        The dealer of the game
    
    player: Player:
        The human player character
    
    deck: Deck:
        The current deck being used
    """
    dealer: Player = Player("Dealer")
    player: Player
    startingBankroll: int
    deckSize: int
    burnCards: int
    deck: Deck

    def __init__(self, playerName: str, deckSize: int, startingBankroll: int, burnCards: int):
        """
        Parameters
        ----------
        playerName: str
            Name of the player
        
        deckSize: int
            Number of decks to use in the game
        """
        self.player = Player(startingBankroll, playerName)
        self.deckSize = deckSize
        self.burnCards = burnCards
        self.deck = Deck(deckSize, burnCards)

    def playerTurn(self) -> None:
        playerTurn: bool = True
        playerHandValue: int = self.player.getHandValue()


        print(f"Your hand is...")

        for card in self.player.hand:
            print(f"{card.stringRepresentation()}")
            
        print(f"\nHand Total: {playerHandValue}")
        
        while(playerTurn):
            if(playerHandValue >= 21):
                print("Turn ending. No available moves\n")
                break

            command: str = input("Would you like to stand, hit, or check hands [S/H/C]").upper()

            match command:
                case "S":
                    print(f"Turn ending. Final hand total: {self.player.getHandValue()}\n")
                    playerTurn = False
                case "H":
                    drawnCard: Card = self.deck.cards.pop()
                    playerHandValue += drawnCard.getValue()
                    self.player.hand.append(drawnCard)

                    print(f"Drawn card is {drawnCard.stringRepresentation()}")
                    print(f"Hand total: {playerHandValue}")
                case "C":

                    print(f"The Dealer Shows a {self.dealer.hand[0].stringRepresentation()}\n")

                    print("Your hand is...")

                    for card in self.player.hand:
                        print(f"{card.stringRepresentation()}")
                    
                    print(f"\nHand Total: {playerHandValue}")
                case _:
                    print("Invalid option please enter S to stand, H to hit, or C to check hand")
        
        return playerHandValue

    def dealerTurn(self) -> None:
        dealerTurn: bool = True
        dealerHandValue: int = self.dealer.getHandValue()

        print(f"The dealer's hand is...")

        for card in self.dealer.hand:
            print(f"{card.stringRepresentation()}")

        print(f"Dealer hand total: {dealerHandValue}")

        while(dealerTurn):
            sleep(.75) # Literally just here for suspence, remove later

            if(dealerHandValue < 16):
                drawnCard: Card = self.deck.cards.pop()
                dealerHandValue += drawnCard.getValue()

                print(f"Dealer draws a {drawnCard.stringRepresentation()}")
                print(f"Dealer hand total: {dealerHandValue}")
                self.dealer.hand.append(drawnCard)
            else:
                print(f"Dealer turn ending. Final hand total: {dealerHandValue}\n")
                dealerTurn = False

        return dealerHandValue

    def runGame(self) -> None:
        continuePlay: bool = True

        while(continuePlay):
            print(f"current deck size: {len(self.deck.cards)}")
            if (len(self.deck.cards) < floor(52 * self.deckSize *.4)):
                print("Deck low. Shuffling new deck")
                self.deck = Deck(self.deckSize, self.burnCards)

            self.dealer.resetHand()
            self.player.resetHand()

            while(True):
                if(self.player.bankroll <= 0):
                    print("You're out of money... Have 10 to play with")
                    self.player.bankroll = 10
                playerBet: int = int(input(f"How much will you bet? Current bankroll: {self.player.bankroll}\n"))

                if(playerBet > self.player.bankroll):
                    print("Not enough chips. Please choose a value less than your bankroll")
                else:
                    break

            for _ in range(2):
                self.dealer.receiveCard(self.deck.cards.pop())
                self.player.receiveCard(self.deck.cards.pop())

            dealerUpCard: str = self.dealer.hand[0].stringRepresentation()

            print(f"~~The Dealer Shows a {dealerUpCard}~~\n")

            print(f"~~{self.player.name}'s Turn~~")
            playerFinalTotal: int = self.playerTurn()
            print(f"~~Dealer's Turn~~")
            dealerFinalTotal: int = self.dealerTurn()

            print("Game ending. Final values are...")
            print(f"{self.player.name}: {playerFinalTotal}")
            print(f"Dealer: {dealerFinalTotal}")

            if(playerFinalTotal > 21):
                print(f"{self.player.name} Busted! You lost {playerBet} chips")
                self.player.bankroll -= playerBet
            
            elif(dealerFinalTotal == 21):
                print(f"Dealer got Blackjack! You lost {playerBet} chips")
                self.player.bankroll -= playerBet
            
            elif(playerFinalTotal == 21):
                print(f"{self.player.name} got Blackjack! You got {playerBet * 1.5} chips")
                self.player.bankroll += playerBet * 1.5

            elif(dealerFinalTotal > 21):
                print(f"Dealer busted! Yo got {playerBet} chips")
                self.player.bankroll += playerBet
            
            elif(dealerFinalTotal > playerFinalTotal):
                print(f"Dealer won! You lost {playerBet} chips")
                self.player.bankroll -= playerBet

            elif(dealerFinalTotal < playerFinalTotal):
                print(f"{self.player.name} won! You won {playerBet} chips")
                self.player.bankroll += playerBet

            else:
                print("A push. No chips lost")

            while(True):
                command: str = input("Play again? [Y/N]").upper()

                match command:
                    case "Y":
                        print("Starting next game")
                        break
                    case "N":
                        continuePlay = False
                        break
                    case _:
                        print("Please type Y to play again or N to stop")



# Testing purposes
startingBankroll: int = int(input("How many chips will you start with?\n"))
deckSize: int = int(input("How many decks will be used?\n"))
burnCards: int = int(input("How many cards should be burnt from the deck\n"))
playerName: str = input("What is your name?\n")

print("\n\n~~Game starting~~\n")
newGame: Game = Game(playerName, deckSize, startingBankroll, burnCards)
newGame.runGame()
