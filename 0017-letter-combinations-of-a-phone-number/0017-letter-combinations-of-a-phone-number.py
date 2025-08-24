class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='':
            return []

        ans = []
        h = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        def backtracking(digits, comb):
            if digits == '':
               ans.append(comb)
            else:
                for i in h[digits[0]]:
                    backtracking(digits[1:], comb+i)
        backtracking(digits, "")
        return ans
            