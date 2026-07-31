class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]=='.':
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i]) 
        for i in range(9):
            seen=set()
            for j in range(3):
                for k in range(3):
                    r=(i//3)*3+j
                    c=(i%3)*3+k
                    if board[r][c]=='.':
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])                       
        return True