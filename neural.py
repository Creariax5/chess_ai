import random
import time

import numpy as np
from os_my_dir import write_net, read_net


def init(ent, dep, out):

    w_input_table = np.random.uniform(-1, 1, ent * dep).tolist()
    w_table = []
    w_output_table = np.random.uniform(-1, 1, out * dep).tolist()

    b_table = []
    b_output_table = np.random.uniform(-1, 1, out).tolist()

    f_table = []
    output_table = np.zeros(out).tolist()

    for i in range(dep):
        w_table.append(np.random.uniform(-1, 1, dep * dep).tolist())

    for i in range(dep):
        b_table.append(np.random.uniform(-1, 1, dep).tolist())

    for i in range(dep):
        f_table.append(np.zeros(dep).tolist())

    seize = [ent, dep, out]

    network = [w_input_table, w_table, w_output_table, b_table, b_output_table, f_table, output_table, seize]

    # write_net(network)

    return network


def forward_propagation(input_table, network):
    def sig(x):
        return 1 / (1 + np.exp(-x))

    # input to deep
    u = 0

    for i in range(network[7][1]):
        tmp = 0
        for j in range(network[7][0]):
            tmp += input_table[j] * network[0][u]
            u += 1
        tmp += network[3][0][i]
        network[5][0][i] = sig(tmp)

    # deep
    for i in range(network[7][1] - 1):
        u = 0
        for j in range(network[7][1]):
            tmp = 0
            for k in range(network[7][1]):
                tmp += network[5][i][j] * network[1][i + 1][u]
                u += 1
            tmp += network[3][i + 1][j]
            network[5][i + 1][j] = sig(tmp)

    # deep to output
    u = 0
    for i in range(network[7][2]):
        tmp = 0
        for j in range(network[7][1]):
            tmp += network[5][network[7][1] - 1][i] * network[2][u]
            u += 1
        tmp += network[4][i]
        network[6][i] = sig(tmp)

    output_table = network[6]

    return output_table


def mutate(network, p):
    ent, dep, out = network[7][0], network[7][1], network[7][2]
    o = 0

    # w_input_table
    for i in range(ent * dep):
        rnd = random.uniform(-p, p)
        if -1 < network[0][i] + rnd < 1:
            network[0][i] = network[0][i] + rnd
            o += 1

    # w_table
    for i in range(dep):
        for j in range(dep * dep):
            rnd = random.uniform(-p, p)
            if -1 < network[1][i][j] + rnd < 1:
                network[1][i][j] = network[1][i][j] + rnd
                o += 1

    # w_output_table
    for i in range(out * dep):
        rnd = random.uniform(-p, p)
        if -1 < network[2][i] + rnd < 1:
            network[2][i] = network[2][i] + rnd
            o += 1

    # b_table
    for i in range(dep):
        for j in range(dep):
            rnd = random.uniform(-p, p)
            if -1 < network[3][i][j] + rnd < 1:
                network[3][i][j] = network[3][i][j] + rnd
                o += 1

    # b_output_table
    for i in range(out):
        rnd = random.uniform(-p, p)
        if -1 < network[4][i] + rnd < 1:
            network[4][i] = network[4][i] + rnd
            o += 1
    # print(o, " modifs")
    print("______________________test 42 ", network[0][0], " test 42______________________\n")
    time.sleep(1)

    return network


def select(dat, net):
    rep = forward_propagation(dat, net)
    return rep
