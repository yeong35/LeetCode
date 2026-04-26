class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.arr = []

        i, j = 0, 0
        while i < len(v1) or j < len(v2):
            if i<len(v1):
                self.arr.append(v1[i])
                i+=1
            if j<len(v2):
                self.arr.append(v2[j])
                j+=1
        
        self.idx = 0        

    def next(self) -> int:
        self.idx+=1
        return self.arr[self.idx-1]

    def hasNext(self) -> bool:
        if self.idx < len(self.arr):
            return True
        return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())