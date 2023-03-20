import copy
import time
from train_no_graph import play
from neural import init, mutate
from os_my_dir import write_net, read_net


nb_ai = 20
percentage = 0.5


for gen in range(100):
    th_list = []
    th_mutate = []

    last_gen_best = read_net()
    # th_list[0] = CustomThread(target=play, args=([last_gen_best, 0],))

    # take last_gen_best and pass it to mutate
    for ijk in range(nb_ai):
        th_mutate.append(copy.deepcopy(mutate(last_gen_best, percentage,)))

    # take network given by mutate and pass it to play
    for ijk in range(nb_ai):
        mut = th_mutate[ijk]
        my_network = copy.deepcopy([mut, 0])
        th_list.append(copy.deepcopy(play(my_network)))
        print(ijk)

    print("                               °\ /°")
    print("                              -(@ @)-")
    print("┌──────────────────────────oOO──(_)──OOo──────────────────────────┐")
    print("|                                                                 |")
    print("|                          Wait a second                          |")
    print("|                                                                 |")
    print("└─────────────────────────────────────────────────────────────────┘")

    # find best network of this generation and save it
    best = 0
    best_score = -1000
    net = []
    for i in range(nb_ai):
        net = th_list[i]
        n = net[0]
        sc = net[1]
        print(n[0][0], "from thread")
        print(sc, "from thread")
        if sc > best_score:
            best_score = sc
            best = n
            print("yes")
    print(best_score)

    time.sleep(1)
    write_net(best, "net3")
