import math
import heapq

def euclidean(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

def shortest_path(graph, src, dst):
    # implement A* using euclidean heuristic via graph.coords
    ...
