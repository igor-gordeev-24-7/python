import random

HEADS = "heads"
TAILS = "tails"
COUNT_VALUES = [HEADS, TAILS]


def flip_coin():
    return random.choice(COUNT_VALUES)


def play_martingale(*, starting_funds: int, min_bet: int, max_bet: int) -> int :
    steps_to_loose = 0
    current_funds = starting_funds
    current_bet = min_bet

    while current_funds > 0:
        print("=======")
        steps_to_loose += 1
        current_funds -= current_bet
        print(f"{current_funds=}, {current_bet=}")
        flip_coin_value = flip_coin()
        if flip_coin_value == HEADS:
            win = current_bet * 2
            current_bet += win
            current_bet = min_bet
        else:
            current_bet *=2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds

    return steps_to_loose


print(play_martingale(min_bet=1, max_bet=100, starting_funds=100))