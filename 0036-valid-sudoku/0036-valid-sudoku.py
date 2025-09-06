class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            temp = [x[i] for x in board]
            cols = Counter(temp)
            rows = Counter(board[i])
            
            for j in cols:
                if j.isdigit() and cols[j] > 1:
                    return False
            for j in rows:
                if j.isdigit() and rows[j] > 1:
                    return False


        arr = [defaultdict(int) for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    t = (i//3)*3 + j//3
                    arr[t][board[i][j]]+=1

                    if arr[t][board[i][j]]>1:
                        return False



        return True