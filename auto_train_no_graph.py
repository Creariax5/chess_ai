from thread import Thread
from train_no_graph import play
from neural import init, mutate
from os_my_dir import write_net, read_net


class CustomThread(Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


nb_ai = 20
percentage = 0.5

my_network_list = []
for i in range(nb_ai):
    my_network_list.append(0)

for gen in range(100):
    last_gen_best = read_net()

    my_network_list[0] = [last_gen_best, 0]

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
        my_network_list[rep][1] = play(my_network_list[rep])

    best = 0
    best_score = 0

    for i in range(nb_ai):
        print(my_network_list[i][1])
        if my_network_list[i][1] >= best_score:
            best_score = my_network_list[i][1]
            best = i
    print(best_score, best)

    write_net(my_network_list[best][0], "net3")
