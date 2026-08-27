class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        def union(a, b):
            a = find(a)
            b = find(b)

            if a<b:
                parent[b] = a
            else:
                parent[a] = b
    

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    union(i,j)
        
        for i in range(n):
            find(i)
        return len(set(parent))