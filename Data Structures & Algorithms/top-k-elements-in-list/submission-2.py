class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # THIS ALGORITHM IS CALLED BUCKET SORT
        hm = defaultdict(int)
        for num in nums:
            hm[num] +=1

        freq = [[] for i in range(len(nums) + 1)]
        for key, value in hm.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

            


        