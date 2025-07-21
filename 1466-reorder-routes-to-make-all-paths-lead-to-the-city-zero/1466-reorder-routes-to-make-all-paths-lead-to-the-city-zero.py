class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected = [[] for i in range(n)]
        directed = set(tuple(i) for i in connections)
        cnt = 0

        stack = [0]
        visit = set()
        visit.add(0)

        for a, b in connections:
            undirected[a].append(b)
            undirected[b].append(a)

        while stack:
            curr = stack.pop()

            for i in undirected[curr]:
                if i not in visit:
                    stack.append(i)
                    visit.add(i)

                    if (curr, i) in directed:
                        cnt+=1
        
            
        return cnt