class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            if parent[x]!=x:
                return find(parent[x])
            else:
                return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        parent = [i for i in range(n)]

        for i, j in edges:
            union(i, j)
        print(parent)
        if find(source) == find(destination):
            return True
        return False
