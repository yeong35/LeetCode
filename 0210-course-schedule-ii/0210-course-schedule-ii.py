class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        queue = []

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.pop(0)
            result.append(curr)

            for i in graph[curr]:
                indegree[i]-=1
                if indegree[i] == 0:
                    queue.append(i)
    
        if len(result) == numCourses:
            return result
        
        return []

