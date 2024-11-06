class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        sorted_nums = sorted(nums)
        operated_nums = []

        head = 0
        tail = 0

        prev = bin(nums[0]).count('1')
        curr = None

        for i in range(1, len(nums)):
            curr = bin(nums[i]).count('1')
            
            if prev == curr:
                tail = i
            else:
                operated_nums += sorted(nums[head:tail+1])

                prev = curr
                head = i
                tail = i

        if head != tail:
            operated_nums += sorted(nums[head:tail+1])
        else:
            operated_nums.append(nums[head])

        return operated_nums == sorted_nums