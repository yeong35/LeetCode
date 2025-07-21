class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindromes(low, high):
            ans = ""
            while low >= 0 and high < len(s):
                if s[low] != s[high]:
                    break
                
                ans = s[low:high+1]

                low -= 1
                high += 1

            return ans

        longest = ""
        for i in range(len(s)):
            temp = palindromes(i, i)

            if len(longest) < len(temp):
                longest = temp
            
            temp = palindromes(i, i+1)

            if len(longest) < len(temp):
                longest = temp

        return longest