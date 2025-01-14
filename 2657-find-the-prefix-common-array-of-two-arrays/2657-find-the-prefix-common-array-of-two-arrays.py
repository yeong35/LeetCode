class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        nums = [0] * 51
        cnt = 0

        ans = []

        for a, b in zip(A,B):
            nums[a]+=1
            nums[b]+=1

            if a == b:
                cnt+=1
            else:
                if nums[a] > 1:
                    cnt+=1
                if nums[b] > 1:
                    cnt+=1
            ans.append(cnt)

        return ans