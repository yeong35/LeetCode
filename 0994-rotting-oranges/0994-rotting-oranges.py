class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        fresh = 0
        sec = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh +=1

        if fresh==0:
            return sec


        while queue:
            k = len(queue)

            for _ in range(k):
                x, y = queue.popleft()

                for i, j in moves:
                    i += x
                    j += y

                    if 0<=i<n and 0<=j<m and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j]=2
                        queue.append((i,j))
                    
                    if fresh==0:
                        return sec+1
            
            sec += 1




        return -1