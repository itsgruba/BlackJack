import random

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
card_keys = list(cards.keys())

def get_card_value(total_value, cards_of):
    if "A" in cards_of and total_value > 21:
        return total_value - 10
    return total_value

def game_start_cards_distribution(dealer, player):
    """Make list of cards, the first."""
    if dealer == [] and player == []:
        dealer.extend(random.sample(card_keys, 2))
        player.extend(random.sample(card_keys, 2))
    return dealer, player


def start():
    """Start game."""
    start_game = input("To start game enter START: ")
    while start_game.lower() != "start":
        print("Wrong input!")
        start_game = input("To start game enter START: ")
    else:
        return "Game starts in 3, 2, 1..."


def value(dealer_cards, player_cards):
    """Firstly see the cards."""
    value_player = sum(cards[card] for card in player_cards)
    value_dealer = sum(cards[card] for card in dealer_cards)
    return f'Dealer: {dealer_cards} => {value_dealer}, Player: {player_cards} => {value_player}'


def ask_add_or_stay():
    """Player has choice to stay or not."""
    while True:
        choice = input("Would you like to add or stay?: ").lower()
        if choice == "add" or choice == "stay":
            return choice
        else:
            print("Wrong input!")


def player_add_count_phrase(player_cards):
    """Prog to add for player, and returns the players amount."""
    player_cards.extend(random.sample(card_keys, 1))
    total_value = sum(cards[card] for card in player_cards)
    total_value_player = get_card_value(total_value, player_cards)
    return f'Player {player_cards} => {total_value_player}'


def count_dealer(dealer_cards):
    """Dealer start to play."""
    total_value_dealer_last = sum(cards[card] for card in dealer_cards)
    while total_value_dealer_last < 17:
        dealer_cards.extend(random.sample(card_keys, 1))
        total_value_dealer = sum(cards[card] for card in dealer_cards)
        total_value_dealer_last = get_card_value(total_value_dealer, dealer_cards)
    return total_value_dealer_last


def winner(dealer_point, player_points):
    """Returns the winner."""
    if player_points < dealer_point <= 21:
        return "Dealer win!"
    elif player_points == dealer_point:
        return "Draft"
    else:
        return "Player win!"


def final_step(dealer_cards, player_cards):
    """The final prog. Controls if player put stay or asked for more"""
    next_step = ask_add_or_stay()
    if next_step == "stay":
        print("Start to count dealer card")
        dealer_points = count_dealer(dealer_cards)
        total_value_player = sum(cards[card] for card in player_cards)
        print(winner(dealer_points, total_value_player))
        return f'Dealer cards: {dealer_cards}'
    else:
        print(player_add_count_phrase(player_cards))
        total_value_player = sum(cards[card] for card in player_cards)
        total_value_player = get_card_value(total_value_player, player_cards)
        if total_value_player > 21:
            return f'Dealer win!\nPlayer went out of 21.'
        while True:
            more = input("Would you like more? (yes or no): ").lower()

            if more == "yes":
                print(player_add_count_phrase(player_cards))
                total_value_player = sum(cards[card] for card in player_cards)
                total_value_player = get_card_value(total_value_player, player_cards)
                if total_value_player > 21:
                    return f'Dealer win!\nPlayer went out of 21.'
            elif more == "no":
                print("Start to count dealer card")
                total_value_player = sum(cards[card] for card in player_cards)
                dealer_points = count_dealer(dealer_cards)
                print(winner(dealer_points, total_value_player))
                return f'Dealer cards: {dealer_cards}'
            else:
                print("Wrong input! Please enter 'yes' or 'no'.")


def the_whole_game(dealer_cards, player_cards):
    print(start())
    dealer_cards, player_cards = game_start_cards_distribution(dealer_cards, player_cards)
    print(value(dealer_cards, player_cards))
    return final_step(dealer_cards, player_cards)

print(the_whole_game([], []))