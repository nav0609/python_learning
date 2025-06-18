import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

game_on = True

# Creating the card
class Card:

    # Intantiating the card attributes
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    # Printing the card
    def __str__(self):
        return self.rank + ' of ' + self.suit
    

# Creating the Deck
class Deck:
    
    # Instantiating each card
    def __init__(self):
        self.deck = []  # Initially the deck is empty

        # Creating the deck using the Card class from earlier
        for suit in suits:
            for rank in ranks:

                created_card = Card(suit,rank)
                self.deck.append(created_card)

    def __str__(self):
        deck_composition=''
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return 'The deck has :' + deck_composition
    
    # Shuffling the cards
    def shuffle(self):
        random.shuffle(self.deck)

    # Dealing the Card
    def deal_card(self):
        single_card = self.deck.pop()
        return single_card
    

# Creating the player's hand
class Hand:

    def __init__(self):
        self.cards = []     # The hand is initially empty
        self.value = 0      # The value of the hand is initially zero
        self.aces = 0       # Taking the number of aces to be zero initially

    # Adding cards to the hand
    def add_card(self,card):

        # The card appended is from the deck created previously using deal_card()
        self.cards.append(card)

        # Adding the value of the card appended
        self.value += values[card.rank]

        # Checking for and adding aces
        if card.rank == 'Ace':
            self.aces +=1

    def adjust_for_ace(self):
        
        # Switching the ace value from 11 to 1 if the value of the hand > 21
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

# Creating the money stuff of the player
class Chips:

    def __init__(self):
        self.total = 100       # Some random choosen starting value
        self.bet = 0           # Initially the bet is zero
    
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# Creating a function for taking bets
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How much would you like to bet :"))
        except ValueError:
            print("Sorry, that's an incorrect input! Please enter an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry you can't bet more than your balance. Your balance is : {chips.total}")
            else:
                break

# Writing a function for hitting the player
def hit(deck,hand):
    
    hand.add_card(deck.deal_card())
    hand.adjust_for_ace()

# Writing a function for the choice of hitting or standing
def hit_or_stand(deck,hand):
    global game_on  # Used for while loop later on

    while True:
        choice = input(print("Enter h if you would like to be hit or enter s if you would like to stand : "))

        if choice[0].lower() == 'h':
            print("The Player hits!")
            hit(deck,hand)
        elif choice[0].lower() =='s':
            print("The Player stands!")
            game_on = False
        else:
            print("Invalid input. Enter the characters h or s")
            continue
        break

def show_some(player,dealer):

    # Show only one of the dealer's cards
    print("\nThe Dealer's hand :")
    print("First card is hidden!")
    print(dealer.cards[1])

    # Show all (2 cards) of player's cards
    print("\nThe Player's hand :")
    for card in player.cards:
        print(card)


def show_all(player,dealer):

    # Show all of dealer's cards
    print("\nThe Dealer's hand :")
    for card in dealer.cards:
        print(card)
    
    # Show the value of the dealer's hand
    print(f"\nThe value of Dealer's hand is : {dealer.value}")
    
    # Show all of player's cards
    print("\nThe Player's hand :")
    for card in player.cards:
        print(card)

    # Show the value of the player's hand
    print(f"\nThe value of Player's hand is : {player.value}")

# Writing the functions for different scenarios of the game
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


# GAME LOGIC
while True:

    print("Welcome to Blackjack!")

    # Creating an instance of the deck and shuffling and dealing the deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    

    # Setting up player's chips
    player_chips = Chips()
    
    # Asking if the player would like to bet
    take_bet(player_chips)

    # Showing the cards while keeping showing only one of dealers cards
    show_some(player_hand,dealer_hand)

    while game_on:

        # Asking for hit or stand
        hit_or_stand(deck,player_hand)

        # Showing the cards while showing only one of the dealers cards
        show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21 breaking out of the loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)

            break

    # If the player hasn't busted then playing the dealer's hand it reaches the value of 17

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        # Showing all cards 
        show_all(player_hand,dealer_hand)

        # Different scenarios of the game

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        elif player_hand.value == dealer_hand.value:
            push(player_hand,dealer_hand)
        
    # Showing the player's total chips
    print(f"\nThe chips of the player are : {player_chips.total}")

    # Asking to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break        