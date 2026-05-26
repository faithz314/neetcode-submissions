class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force: O(n^2)
        # result = 0
        # store = set(nums)
        # for num in nums:
        #     streak = 0
        #     current = num
        #     while current in store:
        #         streak+=1
        #         current+=1
        #     result = max(streak, result)
        # return result


        #hashmap
        # hm = defaultdict(int)
        # res =0

        # for num in nums:
        #     if not hm[num]:
        #         hm[num] = hm[num-1] + hm[num +1]

        #         hm[num- hm[num-1]] = hm[num]
        #         hm[num + hm[num+1]]= hm[num]

        #         res - max(res, hm[num])
        # return res


        #set based solution

        store = set(nums)
        best=0
        for n in nums:
            if (n-1) not in store: #check if n has a nieghbor
            # if not, it's a start
                length = 0
                while (n+length) in store:
                    length+=1
                
                best = max(length, best)
        
        return best









