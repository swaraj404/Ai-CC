def solve(row): 
    if row == n:
        print_solution()
        return
    for col in range(n):
        if cols[col] == 0 and d1[row - col + n] == 0 and d2[row + col] == 0:
            board[row][col] = 1
            cols[col] = d1[row - col + n] = d2[row + col] = 1
            solve(row + 1)
            board[row][col] = 0
            cols[col] = d1[row - col + n] = d2[row + col] = 0 

def print_solution():
    print("\nSolution:")     
    for row in board:
        print(*row) 
n = int(input("Enter N: ")) 
board = [[0]*n for _ in range(n)] 
cols = [0]*n 
d1 = [0]*(2*n) 
d2 = [0]*(2*n) 
solve(0) 