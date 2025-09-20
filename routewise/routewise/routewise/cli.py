import argparse
import json
from .io import load_graph
from .dijkstra import shortest_path as dj

def main():
    parser = argparse.ArgumentParser(prog="routewise")
    sub = parser.add_subparsers(dest="cmd")
    route = sub.add_parser("route")
    route.add_argument("--graph", required=True)
    route.add_argument("--src", required=True)
    route.add_argument("--dst", required=True)
    route.add_argument("--algo", choices=["dijkstra","astar"], default="dijkstra")
    args = parser.parse_args()
    g = load_graph(args.graph)
    if args.algo=="dijkstra":
        path,dist = dj(g, args.src, args.dst)
    else:
        # call astar
        path,dist = None, None
    print("Path:", path)
    print("Distance:", dist)

if __name__=="__main__":
    main()
