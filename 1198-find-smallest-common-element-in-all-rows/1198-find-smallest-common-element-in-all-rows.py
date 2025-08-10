class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        result = set(mat[0])

        for i in mat:
            temp = set(i)

            result = result.intersection(temp)

        if len(result) > 0:
            result = list(result)
            result.sort()
            return result[0]
        return -1