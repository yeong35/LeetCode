class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        s = {(i,j) for i, j in connections}
        visit = {0}
        undirected = [[] for _ in range(n)]
        
        for i, j in connections:
            undirected[i].append(j)
            undirected[j].append(i)

        stack = [0]
        cnt = 0
        while stack:
            curr = stack.pop()

            for neighbor in undirected[curr]:
                if neighbor not in visit:
                    if (curr, neighbor) in s:
                        cnt += 1
                    stack.append(neighbor)
                    visit.add(neighbor)

            
        return cnt