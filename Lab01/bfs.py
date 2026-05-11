from collections import deque


def bfs_recursive(graph, queue, visited):
    if not queue:
        return 


    vertex = queue.popleft()
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    
    bfs_recursive(graph, queue, visited)



def bfs(graph, start):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    print("BFS Traversal:")
    bfs_recursive(graph, queue, visited)



graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


bfs(graph, 'B')