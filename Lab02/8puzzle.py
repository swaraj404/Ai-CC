from queue import PriorityQueue

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(state):
    distance = 0

    for i in range(3):
        for j in range(3):
            value = state[i][j]

            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3

                distance += abs(i - target_x) + abs(j - target_y)

    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

    raise ValueError("Blank tile not found in state")



def to_tuple(state):
    return tuple(tuple(row) for row in state)



def generate_neighbors(state):
    neighbors = []

    x, y = find_blank(state)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors



def a_star(start_state):
    pq = PriorityQueue()

    pq.put((heuristic(start_state), 0, start_state))

    visited = set()

    while not pq.empty():
        f, g, current = pq.get()

        print("Current State:")
        for row in current:
            print(row)
        print()

        
        if current == goal_state:
            print("Goal State Reached!")
            return

        visited.add(to_tuple(current))

        
        for neighbor in generate_neighbors(current):

            if to_tuple(neighbor) not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(neighbor)

                pq.put((new_f, new_g, neighbor))



start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]


a_star(start_state)