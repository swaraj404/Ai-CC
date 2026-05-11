import java.util.*;

public class dfs {

    private int vertices;
    private LinkedList<Integer> adjList[];

    // Constructor
    dfs(int v) {
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

    // DFS Method
    void DFS(int start) {
        boolean visited[] = new boolean[vertices];
        System.out.print("DFS Traversal: ");
        DFSUtil(start, visited);
    }

    void DFSUtil(int v, boolean visited[]) {
        visited[v] = true; // Mark current node as visited
        System.out.print(v + " ");// Print current node

        // Loop through all neighbors and recursively visit unvisited neighbors
        for (int neighbor : adjList[v]) {
            if (!visited[neighbor]) {
                DFSUtil(neighbor, visited);// Recursively visit neighbor
            }
        }
    }

    public static void main(String args[]) {

        dfs g = new dfs(7);

        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 3);
        g.addEdge(2, 4);
        g.addEdge(3, 5);
        g.addEdge(4, 6);

        g.DFS(0);
    }
}
