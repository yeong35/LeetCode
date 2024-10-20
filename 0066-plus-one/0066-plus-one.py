class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(str(i) for i in digits)
        num = int(num)+1

        num = str(num)

        result = []

        for i in num:
            print(int(i))
            result.append(int(i))

        return result