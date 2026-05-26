class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #twoSum with two pointers lol
        l = 0
        r = len(numbers) -1

        while l < r:
            sm = numbers[l] + numbers[r]
            if sm == target:
                return [l+1, r+1]
            elif sm < target:
                l+=1
            else:
                r -=1
        
        return -1
        