class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!= 9:
            digits[-1]= digits[-1]+ 1
            return digits

        digits[-1]= digits[-1] + 1

        for idx in range(len(digits)-1,-1, -1):
            if digits[idx]== 10 and idx!= 0:
                digits[idx]=0
                digits[idx-1]= digits[idx-1]+ 1
            elif digits[idx]==10 and idx == 0:
                digits[idx]= 0
                digits.insert(0, 1)
        
        return digits
