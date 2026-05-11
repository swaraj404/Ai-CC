def is_safe(board, row, col, n):     
    for i in range(row):
        if board[i][col] == 1:
            return False 
    i, j = row, col   
    while i >= 0 and j >= 0:         
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n:  
        if board[i][j] == 1:
            return False         
        i -= 1
        j += 1
    return True 

def solve(board, row, n):
    if row == n:
        print_solution(board, n)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n)
            board[row][col] = 0   # backtrack 
            
def print_solution(board, n):
    print("\nSolution:")
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print() 
n = int(input("Enter N: ")) 
board = [[0]*n for _ in range(n)] 
solve(board, 0, n) 
        