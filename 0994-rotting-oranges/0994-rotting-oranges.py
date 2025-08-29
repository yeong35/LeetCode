class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        minute = 0
        que = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    que.append([i,j])
                    grid[i][j] = 0

        if fresh == 0:
            return minute

        while que:
            minute += 1
            k = len(que)

            for _ in range(k):
                x, y = que.pop(0)
                print(x,y)
                for i, j in move:
                    i += x
                    j += y

                    if 0<=i<m and 0<=j<n:
                        if grid[i][j] == 1:
                            fresh -= 1
                            grid[i][j] = 0
                            que.append([i,j])

                            if fresh == 0:
                                return minute

        return -1        
