class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # pointer to the prev_end
        
        # 1) sort by end time
        intervals.sort(key=lambda x: x[1])

        # 2) keep track of prev_end
        prev_end = intervals[0][1]
        overlaps = 0
        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i][0], intervals[i][1]
            # if overlap
            if curStart < prev_end:
                overlaps +=1
            else:
                prev_end = intervals[i][1]
        return overlaps

        