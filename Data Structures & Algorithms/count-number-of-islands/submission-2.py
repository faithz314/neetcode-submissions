class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        # look for island starts
        # then dfs each start
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            stack = [[r,c]]
            grid[r][c] = "0"
            
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == "0"
                    ):
                        continue
                    stack.append((nr, nc))
                    grid[nr][nc] = "0" 
            


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count+=1
        
        return count

        