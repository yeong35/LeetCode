class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = costs[:candidates]
        right = costs[max(candidates, len(costs)-candidates):]

        left_idx = candidates
        right_idx = max(candidates, len(costs)-candidates)-1

        heapq.heapify(left)
        heapq.heapify(right)

        total = 0

        for _ in range(k):
            if not right or left[0] <= right[0]:
                total += heapq.heappop(left)
                if left_idx <= right_idx:
                    heapq.heappush(left, costs[left_idx])
                    left_idx+=1
            else:
                total += heapq.heappop(right)
                if left_idx <= right_idx:
                    heapq.heappush(right, costs[right_idx])
                    right_idx-=1

        return total