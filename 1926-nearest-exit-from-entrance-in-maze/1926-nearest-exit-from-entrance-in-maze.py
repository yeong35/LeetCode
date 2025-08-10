class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        maze[entrance[0]][entrance[1]] = "+"
        q = [entrance]
        cnt = 0
        
        while q:
            k = len(q)
            for _ in range(k):
                x, y = q.pop(0)

                for i, j in moves:
                    i += x
                    j += y

                    if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == '.':
                        if i == 0 or j == 0 or i == len(maze)-1 or j == len(maze[0])-1:
                            return cnt+1

                        q.append([i,j])
                        maze[i][j] = '+'
            cnt += 1

        return -1


