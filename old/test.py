import random


def mutate(r, p):
    p = random.uniform(0, 1)
    rep = r + p
    return rep


nb = 20
percentage = 0.5
read = 1.5
network_list = []

for i in range(nb):
    network_list.append(0)

my_network = [read, 0]
network_list[0] = my_network

for i in range(nb - 1):
    my_network = [mutate(read, percentage), 0]
    network_list[i] = my_network

print(network_list[0])
print(network_list[19])
