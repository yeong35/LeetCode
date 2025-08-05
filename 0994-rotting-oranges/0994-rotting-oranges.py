class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        sec = 0
        moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    q.append([i,j])

        if fresh==0:
            return 0

        while q:
            k = len(q)
            for _ in range(k):
                x, y = q.pop(0)

                for i, j in moves:
                    i += x
                    j += y

                    if 0 <= i < m and 0<= j < n:
                        if grid[i][j] == 1:
                            grid[i][j]=2
                            fresh -= 1
                            q.append([i,j])
                        
                        if fresh == 0:
                            return sec+1
            

            sec+=1
        return -1