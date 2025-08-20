class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtracking(k, n, start, temp):
            if k==0:
                if n==0:
                    ans.append(list(temp))
            else:
                for i in range(start, 10):
                    temp.append(i)
                    backtracking(k-1, n-i, i+1, temp)
                    temp.pop()

        backtracking(k,n,1,[])
        return ans