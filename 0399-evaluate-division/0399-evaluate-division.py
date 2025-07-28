class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def find(start, target, val):

            visit.add(start)
            r = -1.0
            if start == target:
                return val
            
            if target in h[start]:
                r = val*h[start][target]
            else:
                for neighbor in h[start]:
                    if neighbor not in visit:
                        r = find(neighbor, target, val*h[start][neighbor])
                    if r != -1:
                        break
            visit.remove(start)
            return r


        h = defaultdict(defaultdict)
        visit = set()
        result = []
        for (i, j), value in zip(equations, values):
            h[i][j] = value
            h[j][i] = 1/value

        for i, j in queries:
            val = -1.0
            if i not in h or j not in h:
                val = -1
            elif i==j:
                val = 1.0
            else:
                val = find(i, j, 1)
            
            result.append(val)


        return result