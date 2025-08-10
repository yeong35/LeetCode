class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sold = [0]*n
        hold = [-prices[0]]*n

        for i in range(1, n):
            sold[i] = max(hold[i-1]+prices[i]-fee, sold[i-1])
            hold[i] = max(sold[i-1]-prices[i], hold[i-1])

        return sold[-1]