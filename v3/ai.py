import copy
import time

from neural import select
import random


def select_phase(dat, net):
    score = select(dat, net)
    return copy.deepcopy(score)


def move_phase(dat, net, b):
    x = 0
    y = 0

    xa = 0
    ya = 0

    dat.append(1)
    dat.append(b)
    rep = select(dat, net)

    for i in range(8):
        if x < rep[i]:
            x = rep[i]
            xa = i

    for i in range(8):
        if y < rep[i + 8]:
            y = rep[i]
            ya = i

    x = xa
    y = ya

    return x, y


def select_rnd():
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    return x, y


def move_rnd():
    x = random.randint(0, 7)
    y = random.randint(0, 7)
    return x, y
