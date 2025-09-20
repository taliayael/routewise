# RouteWise

RouteWise — CLI and visual shortest-path planner (Dijkstra / A*)

## מה זה
כלי CLI שמקבל גרף (JSON) ומחשב מסלול מינימום בין נקודות. אפשר להריץ Dijkstra או A* ולהפיק תמונת הדמיה של המסלול.

## התקנה (מהירה)
```bash
git clone https://github.com/YOUR_USERNAME/routewise.git
cd routewise
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Project Definition

**Project Name:** RouteWise

**Description:**
RouteWise is a Python-based tool for finding the optimal route between points using graph algorithms.
The project is designed to showcase algorithmic problem-solving (Dijkstra’s shortest path) and simple data visualization.

**Goals:**
- Allow users to define points (nodes) and connections (edges with weights, e.g., distance or time).
- Implement Dijkstra’s algorithm to compute the shortest path between two points.
- Output the result as:
  - Text (list of nodes in the path + total distance).
  - A visual graph highlighting the path (using NetworkX + Matplotlib).

**Future Extensions (optional):**
- Support importing graph data from external files (CSV/JSON).
- Add A* algorithm for comparison with Dijkstra.
- Create a simple GUI or web interface for route planning.

