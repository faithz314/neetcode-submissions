class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == '':
            return True

        # step 1: find starting points
        starting_points = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    starting_points.append((i, j))
        if not starting_points:
            return False

        # step 2: dfs for each starting point
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for sr, sc in starting_points:
            # row, col, word_index, visited
            stack = [(sr, sc, 0, {(sr, sc)})]
            while stack:
                r, c, k, visited = stack.pop()
                if k == len(word) - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < len(board)
                        and 0 <= nc < len(board[0])
                        and (nr, nc) not in visited
                        and board[nr][nc] == word[k + 1]):
                        stack.append((nr, nc, k + 1, visited | {(nr, nc)}))

        return False