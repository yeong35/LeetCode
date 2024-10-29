class Solution:
    def compress(self, chars: List[str]) -> int:
        last = chars[0]
        cnt = 1

        s = [chars[0]]

        for i in range(1, len(chars)):
            print(chars[i], s[-1])
            if chars[i] != last:
                if cnt > 1:
                    s += str(cnt)
                last = chars[i]
                s += chars[i]
                cnt = 1
            else:
                cnt+=1

        if cnt > 2:
            s += str(cnt)

        print(s)

        chars[:len(s)] = s
        return len(s)