import time

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

th_list = []
th_mutate = []

th_list.append(0)
for i in range(nb_ai - 1):
    th_list.append(0)
    th_mutate.append(0)

for gen in range(100):
    last_gen_best = read_net()
    th_list[0] = CustomThread(target=play, args=([last_gen_best, 0],))

    for ijk in range(nb_ai - 1):
        th_mutate[ijk] = CustomThread(target=mutate, args=(last_gen_best, percentage,))
    for ijk in range(nb_ai - 1):
        th_mutate[ijk].start()
    for ijk in range(nb_ai - 1):
        mut = th_mutate[ijk].join()
        my_network = [mut, 0]
        th_list[ijk + 1] = CustomThread(target=play, args=(my_network,))
        print(ijk + 1)

    for rep in range(int(nb_ai)):
        th_list[rep].start()

    best = 0
    best_score = 0
    net = []
    for i in range(nb_ai):
        net = th_list[i].join()
        print(net[0][0][0], "from thread")
        print(net[1], "from thread")
        if net[1] >= best_score:
            best_score = net[1]
            best = net[0]
    print(best_score)

    time.sleep(3)
    write_net(best, "net3")
