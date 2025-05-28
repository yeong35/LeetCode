class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        result = 0

        for i in gain:
            curr += i
            result = max(result, curr)
        
        return result