class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        
        def isValid(x, y):
            if 0 <= x < rows and 0<=y<cols and maze[x][y] == '.':
                return True
            return False

        x, y = entrance
        maze[x][y] = '+'
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        que = deque()
        que.append((x, y, 0))

        while que:
            x, y, step = que.popleft()
            
            for i, j in directions:
                i += x
                j += y

                if isValid(i,j):
                    if i == 0 or j == 0 or i == rows-1 or j == cols-1:
                        return step+1

                    que.append((i,j,step+1))
                    maze[i][j] = "+"

        return -1