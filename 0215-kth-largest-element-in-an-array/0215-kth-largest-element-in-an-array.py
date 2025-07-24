class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            heappush(h, i)

        heap_neg = [-x for x in h]
        heapify(heap_neg)

        for i in range(k-1):
            heappop(heap_neg)
        return -heappop(heap_neg)
