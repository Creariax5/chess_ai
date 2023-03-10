import random


def create(x1, x2):
    b1w1 = random.uniform(0, 1)
    b2w1 = random.uniform(0, 1)
    b1w2 = random.uniform(0, 1)
    b2w2 = random.uniform(0, 1)
    b1w3 = random.uniform(0, 1)
    b2w3 = random.uniform(0, 1)

    bw1 = random.randint(0, 10)
    bw2 = random.randint(0, 10)
    bw3 = random.randint(0, 10)

    fw1 = x1 * b1w1 + x2 * b2w1 + bw1
    fw2 = x1 * b1w2 + x2 * b2w2 + bw2
    fw3 = x1 * b1w3 + x2 * b2w3 + bw3

    b1o1 = random.uniform(0, 1)
    b2o1 = random.uniform(0, 1)
    b3o1 = random.uniform(0, 1)

    bo1 = random.randint(0, 10)

    fo1 = fw1 * b1o1 + fw2 * b2o1 + fw3 * b3o1 + bo1

    s1 = fo1

    print(s1)
    return s1


max = 0

for i in range(10):
    for j in range(10):
        c = create(i, j)
        if c > max:
            max = c
    print("_____")

print(max)
