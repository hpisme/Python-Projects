
"""This is my version / trying without the professor's help."""
"""Need to remember to use docstrings in my functions"""
"""I think I could have simplified some of this code! It's functional but not efficient."""

print('Welcome to Blackjack! \n')


def blackjack():
    import random

    deck_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []

    continue_input = input('Would you like to play another game? Type \'y\' to play or \'n\' to quit. ')
    if continue_input == 'y':
        for x in range(1, 3):
            user_cards.append(random.choice(deck_list))
            computer_cards.append(random.choice(deck_list))
        print('Your cards: ', user_cards, ', current score: ', sum(user_cards))
        print('Computer\'s first card: ', computer_cards[0])

        while sum(computer_cards) < 16:
            computer_cards.append(random.choice(deck_list))

        another_card = input('Type \'y\' to get another card or \'n\' to pass. ')
        while another_card == 'y':
            if sum(user_cards) < 21:
                user_cards.append(random.choice(deck_list))
                if sum(user_cards) > 21:
                    break
                else:
                    print('Your cards: ', user_cards, 'current score: ', sum(user_cards))
                    another_card = input('Type \'y\' to get another card or \'n\' to pass. ')
                    if another_card == 'y':
                        continue
                    else:
                        break

        if sum(user_cards) == 21:
            print('Your final hand: ', user_cards, 'final score: ', sum(user_cards))
            print('Computer\'s final hand: ', computer_cards, 'final score: ', sum(computer_cards))
            print('You win! Blackjack!')

        elif sum(computer_cards) == 21:
            print('Your final hand: ', user_cards, 'final score: ', sum(user_cards))
            print('Computer\'s final hand: ', computer_cards, 'final score: ', sum(computer_cards))
            print('Computer wins.')

        elif sum(user_cards) > 21 and sum(computer_cards) > 21:
            print('Your final hand: ', user_cards, 'final score: ', sum(user_cards))
            print('Computer\'s final hand: ', computer_cards, 'final score: ', sum(computer_cards))
            print('Draw.')

        elif sum(user_cards) == sum(computer_cards):
            print('Your final hand: ', user_cards, 'final score: ', sum(user_cards))
            print('Computer\'s final hand: ', computer_cards, 'final score: ', sum(computer_cards))
            print('Draw.')

        elif sum(computer_cards) > 21:
            print('Your final hand: ', user_cards, 'final score: ', sum(user_cards))
            print('Computer\'s final hand: ', computer_cards, 'final score: ', sum(computer_cards))
            print('The computer went over. You win!')

        elif sum(user_cards) > 21:
            print('Your final hand: ', user_cards, 'final score: ', sum(user_cards))
            print('Computer\'s final hand: ', computer_cards, 'final score: ', sum(computer_cards))
            print('You went over. You lose.')

        elif sum(user_cards) > sum(computer_cards):
            print('Your final hand: ', user_cards, 'final score: ', sum(user_cards))
            print('Computer\'s final hand: ', computer_cards, 'final score: ', sum(computer_cards))
            print('You win!')

        elif sum(computer_cards) > sum(user_cards):
            print('Your final hand: ', user_cards, 'final score: ', sum(user_cards))
            print('Computer\'s final hand: ', computer_cards, 'final score: ', sum(computer_cards))
            print('The computer wins.')

        blackjack()
    else:
        print("\nThanks for playing.")


blackjack()
