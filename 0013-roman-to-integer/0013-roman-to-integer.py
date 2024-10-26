class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        sum = 0
        biggest = s[-1]

        for i in reversed(s):
            if roman[biggest] > roman[i]:
                sum -= roman[i]
            else:
                biggest = i
                sum += roman[i]


            print(i, sum)

        return sum