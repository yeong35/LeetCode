class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse = True)

        heap = []
        n1Sum = 0
        result = 0

        for n2, n1 in pairs:
            heapq.heappush(heap, n1)
            n1Sum += n1

            if len(heap) > k:
                temp = heapq.heappop(heap)
                n1Sum -= temp
            
            if len(heap) == k:
                result = max(result, n1Sum*n2)

        return result