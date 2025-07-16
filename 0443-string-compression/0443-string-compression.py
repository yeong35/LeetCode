class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        idx = 0
        c = chars[0]

        
        for right in range(len(chars)):
            if chars[right] != c:
                chars[idx] = c
                idx+=1
                if right - left > 1:
                    n = str(right-left)
                    for i in n:
                        chars[idx] = i
                        idx+=1

                c = chars[right]
                left = right
        

        chars[idx] = c
        idx+=1
        if len(chars) - left > 1:
            n = str(len(chars)-left)
            for i in n:
                chars[idx] = i
                idx+=1

        return idx