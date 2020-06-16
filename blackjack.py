import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return ("{} of {}".format(self.rank, self.suit))

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                instatiate_card = Card(suit, rank)
                self.deck.append(instatiate_card)
    def __str__(self):
        deck_cont = ''
        for card in self.deck:
            deck_cont += '\n' + card.__str__()
        return 'The deck has: ' + deck_cont

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_one_card = self.deck.pop()
        return deal_one_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        self.cards.append(card)
        
        
    def ace_adjust(self):
        while c in self.cards == 'Ace':
            if self.value > 11:
                for card,value in values.items():
                    if card == 'Ace':
                        values[value] == 1
                        self.value += 1
            else:
                for card, value in value.items():
                    if card == 'Ace':
                        try:
                            choice = int(input("Do you want the Ace to be 1 or 11?"))
                            if choice == 1:
                                values[value] == 1
                                self.value += values[card.rank]
                            elif choice == 11:
                                values[value] == 11
                                self.value += 11
                            else:
                                print("Choose 1 or 11")
                                continue
                        
                        except ValueError:
                            print("please type in a number!")
            break 
        else:
            self.value += vales[card.rank]
                    
                          
                    
                                
                
            

    def __str__(self):
        hand_cont = ''
        for c in self.cards:
            hand_cont += '\n' + str(c) 
        return 'Your hand has (value: {}):'.format(self.value) + hand_cont 
        

test_deck = Deck()
test_deck.shuffle()
test_hand = Hand()
test_hand.add_card(test_deck.deal())
test_hand.ace_adjust()
print(test_hand)
test_hand.add_card(test_deck.deal())
test_hand.adjust()
print(test_hand)
