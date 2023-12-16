import random
from Deck import Deck
from Chips import Chips
from Hand import Hand

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
deck_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True

def take_bet(chips):
    while True:

        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry please provide an integer')
        else:
            if chips.bet > chips.total:
                print(f'Sorry, you do not have enough chips! You have: {chips.total}')
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print('Player Stand Dealers turn')
            playing = False
        else:
            print('Sorry, I do not understand that input. Please enter h or s ')
            continue
        break

def show_some(player, dealer):
    # show only one of the dealers cards
    print("\nDealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    # Show all 2 cards of the players hand
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    # show all the dealers cards
    # print("\nDealer's Hand: ", *dealer.cards, sep='\n')
    print("\nDealer's Hand: ")
    for card in dealer.cards:
        print(card)

    # calculate and display value (J+K == 20)
    print(f"Value of Dealer's hand is: {dealer.value}")

    # show all the players cards
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is: {player.value}")

def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()
    
def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()
    
def push(player, dealer):
    print("Dealer and player tie! PUSH")


while True:
    # Print an opening statement

    print("WELCOME TO BLACKJACK")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_hand, dealer_hand)


    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break
    
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print(f'\nPlayer total chips are at: {player_chips.total}')

    new_game = input("Play again? y/n ")

    if new_game[0] == 'y':
        playing = True
    else:
        print('Thank you for playing.')

        break


