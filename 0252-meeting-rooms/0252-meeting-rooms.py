class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[1])

        start = 0
        end = 0

        for i, j in intervals:
            if start <= i < end or start <= j < end:
                return False

            end = max(end, max(i, j))

        return True