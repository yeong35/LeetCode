class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair = [[i,j] for i, j in zip(nums1, nums2)]
        pair.sort(key = lambda x: -x[1])

        k_heap = [i for i, j in pair[:k]]
        heapq.heapify(k_heap)
        total = sum(k_heap)
        ans = total*pair[k-1][1]

        for i in range(k, len(pair)):
            total -= heapq.heappop(k_heap)
            heapq.heappush(k_heap, pair[i][0])
            total += pair[i][0]

            ans = max(ans, total*pair[i][1])

        return ans