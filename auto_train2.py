from threading import Thread
from neural import init, mutate
from os_my_dir import write_net, read_net
from train import play


class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


nb_ai = 20
percentage = 0.5

my_network_list = []
for i in range(nb_ai):
    my_network_list.append(0)

last_gen_best = read_net()

for i in range(nb_ai):
    net = [mutate(last_gen_best, percentage), 0]
    # my_network_list[i] = play(net)
    my_network_list[i] = CustomThread(target=play, args=(net,))

for i in range(nb_ai):
    my_network_list[i].start()

for i in range(nb_ai):
    print(my_network_list[i].join())

print(my_network_list[0])

# best of gen
best = 0
best_score = 0

'''for i in range(nb_ai):
    print(my_network_list[i][1])
    if my_network_list[i][1] >= best_score:
        best_score = my_network_list[i][1]
        best = i
print(best_score, best)

write_net(my_network_list[best][0], "net3")'''
