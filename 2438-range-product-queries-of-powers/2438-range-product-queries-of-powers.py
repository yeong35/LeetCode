class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        modulo = pow(10, 9)+7

        ans = []
        power = []
        n = bin(n)[2:]

        temp = 1
        for i in reversed(n):
            if i == '1':
                power.append(temp)
            temp*=2

        for i, j in queries:
            temp = 1
            for k in range(i, j+1):
                temp = (temp*power[k])%modulo
            ans.append(temp)

        return ans