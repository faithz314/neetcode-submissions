class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #brute force: check every triplet
        triplets = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.append([nums[i],nums[j],nums[k]])
        
        for triplet in triplets:
            triplet.sort()
        newtrips = [tuple(triplet) for triplet in triplets]
        
        tripset= list(set(newtrips))
        return tripset
