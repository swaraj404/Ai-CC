package Lab02;

import java.util.*;

public class eightpuzzle {
    static class Node {
        Node parent;
        int[][] mat;
        int x, y;
        int cost;
        int level;

        // here we are creating a constructor for the node to take all the parameters
        // and assign them to that instance variables by this keyword.
        Node(int[][] mat, int x, int y, int cost, int level, Node parent) {
            this.mat = mat;
            for (int i = 0; i < 3; i++) {
                System.arraycopy(mat[i], 0, this.mat[i], 0, 3);
                this.x = x;
                this.y = y;
                this.cost = Integer.MAX_VALUE;
                this.level = level;
                this.parent = parent;
            }
        }
    }

    // here we print the matrix
    static void printMatrix(int[][] mat) {
        for (int[] row : mat) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    // here are the possible moves for the blank tile in the 8 puzzle, we can move
    // up, down, left or right. 1 represents moving down, 0 represents moving left,
    // -1 represents moving up and 0 represents moving right.
    static int[] row = { 1, 0, -1, 0 };
    static int[] col = { 0, -1, 0, 1 };


    //here i calculate the cost of the current state by comparing it withe the goal state.
    static int calculateCost(int[][] initial, int[][] goal) {
        int count = 0;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (initial[i][j] != 0 && initial[i][j] != goal[i][j])
                    count++;
        return count;
    }

    //here i check if the new position of blank tile is within the matrix or not.
    static boolean isSafe(int x, int y) {
        return (x >= 0 && x < 3 && y >= 0 && y < 3);
    }

    

}