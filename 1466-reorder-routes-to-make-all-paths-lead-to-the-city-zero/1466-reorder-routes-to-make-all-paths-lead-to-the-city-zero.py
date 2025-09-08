class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = set()
        undirected = [[] for _ in range(n)]
        visit = {0}
        cnt = 0

        for i, j in connections:
            graph.add((i,j))
            undirected[i].append(j)
            undirected[j].append(i)

        stack = [0]

        while stack:
            curr = stack.pop()

            for neighbor in undirected[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    stack.append(neighbor)
                    if (curr, neighbor) in graph:
                        cnt+=1
            

        return cnt