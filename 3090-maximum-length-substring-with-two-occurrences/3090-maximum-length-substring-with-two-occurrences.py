class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        right = 0
        counter = defaultdict(int)
        result = 0

        while right < len(s):

            counter[s[right]]+=1

            while counter[s[right]]>2:
                counter[s[left]]-=1
                left+=1
            
            result = max(result, right-left+1)

            right+=1

        return result