
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Put every gate (0) into a queue.
        # BFS outward.
        # When visiting an empty room (INF), set its distance to grid[r][c] + 1


        q = []

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.pop(0)
            for dr, dc in directions:
                newr, newc = r+dr, c+dc
                if 0<=newr<len(grid) and 0<=newc<len(grid[0]) and grid[newr][newc]==2147483647:
                    grid[newr][newc] = grid[r][c] + 1
                    q.append((newr, newc))






# INCORRECT: DFS might not find the shortest path actually
# class Solution:
#     def islandsAndTreasure(self, grid: List[List[int]]) -> None:
#          # (i, j, stepsAway)

#         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 0 or grid[i][j] == -1:
#                     continue
#                 else:
#                     stack = [(i, j, 0)]
#                     visited = set()
#                     while stack:
#                         curI, curJ, curStep = stack.pop()
#                         for di, dj in directions:
#                             newI, newJ = curI+di, curJ+dj
#                             if 0<=newI<len(grid) and 0<=newJ<len(grid[0]):
#                                 if grid[newI][newJ] == 0:
#                                     grid[i][j] = curStep + 1
#                                     break
#                                 elif grid[newI][newJ] != -1:
#                                     stack.append((newI, newJ, curStep + 1))
#                                     visited.append((newI, newJ, curStep + 1))



