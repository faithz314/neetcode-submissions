class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            stack = [[i, j]]
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

            while stack:
                curi, curj = stack.pop()
                for dh, dv in directions:
                    ni, nj = curi + dh, curj + dv
                    if ni < 0 or nj < 0 or ni >= rows or nj >= cols:
                        continue
                    if grid[ni][nj] == "1" and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        stack.append([ni, nj])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands +=1

        return islands
