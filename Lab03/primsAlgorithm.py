import sys
def prims(graph, n):
    selected = [False] * n
    selected[0] = True
    print("Edge : Weight")
    for _ in range(n - 1):
        minimum = sys.maxsize
        x = y = 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and graph[i][j]:
                        if minimum > graph[i][j]:
                            minimum = graph[i][j]
                            x, y = i, j
        print(f"{x} - {y} : {graph[x][y]}")
        selected[y] = True
# Main
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
prims(graph, n)