class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0

        for arr in grid:
            for i in arr:
                if i < 0:
                    cnt += 1

        return cnt