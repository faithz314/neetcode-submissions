"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # determine if overlaps exist
        # sort by start time
        intervals.sort(key=lambda x: x.start)

        # loop through each interval to check end [gap] start
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True














        # intervals.sort(key= lambda i: i.start)

        # for i in range(1, len(intervals)):
        #     i1 = intervals[i-1]
        #     i2 = intervals[i]

        #     if i1.end > i2.start:
        #         return False
        
        # return True