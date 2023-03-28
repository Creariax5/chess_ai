import time
from tqdm import tqdm
from train_no_graph import play
from neural import init, mutate, mutate_v2
from os_my_dir import write_net, read_net

nb_ai = 2
percentage = 0.2

for gen in range(10000):
    th_mutate = []

    last_gen_best = read_net()
    # th_list[0] = CustomThread(target=play, args=([last_gen_best, 0],))

    # take last_gen_best and pass it to mutate
    for ijk in tqdm(range(nb_ai)):
        th_mutate.append(mutate(last_gen_best, percentage))
    for ijk in tqdm(range(nb_ai)):
        time.sleep(0.15)
    # take network given by mutate and pass it to play
    start = time.time()

    th = play(th_mutate[0], th_mutate[1])

    end = time.time()
    elapsed = end - start
    print(f'Temps d\'exécution : {elapsed}s')

    # find best network of this generation and save it
    w, b, win = th

    if win == 1:
        write_net(w, "net3")
    if win == 2:
        write_net(b, "net3")

    time.sleep(1)

    print("")
    print("                               °\ /°")
    print("                              -(@ @)-")
    print("┌──────────────────────────oOO──(_)──OOo──────────────────────────┐")
    print("|                                                                 |")
    print("|                          gen :", gen, "                          ")
    print("|                    last best :", win, "                          ")
    print("|                                                                 |")
    print("└─────────────────────────────────────────────────────────────────┘")
