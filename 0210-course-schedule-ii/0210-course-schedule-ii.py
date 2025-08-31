class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        queue = []
        result = []

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        
        print(indegree)

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.pop(0)
            result.append(current)

            for i in graph[current]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        if len(result) == numCourses:
            return result
        return []