class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashMap = Counter(arr)
        check = set()

        for i in hashMap:
            if hashMap[i] not in check:
                check.add(hashMap[i])
            else:
                return False
        
        return True