class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        res=[]

        factors= []
        for idx in range(len(nums)):
            factors =nums[0:idx] + nums[idx+1: len(nums)]

            product = factors[0]
            for idx2 in range(1, len(factors)):
                product= product * factors[idx2]

            res.append(product)
            factors = []
        
        return res

            
