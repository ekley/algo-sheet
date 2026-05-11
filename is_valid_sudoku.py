def isValidSudoku(board):
    n = 9
    
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    boxes = [set() for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            val = board[i][j]
            
            if val == '.':
                continue
            
            if val in rows[i]:
                return False
            rows[i] = val    
            
            if val in cols[j]:
                return False
            cols[j] = val
            
            idx = i//3 * 3 + j//3    
            if val in boxes[idx]:
                return False
            boxes[idx] = val
            
    return True

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board))