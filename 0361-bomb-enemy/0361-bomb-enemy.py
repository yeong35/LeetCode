class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        checker = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        result = 0
        count = 0

        row = len(grid)
        column = len(grid[0])

        for i in range(row):
            for j in range(column):
                if grid[i][j] != "0":
                    continue
                
                count = 0
                for x, y in checker:
                    x += i
                    y += j

                    if x >= 0 and x < row and y >= 0 and y < column and grid[x][y] == "E":
                        count += 1
                
                result = max(result, count)

        return result