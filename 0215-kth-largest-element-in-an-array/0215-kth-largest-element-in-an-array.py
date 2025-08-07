class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_heap = nums[:k]
        
        heapq.heapify(k_heap)

        for i in nums[k:]:
            heapq.heappush(k_heap, i)
            heapq.heappop(k_heap)

        return heapq.heappop(k_heap)
