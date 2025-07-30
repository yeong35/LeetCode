class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [[i,j] for i,j in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        
        k_heap = [i for i,j in pairs[:k]]
        heapq.heapify(k_heap)
        curr = sum(k_heap)
        result = sum(k_heap)*pairs[k-1][1]

        for i, j in pairs[k:]:
            curr -= heapq.heappop(k_heap)
            curr += i
            heapq.heappush(k_heap, i)

            result = max(result, curr*j)

        return result