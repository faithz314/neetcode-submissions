import bisect
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list) # hm = {key: [(timestamp, value), (timestamp2, value2)]}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # note that the timestamps are strictly increasing
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect.bisect_right(self.hm[key], timestamp, key=lambda x: x[0])
        if idx <= 0:
            return ""
        print(idx-1, self.hm[key])
        return self.hm[key][idx-1][1]
        
