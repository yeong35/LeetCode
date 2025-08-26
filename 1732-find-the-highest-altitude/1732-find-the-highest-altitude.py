class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        highest = 0
        curr = 0

        for i in gain:
            curr += i

            highest = max(highest, curr)

        return highest