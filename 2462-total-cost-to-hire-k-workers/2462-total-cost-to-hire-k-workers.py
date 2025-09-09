class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        head = costs[:candidates]
        tail = costs[max(n-candidates, candidates):]
        head_idx = candidates
        tail_idx = max(n-candidates, candidates)-1

        heapq.heapify(head)
        heapq.heapify(tail)

        total = 0

        while k > 0:
            if not tail or head and head[0] <= tail[0]:
                total += heapq.heappop(head)
                if head_idx <= tail_idx:
                    heapq.heappush(head, costs[head_idx])
                    head_idx+=1
            else:
                total += heapq.heappop(tail)
                if head_idx <= tail_idx:
                    heapq.heappush(tail, costs[tail_idx])
                    tail_idx-=1
            k-=1

        return total