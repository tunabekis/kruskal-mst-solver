# Minimum Spanning Tree (MST) Solver

A Python implementation that computes the Minimum Spanning Tree of a
complete, undirected, weighted graph using **Kruskal's algorithm** with a
**Union-Find (Disjoint Set)** structure (path compression + union by rank).

## How it works

1. Reads the graph as an adjacency matrix from `udg.dat` in the current
   working directory. Since the input graph is complete, every off-diagonal
   entry `matrix[i][j]` is treated as a real edge weight between vertex `i`
   and vertex `j` (a weight of `0` is a valid edge weight, not "no edge").
2. Builds the edge list and sorts it by weight.
3. Runs Kruskal's algorithm: edges are added to the MST one by one (lowest
   weight first) as long as they don't form a cycle, which is checked
   efficiently with a Union-Find structure.
4. Prints the total MST weight to standard output.
5. Writes the resulting MST back out as a symmetric adjacency matrix to
   `mst.dat` in the current working directory.

## Technologies

- Python 3 (standard library only, no external dependencies)

## Project structure

```
hw1/
├── main.py     # MST solver (entry point)
├── udg.dat     # Sample input: adjacency matrix of the graph
├── mst.dat     # Output: adjacency matrix of the computed MST
└── README.md
```

## How to run

Make sure `udg.dat` is present in the current working directory, then run:

```bash
python main.py
```

The program prints the minimum spanning weight to standard output and
(re)writes `mst.dat` with the MST's adjacency matrix.

## Input/output format

- **Input (`udg.dat`)**: an `N x N` whitespace-separated adjacency matrix of
  integer edge weights for a complete undirected graph with `N` vertices.
- **Output (`mst.dat`)**: an `N x N` whitespace-separated adjacency matrix
  where `matrix[i][j]` is the weight of the MST edge between vertices `i`
  and `j`, or `0` if no MST edge connects them directly.
