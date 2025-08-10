class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        sec = 0
        maze[entrance[0]][entrance[1]] = "+"
        q = [entrance]
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            k = len(q)

            for _ in range(k):
                x, y = q.pop(0)

                for i, j in moves:
                    i += x
                    j += y

                    if 0<=i<n and 0<=j<m and maze[i][j] == '.':
                        if i == n-1 or i == 0 or j==m-1 or j==0:
                            return sec+1
                        maze[i][j] = '+'
                        q.append([i,j])
            
            sec += 1

        return -1