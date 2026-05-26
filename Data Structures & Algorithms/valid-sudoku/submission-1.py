class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(9):
            seen = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True

        # FIRST ATTEMPT
        # for row in board:
        #     row_set = set(row)
        #     if len(row_set) != len(row):
        #         return False
        #     for num in row:
        #         if num < 1 or num > 9:
        #             return "row"
        
        # for col in range(len(board[0])):
        #     col_set = set()
        #     for row in range(len(board)):
        #         if board[row][col] in col_set or board[row][col] < 1 or board[row][col] > 9:
        #             return False
        #         col_set.add(board[i][j])
        
        # #9 boxes to check
        # #(02, 02), (35, 02), (68, 02)
        # #(02, 35), (35, 35), (68, 35)
        # #(02, 68), (35, 68), (68, 68)

        # #when looping, start from n-2 away
        # boxes = [(2, 2), (5, 2), (8,2),
        #          (2, 5), (5, 5), (8,5),
        #          (2, 8), (5, 8), (8,8)]

        # for box in boxes:
        #     box_set= set()
        #     for i in range(box[0]-2, box[0]+1):
        #         for j in range(box[1]-2, box[1]+1):
        #             if board[i][j] in box_set or board[i][j] < 1 or board[i][j] > 9:
        #                 return False
        #             box_set.add(board[i][j])
        
        # return True





