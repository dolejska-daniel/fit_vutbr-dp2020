import itertools
import functools
import math
import operator


class Cluster:

    def __init__(self):
        self.points = set()

    def __hash__(self) -> int:
        return functools.reduce(operator.xor, map(hash, self.points))

    def __len__(self) -> int:
        return len(self.points)

    def __repr__(self) -> str:
        return "Cluster(points=%s)" % (self.points,)

    def join(self, point):
        self.points.add(point)
        return self

    def leave(self, point):
        self.points.remove(point)

    def center(self) -> tuple[float, float]:
        return sum([pt.x for pt in self.points]) / len(self.points), sum([pt.y for pt in self.points]) / len(
            self.points)

    def distance(self, point) -> float:
        x, y = self.center()
        return math.sqrt((x - point.x) ** 2 + (y - point.y) ** 2)


class Point:
    cluster: Cluster
    cluster_dist = float("inf")

    def __init__(self, x: float, y: float, cluster: Cluster = None):
        self.x = x
        self.y = y

        cluster = cluster or Cluster()
        self.cluster = cluster.join(self)

    def __repr__(self) -> str:
        return "Point(x=%s, y=%s)" % (self.x, self.y)

    def distance(self, point) -> float:
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def try_clusterize(self, point, distance_limit: float):
        distance = self.distance(point)
        if distance > distance_limit or distance > self.cluster_dist:
            return

        self.cluster.leave(self)
        self.cluster = point.cluster.join(self)
        self.cluster_dist = point.cluster.distance(self)


def clusterize(points: list[tuple[float, float]], distance_limit: float = 30) -> set[Cluster]:
    points: list[Point] = list(map(lambda pt: Point(*pt, cluster=Cluster()), points))
    for pt1, pt2 in itertools.permutations(points, 2):
        pt1.try_clusterize(pt2, distance_limit)

    return set([point.cluster for point in points])


def largest_cluster(points: list[tuple[float, float]], distance_limit: float = 30) -> Cluster:
    clusters = clusterize(points, distance_limit)
    return sorted(clusters, key=lambda c: len(c), reverse=True)[0]
