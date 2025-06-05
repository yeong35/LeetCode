class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        queue = []
        cnt = 0

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.pop(0)
            cnt += 1

            for i in graph[curr]:
                indegree[i]-=1
                
                if indegree[i]==0:
                    queue.append(i)
                
        if cnt == numCourses:
            return True
        return False