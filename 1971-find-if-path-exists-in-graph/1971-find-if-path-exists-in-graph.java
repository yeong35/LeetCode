class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
        for(int i = 0; i<n; i++)
            graph.add(new ArrayList<Integer>());
        
        int u, v;
        for(int i = 0; i<edges.length; i++){
            u = edges[i][0];
            v = edges[i][1];

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        Queue<Integer> que = new LinkedList<>();
        int[] visited = new int[n];
        visited[source] = 1;

        int vertex;

        que.add(source);
        visited[source] = 1;

        for(int i = 0; i<graph.get(source).size(); i++){
            que.add(graph.get(source).get(i));
        }

        while(!que.isEmpty()){
            vertex = que.poll();
            if(vertex == destination)
                return true;

            for(int i = 0; i<graph.get(vertex).size(); i++){
                if(visited[graph.get(vertex).get(i)]!=1){
                    que.add(graph.get(vertex).get(i));
                    visited[graph.get(vertex).get(i)] = 1;
                }
            }
        }


        return false;
    }
}