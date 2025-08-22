class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])

        end = float('-inf')
        cnt = 0

        for i, j in points:
            if end < i:
                end = j
                cnt += 1

        return cnt