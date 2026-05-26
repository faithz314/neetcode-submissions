class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        




        #sorted in non decreasing order

        #have 2 pointers -> increase/decrease one of the pointers based on the sum


        p1 = 0
        p2 = len(numbers)-1

        #length is always at least 2 since there's always at least 1 valid answer

        sm = numbers[p1] + numbers[p2]


        while sm != target:
            if sm > target:
                p2-=1
            if sm < target:
                p1+=1

            sm = numbers[p1] + numbers[p2]
        return [p1+1, p2+1]
    
            

