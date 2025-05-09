import heapq
from collections import defaultdict

# Graph class using adjacency list
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Undirected

    def prim_mst(self):
        visited = [False] * self.V
        min_heap = [(0, 0)]  # (weight, vertex)
        prev = [None] * self.V
        mst_weight = 0
        mst_edges = []

        while min_heap:
            weight, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            mst_weight += weight

            if prev[u] is not None:
                mst_edges.append((prev[u], u, weight))

            for v, w in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
                    prev[v] = u

        return mst_edges, mst_weight


# --- Accept user input ---
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

g = Graph(V)

print("Enter each edge in the format: u v weight")
for i in range(E):
    u, v, w = map(int, input(f"Edge {i+1}: ").split())
    g.add_edge(u, v, w)

# Compute MST
mst, total_weight = g.prim_mst()

# Display the MST
print("\nEdges in the Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} - {v} with weight {weight}")
print(f"Total weight of MST: {total_weight}")
