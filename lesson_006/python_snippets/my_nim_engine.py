from random import randint



_holder = []

def put_stoned():
    global _holder
    for i in range(5):
        _holder.append(randint(1, 20))

def take_from_bunch(position, quantity):
    if 1 <= position < len(_holder)+1:
        _holder[position-1]-=quantity

def get_bunches():
    return _holder


def is_gameover():
    return sum(_holder)==0
