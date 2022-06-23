import random


def dice_calculator(func):
    '''decorator for setting the values of the dice'''

    def wrapper():
        result = func()
        print('Dice stopped spinning')
        return result

    return wrapper


@dice_calculator
def dice_throw():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print('Computer: Dice #1: {} / Dice #2: {} / Sum: {}'.format(d1, d2, d1 + d2))
    return d1 + d2


def player_dice(func):
    '''Decorator that receives parameters'''

    def wrapper(func_to_do, ref_value):
        result = func(func_to_do, ref_value)
        print('Next Round:\n\n')
        return result

    return wrapper


@player_dice
def dice_cheat(func_to_do, ref_value):
    if func_to_do == 'lower':
        d1 = random.randint(1, ref_value)
        d2 = random.randint(1, ref_value)
        print('Your values: Dice #1: {} / Dice #2: {} / Sum: {}'.format(d1, d2, d1 + d2))
        return d1 + d2
    else:
        d1 = random.randint(ref_value, 6)
        d2 = random.randint(ref_value, 6)
        print('Your values: Dice #1: {} / Dice #2: {} / Sum: {}'.format(d1, d2, d1 + d2))
        return d1 + d2


def repeat(answer):
    '''decorator that recieves a parameter'''

    def decorator(func):
        def repeat_wrapper():
            choice = answer
            while choice == 'Y':
                choice = func()
            print('END GAME...')

        return repeat_wrapper

    return decorator


def function_recall(func):
    '''decorator that has the same name'''

    def wrapper():
        answer = func(5)
        return answer

    return wrapper


@repeat('Y')
@function_recall
def function_recall(n):
    player_score = 0
    computer_score = 0
    for i in range(n):
        computer_score = computer_score + dice_throw()
        player_score = player_score + dice_cheat(input(), int(input()))
    if player_score == computer_score:
        print('You won!\nComputer_score: {} / Player_score: {}\nTo play again press Y else press N'.format(
            computer_score, player_score))
    else:
        print('You lost.\nComputer_score: {} / Player_score: {}\nTo play again press Y else press N'.format(
            computer_score, player_score))
    return input()


function_recall()
