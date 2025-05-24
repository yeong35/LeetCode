from collections import defaultdict

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.dictionary = {}

        for i in nums:
            if i not in self.dictionary:
                self.dictionary[i] = 0
            self.dictionary[i] += 1

    def showFirstUnique(self) -> int:
        for i in self.arr:
            if self.dictionary[i] == 1:
                return i

        return -1

    def add(self, value: int) -> None:
        self.arr.append(value)
        
        if value not in self.dictionary:
            self.dictionary[value] = 0
        self.dictionary[value] += 1
            

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)