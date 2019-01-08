import math


def senPos(sentences):
    th = 0.2
    minv = th * len(sentences)
    maxv = th * 2 * len(sentences)
    pos = []
    for i in range(len(sentences)):
        if i == 0 or i == len((sentences)):
            pos.append(0)
        else:
            t = math.cos((i - minv) * ((1 / maxv) - minv))
            pos.append(t)

    return pos
