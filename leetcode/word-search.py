# https://leetcode.com/problems/word-search/
# ------------------------------------------------------------------------------- #
def solution(board, word):
    def exist(pos, r, c):
        if pos == len(word): return True
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c]==True or board[r][c] != word[pos]: return False
        retained_val,board[r][c] = board[r][c],True
        result = ( exist(pos+1, r+1, c) or exist(pos+1, r-1, c) or exist(pos+1, r, c+1) or exist(pos+1, r, c-1) ) 
        board[r][c] = retained_val
        return result
    for r in range(len(board)):
        for c in range(len(board[0])): 
            if exist(0, r, c): return True
    return False
# ------------------------------------------------------------------------------- #
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]  
print(solution(board, "ABCCED"))
print(solution(board, "SEE"))
print(solution(board, "ABCB"))
print(solution(board, "ABFDEESCC"))

>>> True
>>> True
>>> False
>>> True
