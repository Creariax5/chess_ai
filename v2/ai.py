import time

from neural import select
import random


def select_phase(dat, net):
    x = 0
    y = 0
    xa = 0
    ya = 0

    x_next = 0
    y_next = 0
    xa_next = 0
    ya_next = 0

    rep = select(dat, net)

    for i in range(8):
        if x < rep[i]:
            x = rep[i]
            xa = i

    for i in range(8):
        if y < rep[i + 8]:
            y = rep[i + 8]
            ya = i

    for i in range(8):
        if x_next < rep[i + 8*2]:
            x_next = rep[i + 8*2]
            xa_next = i

    for i in range(8):
        if y_next < rep[i + 8*3]:
            y_next = rep[i + 8*3]
            ya_next = i

    x = xa
    y = ya
    x_next = xa_next
    y_next = ya_next

    u = str(y) + str(y_next)
    print(u)

    return x, y, x_next, y_next


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
