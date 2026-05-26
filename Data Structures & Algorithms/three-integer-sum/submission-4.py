class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force: check every triplet
        # triplets = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplets.append([nums[i],nums[j],nums[k]])
        
        # for triplet in triplets:
        #     triplet.sort()
        # newtrips = [tuple(triplet) for triplet in triplets]
        # tripset= list(set(newtrips))
        # return tripset



        # solution- two pointers
        # sort the array, fix one number and then search for the other two

        nums.sort()
        result = []

        for i in range(len(nums)):
            # edge case; break since all remaining numbers are positive
            if nums[i] > 0:
                break
            
            # edge case; skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums) -1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    # then skip duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                if threeSum < 0:
                    l+=1
                if threeSum > 0:
                    r-=1
        return result

                  




