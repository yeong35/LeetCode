class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if parent[x]==x:
                return parent[x]
            else:
                return find(parent[x])

        def union(x,y):
            x = find(x)
            y = find(y)

            if x < y:
                parent[y] = x
            else:
                parent[x] = y
        
        n = len(isConnected)
        parent = [i for i in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    union(i, j)
        
        for i in range(n):
            parent[i] = find(i)

        return len(set(parent))
