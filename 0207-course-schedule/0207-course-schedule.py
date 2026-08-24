class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]

        indegree = [0] * numCourses

        complete = 0

        for course, pre in prerequisites:
            graph[course].append(pre)
            indegree[course] += 1
        
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            complete += 1

            for idx in range(numCourses):
                if curr in graph[idx]:
                    indegree[idx] -= 1

                    if indegree[idx] == 0:
                        q.append(idx)
        
        return complete == numCourses
        