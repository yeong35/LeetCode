class RecentCounter:

    def __init__(self):
        self.que = []

    def ping(self, t: int) -> int:
        self.que.append(t)

        idx = 0
        for i in range(len(self.que)):
            if self.que[i]>=t-3000:
                idx = i
                break

        self.que = self.que[i:]

        return len(self.que)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)