import random

# Constants
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(CARDS)

def calculate_scores(cards):
    """Calculates the score of the given cards."""
    score = sum(cards)
    # Check for blackjack (Ace + 10)
    if len(cards) == 2 and score == 21:
        return 0  # Blackjack
    # Adjust for Aces
    while 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)  # Recalculate score after adjustment
    return score

def compare(user_score, computer_score):
    """Compares the scores of the user and the computer."""
    if user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0:
        return "You won with a Blackjack!"
    elif computer_score == 0:
        return "You lost! The computer has Blackjack."
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "The computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_blackjack():
    """Main function to play the Blackjack game."""
    print("Welcome to Blackjack!")
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Start the game
play_blackjack()
