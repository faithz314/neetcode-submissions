from bisect import bisect_left, bisect_right

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        idx = bisect_left(arr, x)

        l = idx - 1
        r = idx

        # my idea was very close: find the midpoint and then move left/right pointers outwards
        # return arr[l+1:r]
        while k > 0:
            if l < 0:
                r += 1
            elif r >= len(arr):
                l -= 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1

            k -= 1

        return arr[l + 1:r]

        # ATTEMPT:
        # bisect x into the array
        # two pointers out from where it's bisected?
        # idx_left = bisect_left(arr, x)
        # l = idx_left - 1
        # r = idx_right + 1

        # count = 0
        # res = []
        # while count < k:
        #     if (abs(arr[l]-x) < abs(arr[r]-x)):
        #         res.append(arr[l])
        #         count+=1
        #         l+=1
        #     elif (abs(arr[r]-x) < abs(arr[l]-x)):
        #         res.append(arr[r])
        #         count+=1
        #         r-=1
        #     elif (abs(arr[l]-x) == abs(arr[r]-x)):
        #         res.append(arr[l])
        #         count+=1
        #     else:
        #         res.append(arr[l])
        #         count+=1



