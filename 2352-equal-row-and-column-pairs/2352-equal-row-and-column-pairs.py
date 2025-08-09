class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        s = defaultdict(int)
        cnt = 0
        for i in grid:
            s[tuple(i)] += 1

        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(grid[j][i])

            cnt+=s[tuple(temp)]
        

        return cnt