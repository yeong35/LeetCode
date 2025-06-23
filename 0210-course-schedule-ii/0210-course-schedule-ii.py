class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.pop(0)
            result.append(curr)
            for i in graph[curr]:
                indegree[i]-= 1

                if indegree[i] == 0:
                    queue.append(i)

        if numCourses == len(result):
            return result
        
        return []