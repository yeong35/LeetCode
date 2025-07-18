class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected = [[] for i in range(n)]
        directed = [[] for i in range(n)]
        visit = set()
        cnt = 0

        for a, b in connections:
            undirected[a].append(b)
            undirected[b].append(a)
            directed[a].append(b)

        stack = [0]
        visit.add(0)

        while stack:
            curr = stack.pop()

            for i in undirected[curr]:
                if i not in visit:
                    visit.add(i)
                    stack.append(i)

                    if i in directed[curr]:
                        cnt+=1
        
        return cnt