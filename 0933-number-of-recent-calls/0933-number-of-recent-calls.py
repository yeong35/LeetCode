class RecentCounter:

    def __init__(self):
        self.save = []

    def ping(self, t: int) -> int:
        self.save.append(t)
        while self.save and self.save[0] < t-3000:
            self.save.pop(0)
        
        return len(self.save)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)