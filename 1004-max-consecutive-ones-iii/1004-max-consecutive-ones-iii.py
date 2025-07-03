class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        cnt = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                if k > 0:
                    k -= 1
                else:
                    while k == 0:
                        if nums[left] == 0:
                            k += 1
                        left+=1
                    k -= 1

            print(left, right)
            cnt = max(cnt, right-left+1)

        return cnt
