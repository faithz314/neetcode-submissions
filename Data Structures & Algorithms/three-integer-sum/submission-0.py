class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:



        #brute force is to legit check every single triplet 



        #two pointers is the optimal solution

        res = []
        nums.sort()


        for idx,item in enumerate(nums):
            if item >0:
                break
            
            if idx >0 and item == nums[idx-1]:
                continue
            
            p1 = idx+1
            p2 = len(nums)-1

            while p1 < p2:
                sm = item + nums[p1] + nums[p2]

                if sm >0:
                    p2 -=1
                elif sm < 0:
                    p1 +=1
                else:
                    res.append([item, nums[p1], nums[p2]])
                    p1+=1
                    p2 -=1
                    while nums[p1]== nums[p1-1] and p1 <p2:
                        p1+=1
        return res