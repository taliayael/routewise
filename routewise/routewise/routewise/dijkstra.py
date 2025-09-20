import heapq
from typing import Dict, Tuple, List, Optional

def shortest_path(graph, src: str, dst: str):
    dist = {n: float('inf') for n in graph.adj}
    prev = {n: None for n in graph.adj}
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d,u = heapq.heappop(heap)
        if d>dist[u]:
            continue
        if u==dst:
            break
        for v,w in graph.adj.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))
    # build path
    if dist[dst]==float('inf'):
        return None, None
    path = []
    cur = dst
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    return list(reversed(path)), dist[dst]
