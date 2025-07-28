class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def traverse(start, target, curr):
            temp = -1.0
            visit.add(start)

            if target in graph[start]:
                visit.remove(start)
                return curr*graph[start][target]
            
            for neighbor in graph[start]:
                if neighbor not in visit:
                    temp = traverse(neighbor, target, curr*graph[start][neighbor])
                    if temp != -1:
                        break
            
            visit.remove(start)

            return temp

        graph = defaultdict(defaultdict)
        visit = set()

        result = []

        for (i, j), k in zip(equations, values):
            graph[i][j] = k
            graph[j][i] = 1/k

        for i, j in queries:
            if i not in graph or j not in graph:
                result.append(-1.0)
            elif i == j:
                result.append(1.0)
            else:
                result.append(traverse(i, j, 1))
        
        return result