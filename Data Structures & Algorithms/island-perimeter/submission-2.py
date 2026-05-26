class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # iterative dfs solution
        # rows, cols = len(grid), len(grid[0])
        # visited = set()

        # def dfs(i, j):
        #     stack = [(i, j)]
        #     visited.add((i, j))
        #     perimeter = 0
        #     directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        #     while stack:
        #         curi, curj = stack.pop()
        #         for dh, dv in directions:
        #             ni, nj = curi + dh, curj + dv

        #             if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
        #                 perimeter += 1
        #                 continue

        #             if grid[ni][nj] == 0:
        #                 perimeter += 1
        #             else:
        #                 if (ni, nj) not in visited:
        #                     visited.add((ni, nj))
        #                     stack.append((ni, nj))
        #     return perimeter

        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == 1:
        #             return dfs(i, j)
        # return 0


        # can also just check every box and count perimeter
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                # optimistically assume all 4 edges are perimeter
                if grid[i][j] == 1:
                    perimeter += 4

                    # subtract shared edges from previous
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        
        return perimeter









