from bisect import bisect_left
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        target = newInterval[0]
        idx = bisect_left(intervals, newInterval)
        intervals.insert(idx, newInterval)

        # now get rid of overlaps
        res = []
        for interval in intervals:
            curStart, curEnd = interval[0], interval[1]
            if not res:
                res.append(interval)
            # if there is no overlap between prev and curInterval
            elif res[-1][1] < curStart:
                res.append(interval)
            # if there is an overlap between prev and curInterval
            # change the end of res[-1][1]
            else:
                res[-1][1]= max(res[-1][1], curEnd)
        return res
                
