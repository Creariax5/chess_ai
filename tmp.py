
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
