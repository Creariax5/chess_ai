import time
from tqdm import tqdm
from customThread import CustomThread
from train_no_graph import play
from neural import init, mutate, mutate_v2
from os_my_dir import write_net, read_net

nb_ai = 1
percentage = 1

for gen in range(10000):
    th_list = []
    th_mutate = []

    last_gen_best = read_net()
    # th_list[0] = CustomThread(target=play, args=([last_gen_best, 0],))

    # take last_gen_best and pass it to mutate
    for ijk in tqdm(range(nb_ai)):
        th_mutate.append(CustomThread(target=mutate_v2, args=(last_gen_best, percentage,)))
    for ijk in tqdm(range(nb_ai)):
        th_mutate[ijk].start()
        time.sleep(0.15)
    # take network given by mutate and pass it to play
    for ijk in tqdm(range(nb_ai)):
        mut = th_mutate[ijk].join()
        my_network = [mut, 0]
        th_list.append(CustomThread(target=play, args=(my_network,)))
        time.sleep(0)
        print(ijk)
    for rep in tqdm(range(int(nb_ai))):
        th_list[rep].start()
        time.sleep(0)

    # find best network of this generation and save it
    best = 0
    best_score = -1000
    net = []
    for i in range(nb_ai):
        net = th_list[i].join()
        n = net[0]
        sc = net[1]
        if sc > best_score:
            best_score = sc
            best = n
    if sc > 4:
        write_net(n, "net_of_win")
    # print(best_score)

    print("")
    print("                               °\ /°")
    print("                              -(@ @)-")
    print("┌──────────────────────────oOO──(_)──OOo──────────────────────────┐")
    print("|                                                                 |")
    print("|                          gen :", gen, "                              |")
    print("|                    last best :", best_score, "                              |")
    print("|                                                                 |")
    print("└─────────────────────────────────────────────────────────────────┘")
    time.sleep(1)
    # write_net(best, "net3")
