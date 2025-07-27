class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        move = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        maze[entrance[0]][entrance[1]] = '+'
        q = [entrance]
        step = 0

        while q:
            n = len(q)
            for _ in range(n):
                r, c = q.pop(0)

                for i, j in move:
                    i += r
                    j += c

                    if 0<=i<len(maze) and 0<=j<len(maze[0]) and maze[i][j] == ".":
                        if i==0 or i==len(maze)-1 or j==0 or j==len(maze[0])-1:
                            return step+1
                        q.append([i, j])
                        maze[i][j] = '+'

            step += 1
            
        return -1