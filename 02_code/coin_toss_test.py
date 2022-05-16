from re import L
from numpy.random import seed, randint

seed(1)

def coin_toss():
    if randint(0, 2) == 1:
        return 'HEAD'
    else:
        return 'TAIL'

print(coin_toss())