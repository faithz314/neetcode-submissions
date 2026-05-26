class Solution:
    def canJump(self, nums: List[int]) -> bool:
        


        # p1 = 0
        # jump = nums[p1]

        # if len(nums)==1:
        #     return True


        # while p1 != -1:
        #     p1 = p1 + jump


        #     if p1 >= len(nums)-1:
        #         return True
            
        #     jump = nums[p1]

        #     if jump ==0:
        #         return False


        goal = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal ==0
            


