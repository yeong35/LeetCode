class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
            
        
        def union(x, y):
            x = find(x)
            y = find(y)
            
            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        cycle = 0

        parent = [i for i in range(n)]

        for x,y in edges:
            if find(x) == find(y):
                cycle+=1
            
            union(x,y)

        return cycle == 0 and len(set(parent))==1