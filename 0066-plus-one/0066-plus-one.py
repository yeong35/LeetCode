class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        length = len(digits)

        for i in range(len(digits)):
            digits[length-i-1] += plus

            plus = digits[length-i-1]//10
            digits[length-i-1] %= 10

        if plus != 0:
            digits = [plus]+digits
        
        return digits