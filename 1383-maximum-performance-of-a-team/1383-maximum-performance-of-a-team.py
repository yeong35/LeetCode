class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = sorted(zip(efficiency, speed), reverse = True)

        heap = []
        speedSum = 0
        result = 0

        mod = pow(10,9)+7

        for p, s in pairs:
            heapq.heappush(heap, s)
            speedSum += s

            if len(heap) > k:
                speedSum -= heapq.heappop(heap)
            
            result = max(result, speedSum*p)

        return result%mod