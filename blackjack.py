import random

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 1}
card_keys = list(cards.keys())
dealer_cards = []
player_cards = []

def game_start(dealer, player):
    if dealer == [] and player == []:
        dealer_cards.extend(random.sample(card_keys, 2))
        player_cards.extend(random.sample(card_keys, 2))
    return dealer_cards, player_cards

def player_add_count(player):
    player_cards.extend(random.sample(card_keys, 1))
    total_value = sum(cards[card] for card in player_cards)
    return f'Player {player_cards} => {total_value}'

def ask_add_or_stay():
    while True:
        choice = input("Would you like to add or stay?: ").lower()
        if choice == "add" or choice == "stay":
            return choice
        else:
            print("Wrong input!")

def count_dealer(dealer):
    total_value_dealer_last = sum(cards[card] for card in dealer)
    while total_value_dealer_last < 17:
        dealer_cards.extend(random.sample(card_keys, 1))
        total_value_dealer_last = sum(cards[card] for card in dealer_cards)
    return total_value_dealer_last

def winner(dealer_point, player_points):
    if player_points > 21:
        return "Dealer win! Player went out of 21"
    elif player_points < dealer_point <= 21:
        return "Dealer win!"
    elif player_points == dealer_point:
        return "Draft"
    else:
        return "Player win!"


start_game = input("To start game enter START: ")

while start_game.lower() != "start":
    print("Wrong input!")
    start_game = input("To start game enter START: ")
else:
    print("Game starts in 3, 2, 1...")
    dealer_cards, player_cards = game_start(dealer_cards,player_cards)

total_value_player = sum(cards[card] for card in player_cards)
total_value_dealer = sum(cards[card] for card in dealer_cards)
print(f'Dealer: {dealer_cards} => {total_value_dealer}, Player: {player_cards} => {total_value_player}')

next_step = ask_add_or_stay()

if next_step == "stay":
    print("Start to count dealer card")
    dealer_points = count_dealer(dealer_cards)
    total_value_player = sum(cards[card] for card in player_cards)
    print(winner(dealer_points, total_value_player))
    print(f'Dealer cards: {dealer_cards}')
else:
    print(player_add_count(player_cards))
    while True:
        more = input("Would you like more? (yes or no): ").lower()

        if more == "yes":
            print(player_add_count(player_cards))
        elif more == "no":
            print("Start to count dealer card")
            total_value_player = sum(cards[card] for card in player_cards)
            dealer_points = count_dealer(dealer_cards)
            print(winner(dealer_points, total_value_player))
            print(f'Dealer cards: {dealer_cards}')
            break
        else:
            print("Wrong input! Please enter 'yes' or 'no'.")
