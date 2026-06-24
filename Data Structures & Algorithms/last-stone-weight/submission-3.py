import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap) #creates a min-heap (we're actually going to create a max-heap)
        
        # heappush -> add an itme
        # heappop -> remove the smallest (in our case largest) item

        while len(max_heap) > 1:
            first_stone = -(heapq.heappop(max_heap))
            second_stone = -(heapq.heappop(max_heap))
            if first_stone == second_stone:
                continue
            if first_stone > second_stone:
                new_stone = first_stone - second_stone
                heapq.heappush(max_heap, -new_stone)
            # this else is unnecessary since the heapq will always push in weight order:
            # else:
            #     new_stone = first_stone - second_stone
            #     heapq.heappush(max_heap, -new_stone)
        
        if max_heap:
            return -heapq.heappop(max_heap)
        return 0
