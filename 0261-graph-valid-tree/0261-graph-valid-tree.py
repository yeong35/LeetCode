class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
             
            if x < y:
                parent[y] = x
            else:
                parent[x] = y
        
        parent = [i for i in range(n)]

        for a, b in edges:
            if find(a) == find(b):
                return False
            union(a,b)
        
        for i in range(n):
            find(i)
        print(parent)
        
        return len(set(parent)) == 1