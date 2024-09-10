'''
Data structure to implement deck of cards and shuffle and draw cards
'''



import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        #print("From class Card")
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        #This list has Card objects created with given rank, suit
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]
        #Shuffle the cards
        #random.shuffle(self.cards)
        #Knuth-Fisher-Yates shuffle algorithm
        self.shuffle()

    def draw(self):
        #idx = random.randint(0, len(self.cards) - 1) #This produced repeated idx, drawing same card, which is not possible
        #return self.cards[idx]
        return self.cards.pop()
       

    def __str__(self):
        return f"Deck with {len(self.cards)} cards remaining"
    
    def shuffle(self):
        # Implementing Fisher-Yates shuffle
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

# Example usage
deck = Deck()
print("Initial deck:")
print(deck)
print("\nDrawing cards:")
for _ in range(5):
    print(deck.draw())

