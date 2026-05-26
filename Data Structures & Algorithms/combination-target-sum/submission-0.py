# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []
#         nums.sort()

#         def dfs(i, cur, total):
#             if total == target:
#                 res.append(cur.copy())
#                 return
            
#             for j in range(i, len(nums)):
#                 if total + nums[j] > target:
#                     return
#                 cur.append(nums[j])
#                 dfs(j, cur, total+nums[j])
#                 cur.pop()

#         dfs(0, [], 0)
#         return res
        
# iterative solution
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        # stack stores: (start_index, current_combination, current_total)
        stack = [(0, [], 0)]

        while stack:
            i, cur, total = stack.pop()

            if total == target:
                res.append(cur)
                continue

            for j in range(i, len(nums)):
                new_total = total + nums[j]

                if new_total > target:
                    break

                stack.append((
                    j,
                    cur + [nums[j]],
                    new_total
                ))

        return res