import os
import ast


def create_directory(nb):
    directory = "gen" + nb
    parent_dir = "D:/devProjects/PycharmProjects/little23/my_gen"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    return path


def write_net(net, name):
    print("writing")
    net = str(net)
    with open('my_gen/' + name + '.txt', 'w') as file:
        for l in net:
            file.write(l)


def read_net():
    print("reading")
    with open('my_gen/net5.0test.txt', 'r') as f:
        net = f.read()
        net = ast.literal_eval(net)
    return net
