class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s=set()
            for i in row:
                if i=='.':
                    continue
                if i in s:
                    return False
                else:
                    s.add(i)
        for col in range(len(board)):
            s1=set()
            for row in range(len(board)):
                if board[row][col]==".":
                    continue
                if board[row][col] in s1:
                    return False
                else:
                    s1.add(board[row][col])

        
        for r in range(0,9,3):
            for c in range(0,9,3):
                s2=set()
                for i in range(0,3):
                    for j in range(0,3):
                        if board[r+i][c+j]==".":
                            continue
                        if board[r+i][c+j] in s2:
                            return False
                        else:
                            s2.add(board[r+i][c+j])

        return True

            

        