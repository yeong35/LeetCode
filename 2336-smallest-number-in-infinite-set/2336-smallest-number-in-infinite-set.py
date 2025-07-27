import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.h = [i+1 for i in range(1000)]
        self.s = set(self.h)

    def popSmallest(self) -> int:
        n = heapq.heappop(self.h)
        self.s.remove(n)
        return n
        

    def addBack(self, num: int) -> None:
        if num not in self.s:
            heapq.heappush(self.h, num)
            self.s.add(num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)