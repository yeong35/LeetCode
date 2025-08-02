class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = defaultdict(int)
        small = float('inf')
        arr = []

        for i in basket1:
            count[i] += 1
            small = min(small, i)

        for i in basket2:
            count[i] -= 1
            small = min(small, i)
        
        for i in count:
            if count[i]%2==1:
                return -1
            
            temp = abs(count[i])//2
            while temp > 0:
                arr.append(i)
                temp -= 1
        
        cost = 0
        arr.sort()

        for i in range(len(arr)//2):
            # print(arr[i], small)
            cost += min(small*2, arr[i])
        return cost