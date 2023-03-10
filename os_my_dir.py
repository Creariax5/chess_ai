import os
import ast


def create_directory(nb):
    directory = "gen" + nb
    parent_dir = "D:/devProjects/PycharmProjects/little23/my_gen"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    return path


def write_net(net, name):
    net = str(net)
    with open('my_gen/' + name + '.txt', 'w') as file:
        for l in net:
            file.write(l)


def read_net():
    with open('my_gen/net3.txt', 'r') as f:
        net = f.read()
        net = ast.literal_eval(net)
    print("read")
    return net
