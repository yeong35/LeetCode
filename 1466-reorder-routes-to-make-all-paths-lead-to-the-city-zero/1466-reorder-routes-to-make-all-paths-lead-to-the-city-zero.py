class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        edges = {(i,j) for i,j in connections}

        for i, j in connections:
            graph[i].append(j)
            graph[j].append(i)

        cnt = 0
        stack = [0]
        visit = {0}

        while stack:
            curr = stack.pop()

            for i in graph[curr]:
                if i not in visit:
                    stack.append(i)
                    visit.add(i)

                    if (curr, i) in edges:
                        cnt += 1

        return cnt