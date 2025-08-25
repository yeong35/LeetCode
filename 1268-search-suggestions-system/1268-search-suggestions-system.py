class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        typing = ''
        ans = []

        for i in searchWord:
            typing += i
            idx = bisect_left(products, typing)

            temp = []
            for j in products[idx:idx+3]:
                if j.startswith(typing):
                    temp.append(j)
            ans.append(temp)

        return ans