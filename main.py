"""Minimum Spanning Tree solver for a complete, undirected, weighted graph.

Reads an adjacency matrix from INPUT_FILENAME, computes the MST using
Kruskal's algorithm with a union-find (disjoint set) structure, prints the
total MST weight to stdout, and writes the MST as an adjacency matrix to
OUTPUT_FILENAME.
"""

import os

INPUT_FILENAME = "udg.dat"
OUTPUT_FILENAME = "mst.dat"


class DisjointSet:
    """Union-find structure with path compression and union by rank."""

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item):
        # Path compression: point directly to the root on the way back up.
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        # Union by rank: attach the shorter tree under the taller one.
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


def read_adjacency_matrix(path):
    """Reads a whitespace-separated adjacency matrix from a text file."""
    matrix = []
    with open(path, "r") as f:
        for line in f:
            if line.strip():
                matrix.append([int(x) for x in line.split()])
    return matrix


def write_adjacency_matrix(path, matrix):
    """Writes an adjacency matrix to a text file, space-separated per row."""
    with open(path, "w") as f:
        for row in matrix:
            f.write(" ".join(map(str, row)) + "\n")


def build_edge_list(matrix):
    """Builds the edge list (u, v, weight) for a complete undirected graph.

    The input graph is complete, so every distinct vertex pair (i, j) is a
    valid edge regardless of its weight value (including a weight of 0).
    """
    num_vertices = len(matrix)
    edges = []
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            edges.append((i, j, matrix[i][j]))
    return edges


def compute_mst(num_vertices, edges):
    """Computes the MST edges and total weight using Kruskal's algorithm."""
    disjoint_set = DisjointSet(num_vertices)
    mst_edges = []
    total_weight = 0

    for u, v, weight in sorted(edges, key=lambda edge: edge[2]):
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            mst_edges.append((u, v, weight))
            total_weight += weight

    return mst_edges, total_weight


def build_mst_matrix(num_vertices, mst_edges):
    """Converts a list of MST edges into a symmetric adjacency matrix."""
    mst_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v, weight in mst_edges:
        mst_matrix[u][v] = weight
        mst_matrix[v][u] = weight
    return mst_matrix


def solve_mst():
    if not os.path.exists(INPUT_FILENAME):
        print(f"Error: {INPUT_FILENAME} not found in the current directory.")
        return

    matrix = read_adjacency_matrix(INPUT_FILENAME)
    num_vertices = len(matrix)

    edges = build_edge_list(matrix)
    mst_edges, total_weight = compute_mst(num_vertices, edges)

    print(total_weight)

    mst_matrix = build_mst_matrix(num_vertices, mst_edges)
    write_adjacency_matrix(OUTPUT_FILENAME, mst_matrix)


if __name__ == "__main__":
    solve_mst()
