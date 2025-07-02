class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowHash = []
        colHash = []
        cnt = 0

        for i in range(len(grid)):
            rowHash.append(grid[i])
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            colHash.append(temp)
        
        for i in rowHash:
            for j in colHash:
                if i == j:
                    cnt += 1
        
        return cnt