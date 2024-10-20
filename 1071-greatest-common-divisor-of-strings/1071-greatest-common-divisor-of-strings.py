class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length = min(len(str1), len(str2))
        prefix = []

        for i in range(length):
            if str1[i] != str2[i]:
                break
            else:
                prefix += str1[i]

        longer = ""
        if len(str1) > len(str2):
            longer = str1
        else:
            longer = str2

        prefix = "".join(prefix)

        for i in reversed(range(1, len(prefix)+1)):
            if len(str1)%i==0 and len(str2)%i==0:
                start = 0
                end = i
                while start < len(longer):
                    print("hihi", prefix[:i], longer[start:end])
                    if longer[start:end] != prefix[:i]:
                        return ""
                    else:
                        start = end
                        end = end+i
                
                return "".join(prefix[:i])
            
        return ""