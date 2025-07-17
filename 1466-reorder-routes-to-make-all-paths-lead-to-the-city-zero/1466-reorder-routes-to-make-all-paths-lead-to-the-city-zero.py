class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected = [[] for i in range(n)]
        graph = [[] for i in range(n)]
        visited = [0] * n
        cnt = 0

        for a, b in connections:
            graph[a].append(b)
            undirected[a].append(b)
            undirected[b].append(a)

        stack = [0]
        visited[0] = 1

        while stack:
            curr = stack.pop()

            for i in undirected[curr]:
                if visited[i] == 0:
                    stack.append(i)
                    visited[i] = 1
                    if i in graph[curr]:
                        cnt += 1
        
        return  cnt
        