class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[1], [1,1]]

        if numRows < 3:
            return pascals[:numRows]
        
        for i in range(1, numRows-1):
            pascals.append([1])
            for j in range(len(pascals[i])-1):
                pascals[i+1].append(pascals[i][j]+pascals[i][j+1])
            pascals[i+1].append(1)

        return pascals