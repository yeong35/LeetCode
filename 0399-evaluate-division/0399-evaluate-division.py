class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def evaluate(start, target, h, curr):
            temp = -1

            if start == target:
                return curr
            else:
                for neighbor in h[start]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        temp = evaluate(neighbor, target, h, curr*h[start][neighbor])
                        if temp != -1:
                            break
                        visit.remove(neighbor)

            return temp
        
        ans = []
        h = defaultdict(defaultdict)
        visit = set()

        for (a, b), value in zip(equations, values):
            h[a][b]=value
            h[b][a]=1/value
        
        for a, b in queries:
            temp = 1
            if a not in h or b not in h:
                temp = -1
            elif a == b:
                temp = 1
            else:
                visit = set()
                visit.add(a)
                temp = evaluate(a, b, h, 1)
                
            ans.append(temp)
    
        return ans