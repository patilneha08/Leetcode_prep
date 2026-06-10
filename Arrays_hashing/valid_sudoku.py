from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r=defaultdict(list)
        c=defaultdict(list)
        block=defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                elif board[i][j] in r[i] or board[i][j] in c[j] or board[i][j] in block[(i//3,j//3)]:
                    return False
                else:
                    r[i].append(board[i][j])
                    c[j].append(board[i][j])
                    block[(i//3,j//3)].append(board[i][j])
        return True