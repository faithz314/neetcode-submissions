class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # res=[]

        # factors= []
        # for idx in range(len(nums)):
        #     factors =nums[0:idx] + nums[idx+1: len(nums)]

        #     product = factors[0]
        #     for idx2 in range(1, len(factors)):
        #         product= product * factors[idx2]

        #     res.append(product)
        #     factors = []
        
        # return res


        res = [1]*len(nums)

        prefix = 1
        
        for i in range(len(nums)):
            res[i]= prefix
            prefix*= nums[i]
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i]*= postfix
            postfix*= nums[i]

        return res





            
