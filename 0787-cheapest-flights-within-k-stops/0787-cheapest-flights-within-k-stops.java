class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        List<List<int[]>> graph = new ArrayList<>();

        // initialize
        for (int i = 0; i < n; i++)
            graph.add(new ArrayList<>());

        // put the path
        for (int flight[] : flights) {
            graph.get(flight[0]).add(new int[] {flight[1], flight[2]});
        }

        Queue<int[]> que = new LinkedList<>();

        if (src == dst)
            return 0;
        
        int[] visited = new int[n];

        Arrays.fill(visited, Integer.MAX_VALUE);
        visited[src] = 0;
        
        // put the start node for traversing
        que.offer(new int[] {src, 0});

        int depth = 0;

        while (!que.isEmpty() && depth < k + 1) {
            int size = que.size();
            for (int i = 0; i < size; i++) {

                int current[] = que.poll();

                for (int next[] : graph.get(current[0])) {
                    if (current[1] + next[1] < visited[next[0]]) {
                        visited[next[0]] = current[1] + next[1];
                        que.offer(new int[] {next[0], visited[next[0]]});
                    }
                }
            }
            depth++;
        }
        return visited[dst] == Integer.MAX_VALUE ? -1 : visited[dst];
    }
}