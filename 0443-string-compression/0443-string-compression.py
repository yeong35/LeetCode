class Solution:
    def compress(self, chars: List[str]) -> int:
        compIdx = 0
        char = chars[0]
        cnt = 1
        
        for idx in range(1, len(chars)):
            if chars[idx] == char:
                cnt+=1
            else:
                if cnt == 1:
                    chars[compIdx] = char
                    compIdx+=1

                    char = chars[idx]
                    cnt = 1
                else:
                    chars[compIdx] = char
                    compIdx+=1

                    s = str(cnt)
                    for i in s:
                        chars[compIdx] = i
                        compIdx+=1

                    char = chars[idx]
                    cnt = 1

        # trim
        if cnt == 1:
            chars[compIdx] = char
            compIdx+=1
        else:
            chars[compIdx] = char
            compIdx+=1

            s = str(cnt)
            for i in s:
                chars[compIdx] = i
                compIdx+=1


        return compIdx