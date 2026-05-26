class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end time
        intervals.sort(key=lambda x: x[1])

        # heuristic- loop through every interval and if something overlaps, keep the 
        # interval with the shorter end time

        count = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                count+=1
            else:
                prev_end = intervals[i][1]
        return count
        