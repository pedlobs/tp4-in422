# Code Élève
from heapq import *

# exemple basique
exemple1 = {
    "a": [("f", 14), ("c", 9), ("b", 7)],
    "b": [("c", 10), ("d", 15)],
    "c": [("f", 2), ("d", 11)],
    "d": [("e", 6)],
    "e": [],
    "f": [("e", 9)],
}

INFINI = float("inf")


def longueur_chemin(gv, c):
    distance = 0

    for u, v in zip(c, c[1:]):

        found_path = 0

        if u in gv:
            for neighbour, weight in gv[u]:
                if neighbour == v:
                    distance += weight
                    found_path = 1
                    break
            if not found_path:
                return INFINI

    return distance


def dijkstra(s, gv):
    pass


def dijkstra_optimise(s, gv):
    pass
