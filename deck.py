"""
Deck of cards, use classes for deck, the suits, and the cards. Want to be able to shuffle the deck, and then pull a card from the top of the deck.
"""
# import libraries
import random, time
# Define classes

# make the Suit class (subclass of Deck)
class Suit:
    def __init__(self, typeSuit, color):
        # give attributes of type, color, cards = 13
        self.__names__ = [
            'King',
            'Queen',
            'Jack',
            'Ten',
            'Nine',
            'Eight',
            'Seven',
            'Six',
            'Five',
            'Four',
            'Three',
            'Two',
            'Ace'
        ]
        self.__suitType__ = typeSuit
        self.__suitColor__ = color

    # give actions of generate cards
    def makeCards(self):
        # Will make the Card object and return it
        for name in self.__names__:
            card = Card(name,self.__suitType__,self.__suitColor__)
            # testing
            yield card

# make the Deck class
class Deck:
    def __init__(self, 
                 size = 52, 
                 suits = 4, 
                 types = ['Clubs','Spades','Hearts','Diamonds']):
        # give attributes of size = 52, suits = 4, type of suit 
        self.__deckSize__ = size
        self.__numSuits__ = suits
        self.__suitTypes__ = types
        self.__deck__ = []

    # give actions of shuffle, draw, generate cards
    def makeCardDeck(self):
        # make the suits
        for suit in self.__suitTypes__:
            # print(suit)
            # Assign based on color
            if suit in ['Clubs','Spades']:
                tempObject = Suit(suit,'black')
                # self.__suitHolding__.append(Suit(suit,'black'))
                # for suit in deck.__suitHolding__: print(suit.__suitType__, suit.__suitColor__)
            else:
                tempObject = Suit(suit,'red')
                # self.__suitHolding__.append(Suit(suit, 'red'))
            
            # Create the cards
            self.__deck__.extend(list(tempObject.makeCards()))
        # print(self.__deck__)
    
    def printDeck(self):
        # go through and print each deck, waiting a short bit in between each printing
        for card in self.__deck__:
            print(card.showCard())
            time.sleep(0.1)

    def shuffleDeck(self):
        # shuffle the deck
        random.shuffle(self.__deck__)
    
    def pullCard(self):
        # Pulls card from top of deck
        return self.__deck__.pop(0)



# make the Card class (subclass of Suit)
class Card(Suit):
    def __init__(self, name, typeSuit, color):
        super().__init__(typeSuit, color)
        # give attributes of suit, name(or rank)
        self.__cardName__ = name
    
    def showCard(self):
        return f"{self.__cardName__} of {self.__suitType__}"
# 
def invalAction():
    print("Please enter a valid entry.")

def main():
    deck = Deck()
    deck.makeCardDeck()
    deck.shuffleDeck()

    while True:
        print("""
        What action would you like to do?
        1) Pull a card
        2) Print the deck
        3) Shuffle deck
        4) Triple shuffle
        5) Quit
        """)
        try:
            userAction = int(input())

            if userAction not in [1,2,3,4,5]:
                invalAction()
        except ValueError:
            invalAction()
    
        match userAction:
            case 1:
                card = deck.pullCard()
                print(card.showCard())
            case 2:
                deck.printDeck()
            case 3:
                deck.shuffleDeck()
            case 4:
                for i in range(3):
                    deck.shuffleDeck()
            case 5:
                break

if __name__ == "__main__":
    main()