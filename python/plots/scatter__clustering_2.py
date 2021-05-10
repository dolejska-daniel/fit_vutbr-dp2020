import re

import numpy as np
import matplotlib.pyplot as plt
from other.point_cluster import Point, clusterize


def run():
    with open("../data/captcha_2.txt", "r") as f:
        c = "".join(f.readlines())

    tuples = re.findall(r"x=(\d+),y=(\d+)", c)
    xy = list(map(lambda tuple: list(map(lambda coord: int(coord), tuple)), tuples))

    # xy = np.random.random_sample((10, 2))
    # xy *= (200, 50)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    img = plt.imread("../data/captcha_2.png")
    ax.imshow(img)

    clusters = clusterize(xy, distance_limit=20)
    x, y, cx, cy, cluster = [], [], [], [], []
    cluster_mapping = {"x": 0}
    for c in clusters:
        if c in cluster_mapping:
            id = cluster_mapping[c]

        else:
            id = cluster_mapping[c] = max(cluster_mapping.values()) + 1

        for p in c.points:
            x.append(p.x)
            y.append(p.y)
            cluster.append(id)

        c = c.center()
        cx.append(c[0])
        cy.append(c[1])

    ax.set_xlim(0, 200)
    ax.set_xlabel('x')

    ax.set_ylabel('y')
    ax.set_ylim(50, 0)

    plt.yticks(np.arange(0,  51, 25), visible=True, rotation="horizontal")
    plt.xticks(np.arange(0, 201, 25), visible=True, rotation="horizontal")

    scatter = ax.scatter(x, y, s=75, cmap="brg")
    plt.savefig("../../build/point_clustering_2_raw.pdf", bbox_inches="tight")

    scatter = ax.scatter(x, y, c=cluster, s=75, cmap="brg")
    for x, y in zip(cx, cy):
        ax.scatter(x, y, s=50, c="red", marker="x")

    # ax.legend(labels, bbox_to_anchor=(.95, .8))  # .remove()
    plt.savefig("../../build/point_clustering_2.pdf", bbox_inches="tight")


if __name__ == '__main__':
    run()
    plt.tight_layout(pad=0)
    plt.show()
