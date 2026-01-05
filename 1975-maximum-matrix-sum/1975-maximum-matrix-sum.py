class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cnt = 0
        minN = float('inf')

        total = 0

        for arr in matrix:
            for i in arr:
                print(abs(i), minN)
                
                minN = min(minN, abs(i))
                
                if i < 0:
                    cnt += 1
                total += abs(i)

        if cnt % 2 == 1:
            total -= minN*2

        return total