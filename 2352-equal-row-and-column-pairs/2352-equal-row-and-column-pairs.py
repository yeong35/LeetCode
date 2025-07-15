class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        h = defaultdict(int)
        n = len(grid)
        cnt = 0

        for i in grid:
            h[tuple(i)] += 1
        
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(grid[j][i])
            
            cnt += h[tuple(temp)]
        
        return cnt
        