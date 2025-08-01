class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def backtracking(idx, arr, k, n):
            
            if k == 0 and n==0:
                result.append(list(arr))
            else:
                for i in range(idx, 10):
                    if n-i >= 0:
                        arr.append(i)
                        backtracking(i+1, arr, k-1, n-i)
                        arr.pop()
        
        backtracking(1, [], k, n)
        return result