"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1)) #+1 = need a room
            time.append((i.end, -1)) #-1 = free a room

        #Sort meetings by time
        #Secondarily sort meetings by event type (+1 before -1)
        time.sort(key=lambda x: (x[0], x[1]))

        # time = [(0, 1), (5, 1), (10, -1), (15, 1), (20, -1), (40, -1)]
        # heuristic = the minimum number of rooms = maximum number of overlapping meetings at one time
        roomCount = 0
        meetingCount = 0 
        for t in time:
            meetingCount += t[1]
            roomCount = max(roomCount, meetingCount)
        return roomCount
        
        

