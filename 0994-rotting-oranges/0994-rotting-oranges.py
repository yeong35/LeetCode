class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    grid[i][j] = 0
                    queue.append((i,j))
        
        sec = 0
        if fresh ==0:
            return sec
        
        while queue:
            k = len(queue)
            for _ in range(k):
                x, y = queue.pop(0)

                for i, j in move:
                    i += x
                    j += y

                    if (0<=i<m and 0<=j<n) and grid[i][j] != 0:
                        if grid[i][j] == 1:
                            fresh -= 1
                            if fresh == 0:
                                return sec+1
                        grid[i][j] = 0
                        queue.append((i,j))
            
            sec+=1


        return -1