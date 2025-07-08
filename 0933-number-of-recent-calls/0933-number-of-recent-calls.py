class RecentCounter:

    def __init__(self):
        self.storage = []

    def ping(self, t: int) -> int:
        self.storage.append(t)
        minimum = t - 3000
        for i in range(len(self.storage)):
            if self.storage[i] >= minimum:
                return len(self.storage) - i
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)