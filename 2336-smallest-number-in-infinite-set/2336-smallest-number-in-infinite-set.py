class SmallestInfiniteSet:

    def __init__(self):
        self.h = [i for i in range(1, 1001)]

    def popSmallest(self) -> int:
        return heapq.heappop(self.h)

    def addBack(self, num: int) -> None:
        if num not in self.h:
            heapq.heappush(self.h, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)