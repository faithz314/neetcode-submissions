class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time first
        intervals.sort()
        res= []
        for interval in intervals:
            curStart, curEnd = interval[0], interval[1]
            if not res:
                res.append(interval)
            else:
                prevEnd = res[-1][1]
                # if no overlap
                if prevEnd < curStart:
                    res.append(interval)
                # otherwise if overlapped
                elif prevEnd >= curStart:
                    if prevEnd < curEnd:
                        res[-1][1]=curEnd
        return res

        