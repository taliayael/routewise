from typing import Dict, Tuple, List

class Graph:
    def __init__(self, directed: bool = False):
        self.adj: Dict[str, List[Tuple[str, float]]] = {}
        self.coords: Dict[str, Tuple[float, float]] = {}
        self.directed = directed

    def add_node(self, name: str, x: float = 0.0, y: float = 0.0):
        self.coords[name] = (x, y)
        self.adj.setdefault(name, [])

    def add_edge(self, u: str, v: str, w: float = 1.0):
        self.adj.setdefault(u, []).append((v, w))
        if not self.directed:
            self.adj.setdefault(v, []).append((u, w))
