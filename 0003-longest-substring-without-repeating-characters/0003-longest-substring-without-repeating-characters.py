class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        result = 0
        left = 0

        for right in range(len(s)):
            cnt[s[right]]+=1

            while cnt[s[right]] > 1:
                cnt[s[left]]-=1
                left+=1    

            result = max(result, right-left+1)

        return result