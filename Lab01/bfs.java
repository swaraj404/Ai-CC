import java.util.*;

public class bfs {

    private int vertices;
    private LinkedList<Integer> adjList[];

    // Constructor
    bfs(int v) {
        vertices = v;
        adjList = new LinkedList[v];

        for (int i = 0; i < v; i++) {
            adjList[i] = new LinkedList<>();
        }
    }

    // Add edge (Undirected)
    void addEdge(int v, int w) {
        adjList[v].add(w);
        adjList[w].add(v);
    }

    // BFS Method
    void BFS(int start) {
        boolean visited[] = new boolean[vertices];//array to keep track of visited vertices
        Queue<Integer> queue = new LinkedList<>();//queue to process vertices in BFS order

        visited[start] = true;
        queue.add(start);

        System.out.print("BFS Traversal: ");

        //while queue is not empty, remove the front vertex and print it
        while (!queue.isEmpty()) { 
            int v = queue.poll();
            System.out.print(v + " ");

            for (int neighbor : adjList[v]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }
    }

    public static void main(String args[]) {

        bfs g = new bfs(9);

        // g.addEdge(0, 1);
        // g.addEdge(0, 2);
        // g.addEdge(1, 3);
        // g.addEdge(2, 4);
        // g.addEdge(3, 5);
        // g.addEdge(3, 6);
        // g.addEdge(4, 7);
        // g.addEdge(4, 8);

        g.addEdge(1, 3);
        g.addEdge(1, 5);
        g.addEdge(3, 7);
        g.addEdge(3, 8);
        g.addEdge(5, 6);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(2, 4);        

        g.BFS(0);
    }
}
