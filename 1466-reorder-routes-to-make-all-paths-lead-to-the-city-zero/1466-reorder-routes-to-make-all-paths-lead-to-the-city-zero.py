class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        s = set()
        graph = [[] for _ in range(n)]

        for a, b in connections:
            s.add((a,b))
            graph[a].append(b)
            graph[b].append(a)


        stack = [0]
        visit = {0}
        cnt = 0

        while stack:
            curr = stack.pop()

            for i in graph[curr]:
                if i not in visit:
                    visit.add(i)
                    stack.append(i)

                    if (curr,i) in s:
                        cnt+=1
        
        return cnt