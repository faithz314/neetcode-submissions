class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = defaultdict(int) # if key dne, initialize to 0
        currentMax = 0
        maxElement = 0

        for num in nums:
            hm[num] +=1
            if currentMax < hm[num]:
                maxElement = num
                currentMax = hm[num]

        return maxElement
