class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        c = chars[0]
        idx = 0
        left = 0
        right = 0

        while right < n:
            while right < n and chars[right] == c:
                right+=1

            chars[idx] = c
            idx+=1
            c = chars[right] if right < n else ''

            if right - left > 1:
                m = str(right - left)

                for i in m:
                    chars[idx] = i
                    idx+=1

            left = right

        return idx

        

