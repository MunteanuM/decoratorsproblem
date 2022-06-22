import random


def dice_calculator(func):
    '''decorator for setting the values of the dice'''

    def wrapper():
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print('Computer: Dice #1: {} / Dice #2: {} / Sum: {}'.format(d1, d2, d1 + d2))

        func()
        return d1 + d2

    return wrapper


def values_cheater(func, x):
    score = func(x)
    return score


def lower_value(x):
    d1 = random.randint(1, x)
    d2 = random.randint(1, x)
    print('Dice #1: {} / Dice #2: {} / Sum: {}'.format(d1, d2, d1 + d2))
    return d2 + d1


def higher_value(x):
    d1 = random.randint(x, 6)
    d2 = random.randint(x, 6)
    print('Dice #1: {} / Dice #2: {} / Sum: {}'.format(d1, d2, d1 + d2))
    return d2 + d1


def game(ans):
    computer_score = 0
    player_score = 0
    while ans == 'Y':
        for i in range(5):
            @dice_calculator
            def dice_throw():
                print('Dice stopped spinning. Your turn')

            computer_score = computer_score + dice_throw()
            print(
                'To get a little help with your luck choose if you want'
                ' to throw a lower value than x or higher value than x...')
            if input() == 'lower':
                player_score = player_score + values_cheater(lower_value, int(input()))
            else:
                player_score = player_score + values_cheater(higher_value, int(input()))
        if player_score != computer_score:
            print("You lost! to try again press Y else press N\ncomputer score: {} / player score: {}".format(
                computer_score, player_score))
        else:
            print("You won! to play again press Y else press N")
        ans = input()
    print("GAME END...")


game('Y')
