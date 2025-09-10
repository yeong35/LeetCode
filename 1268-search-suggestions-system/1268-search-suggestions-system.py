class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        t = ""
        for i in searchWord:
            t += i
            idx = bisect_left(products, t)
            
            temp = []
            for word in products[idx:idx+3]:
                if word.startswith(t):
                    temp.append(word)
            ans.append(temp)
        return ans