class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            stack = [[i,j]]
            visited.add((i, j))
            size = 1

            while stack:
                curi, curj = stack.pop()
                for dv, dh in directions:
                    ni, nj = curi + dv, curj + dh
                    if ni < 0 or nj < 0 or ni >= rows or nj >= cols:
                        continue
                    nbr = grid[ni][nj]

                    if (ni, nj) not in visited and nbr == 1:
                        size+=1
                        visited.add((ni, nj))
                        stack.append([ni, nj])
            
            return size





        best = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    size = dfs(i, j)
                    best = max(size, best)
        
        return best
        