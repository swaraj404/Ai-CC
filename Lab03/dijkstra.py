import sys
def dijkstra(graph, n, src):
    dist = [sys.maxsize] * n
    visited = [False] * n
    dist[src] = 0
    for _ in range(n):
        # Find minimum distance vertex
        min_dist = sys.maxsize
        u = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = -1
        visited[u] = True
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                if dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]
    print("\nVertex \t Distance from Source")
    for i in range(n):
        print(f"{i} \t {dist[i]}")
# Main
n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
src = int(input("Enter source vertex: "))
dijkstra(graph, n, src)
