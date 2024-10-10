"""
In-class project:
Deck of cards, use classes for deck, the suits, and the cards. Want to be able to shuffle the deck, and then pull a card from the top of the deck.
"""
# import libraries
import random, time

    # Define classes:
# make the Suit class
class Suit:
    def __init__(self, typeSuit):
        # Create a list of the card names
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

        # Assign the type of suit and color based on what's been given
        self.__suitType__ = typeSuit

        # Determine what the actual color will be
        if self.__suitType__ in ['Clubs','Spades']:
            self.__suitColor__ = 'black'
        else:
            self.__suitColor__ = 'red'

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
            tempObject = Suit(suit)
            
            # Create the cards
            # tempObject.makeCards() creates a generator OBJECT, which needs to be converted to a list for our use
            # .extend() is a list method that adds the ITEMS of our list to __deck__
            # NOTE: .append() will add the entire LIST as an ITEM
            self.__deck__.extend(list(tempObject.makeCards()))
        # print(self.__deck__)
    
    def printDeck(self):
        # go through and print each deck, waiting a short bit in between each printing
        for card in self.__deck__:
            print(card.showCard())
            time.sleep(0.2)

    def shuffleDeck(self):
        # shuffle the deck
        random.shuffle(self.__deck__)
    
    def pullCard(self):
        # Pulls card from top of deck and removes it from the deck
        return self.__deck__.pop(0)



# make the Card class (subclass of Suit)
class Card(Suit):
    def __init__(self, name, typeSuit, color):
        # give attributes of suit, name, and color
        self.__cardName__ = name
        self.__suitType__ = typeSuit
        self.__suitColor__ = color
    
    def showCard(self):
        # return a string of the full card name
        return f"{self.__cardName__} of {self.__suitType__}"
# 
def invalAction():
    """
    For when a user has entered an unaccaptable entry
    """
    print("Please enter a valid entry.")

def main():
    # Build and shuffle the deck
    deck = Deck()
    deck.makeCardDeck()
    deck.shuffleDeck()

    # Run the program until the user wants to quit
    while True:
        print("""
        What action would you like to do?
        1) Pull a card
        2) Print the deck
        3) Shuffle deck
        4) Triple shuffle
        5) Quit
        """)
        # 
        try:
            userAction = int(input())

            if userAction not in [1,2,3,4,5]:
                invalAction()

        except ValueError:
            invalAction()

        except:
            # catch all for userAction entry
            print("Another error has occurred during action entry.")
    
        # Match the appropriate action
        match userAction:
            case 1:
                card = deck.pullCard()
                print(card.showCard())
                # print(card.__suitColor__) # testing purposes
            case 2:
                deck.printDeck()
            case 3:
                deck.shuffleDeck()
            case 4:
                for i in range(3):
                    deck.shuffleDeck()
            case 5:
                break

# Only run the main() function if this file is not imported
if __name__ == "__main__":
    main()