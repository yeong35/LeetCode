class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(x):
            if parent[x]!=x:
                return find(parent[x])
            else:
                return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)

            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        parent = {}
        nums = set(nums)
        
        # initialize
        for n in nums:
            parent[n] = n
        
        for n in nums:
            if n-1 in nums:
                union(n, n-1)
        
        result = 0

        for n in nums:
            result = max(result, n-parent[n]+1)

        return result