class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # find all of the starting points
        rotten = []
        # INTRODUCE A FRESH VARIABLE
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i, j))
                elif grid[i][j] == 1:
                    fresh+=1
    
        # Incorrect: too many loops
        # minutes = 0
        # stack = [rotten]
        # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # while stack:
        #     curRotten = stack.pop()
        #     newRotten = []
        #     for rotI, rotJ in curRotten:
        #         for di, dj in directions:
        #             newI, newJ = rotI + di, rotJ + dj
        #             if 0<=newI<rows and 0<=newJ<cols and grid[newI][newJ]==1:
        #                 grid[newI][newJ] = 2
        #                 newRotten.append((newI, newJ))
        #     stack.append(newRotten)
        #     minutes +=1

        # do bfs/dfs with layers of rotten
        minutes = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while rotten and fresh > 0:
            new_rotten = []

            for r, c in rotten:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        new_rotten.append((nr, nc))

            rotten = new_rotten
            minutes += 1

        return minutes if fresh == 0 else -1














