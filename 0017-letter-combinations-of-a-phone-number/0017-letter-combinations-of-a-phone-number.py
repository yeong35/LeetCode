class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtracking(digits, temp):
            if len(digits) == 0:
                result.append(temp)
                return
            else:
                for i in d[digits[0]]:
                    backtracking(digits[1:], temp+i)
        if digits == "":
            return []


        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        result = []
        backtracking(digits, "")

        return result