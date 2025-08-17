class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])

        cnt = 0
        end = float('-inf')

        for i,j in intervals:
            if i >= end:
                end = j
            else:
                cnt+=1

        return cnt
