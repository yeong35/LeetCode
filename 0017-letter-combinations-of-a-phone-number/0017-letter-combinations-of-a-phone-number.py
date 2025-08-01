class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=='':
            return []
        arr = [['a', 'b', 'c'], ['d','e','f'], ['g','h','i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        def backtracking(digits, arr, temp):
            if len(digits)==1:
                for c in arr[int(digits[0])-2]:
                    result.append(temp+c)
            else:
                for c in arr[int(digits[0])-2]:
                    backtracking(digits[1:], arr, temp+c)

        
        result = []
        backtracking(digits, arr, "")

        
        return result