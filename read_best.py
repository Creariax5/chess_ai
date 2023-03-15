

def train_best(read):
    my_network_list[0] = [last_gen_best, 0]

    # mutate and train
    for ijk in range(nb_ai - 1):
        my_network = [mutate(last_gen_best, percentage), 0]
        my_network_list[ijk + 1] = my_network
        print(my_network_list[ijk + 1][0][0][0], "test 2")
        print(ijk + 1)
    print("__________________________")
    print(my_network_list[15][0][0][0], "test 3")
    print(my_network_list[5][0][0][0], "test 4")
    print("__________________________")

    for rep in range(int(nb_ai)):
        play(my_network_list[rep])

    # best of gen
    best = 0
    best_score = 0

    for i in range(nb_ai):
        print(my_network_list[i][1])
        if my_network_list[i][1] >= best_score:
            best_score = my_network_list[i][1]
            best = i
    print(best_score, best)

    write_net(my_network_list[best][0], "net3")
