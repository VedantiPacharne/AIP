from collections import deque

class Graph:
    def __init__(self):
        self.graph = [[0 for _ in range(10)] for _ in range(10)]

    def add_edge(self, row, column):
        self.graph[row][column] = 1
        self.graph[column][row] = 1

    def check_edge(self, row, column):
        return self.graph[row][column] == 1

    def display(self, n):
        for i in range(n):
            for j in range(n):
                print(self.graph[i][j], end="")
            print()

def dfs(graph_obj, traversal, size):
    x = int(input("Enter the starting node: "))
    visited = [False] * size
    stack = []
    a = 0

    stack.append(x)
    visited[x] = True

    while stack:
        top = stack.pop()
        traversal[a] = top
        a += 1

        for j in range(size - 1, -1, -1):  # Reverse to match C++ stack order
            if graph_obj.check_edge(top, j) and not visited[j]:
                stack.append(j)
                visited[j] = True

def bfs(graph_obj, traversal, size):
    x = int(input("Enter the starting node: "))
    visited = [False] * size
    queue = deque()
    a = 0

    queue.append(x)
    visited[x] = True

    while queue:
        top = queue.popleft()
        traversal[a] = top
        a += 1

        for j in range(size):
            if graph_obj.check_edge(top, j) and not visited[j]:
                queue.append(j)
                visited[j] = True

def main():
    G = Graph()
    n = int(input("Enter the number of vertices: "))

    while True:
        row = int(input("Enter the row number: "))
        column = int(input("Enter the column number: "))
        G.add_edge(row, column)
        ans = input("Do you want to add another edge? (y/n): ")
        if ans.lower() != 'y':
            break

    G.display(n)
    traversal = [-1] * n

    choice = int(input("Enter 1 for DFS, 2 for BFS: "))
    if choice == 1:
        dfs(G, traversal, n)
    elif choice == 2:
        bfs(G, traversal, n)

    x = int(input("Enter the node to search: "))
    found = False
    for i in range(n):
        print(traversal[i], end=" ")
        if traversal[i] == x:
            print("Node found")
            found = True
            break
    if not found:
        print("\nThe node doesn't exist")

if __name__ == "__main__":
    main()
