package Lab02;

import java.util.*;

class PuzzleSolver {
    static final int N = 3;

    static int[] row = { 0, 0, -1, 1 };
    static int[] col = { -1, 1, 0, 0 };

    static class PuzzleState {
        int[][] board;
        int x, y;
        int depth;
        int hash;

        // its the constructor fot the puzzle state which takes the current board
        // configuration, the position of the blank tile (x, y), and the depth of the
        // state in the search tree. It also calculates a hash value for the board
        // configuration to facilitate quick comparisons and storage in a HashSet.
        PuzzleState(int[][] b, int i, int j, int d) {
            board = new int[N][N];
            for (int k = 0; k < N; k++)
                board[k] = Arrays.copyOf(b[k], N);
            x = i;
            y = j;
            depth = d;
            hash = Arrays.deepHashCode(board);
        }

        // The equals method is overridden to compare two PuzzleState objects based on
        // their hash values, which represent the board configuration. This allows us to
        // easily check if a state has been visited before when we store states in a
        // HashSet.
        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;
            if (obj == null || getClass() != obj.getClass())
                return false;
            PuzzleState that = (PuzzleState) obj;
            return hash == that.hash;
        }

        // The hashCode method is overridden to return the precomputed hash value of the board configuration. This ensures that the hash code is consistent with the equals method, allowing us to use PuzzleState objects effectively in hash-based collections like HashSet.
        @Override
        public int hashCode() {
            return hash;
        }
    }

    
    // This method checks if the current board configuration matches the goal state. It uses Arrays.deepEquals to compare the two 2D arrays representing the board configurations. If they are equal, it means we have reached the goal state.
    static boolean isGoalState(int[][] board, int[][] goal) {

        return Arrays.deepEquals(board, goal);
    }

    static boolean isValid(int x, int y) {
        return (x >= 0 && x < N && y >= 0 && y < N);
    }

    static void printBoard(int[][] board) {
        for (int[] row : board) {
            for (int num : row)
                System.out.print(num + " ");
            System.out.println();
        }
        System.out.println("--------");
    }

    static void solvePuzzleBFS(int[][] start, int x, int y) {
        Queue<PuzzleState> queue = new LinkedList<>();
        Set<PuzzleState> visited = new HashSet<>();

        queue.add(new PuzzleState(start, x, y, 0));
        visited.add(new PuzzleState(start, x, y, 0));

        while (!queue.isEmpty()) {
            PuzzleState curr = queue.poll();

            System.out.println("Depth: " + curr.depth);
            printBoard(curr.board);

            if (isGoalState(curr.board, new int[][] { { 1, 2, 3 }, { 4, 5, 0 }, { 6, 7, 8 } })) {
                System.out.println("Goal state reached at depth " + curr.depth);
                return;
            }

            for (int i = 0; i < 4; i++) {
                int newX = curr.x + row[i];
                int newY = curr.y + col[i];

                if (isValid(newX, newY)) {
                    int[][] newBoard = new int[N][N];
                    for (int j = 0; j < N; j++)
                        newBoard[j] = Arrays.copyOf(curr.board[j], N);

                    int temp = newBoard[curr.x][curr.y];
                    newBoard[curr.x][curr.y] = newBoard[newX][newY];
                    newBoard[newX][newY] = temp;

                    PuzzleState newState = new PuzzleState(newBoard, newX, newY, curr.depth + 1);

                    if (!visited.contains(newState)) {
                        visited.add(newState);
                        queue.add(newState);
                    }
                }
            }
        }

        System.out.println("No solution found (Unsolvable Puzzle)");
    }

    public static void main(String[] args) {
        int[][] start = { { 1, 2, 3 }, { 4, 0, 5 }, { 6, 7, 8 } };
        int[][] goal = { { 1, 2, 3 }, { 4, 5, 0 }, { 6, 7, 8 } };
        int x = 1, y = 1;

        System.out.println("Initial State: ");
        printBoard(start);

        solvePuzzleBFS(start, x, y);
    }
}