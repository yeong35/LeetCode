class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        curr = 0
        T = 0

        result = 0

        for i in range(len(calories)):
            if curr >= k:
                curr -= 1
                T -= calories[i-k]
            
            T += calories[i]
            curr += 1
            if curr == k:
                if T < lower:
                    result -= 1
                if T > upper:
                    result += 1

        return result