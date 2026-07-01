class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        # optimize the # of pairs that can fit into each boat with limit
        # strategy: get pairs as close to the limit as possible

        # sort and then pair from the ends
        people.sort()
        l, r = 0, len(people) -1

        count = 0

        while l <= r:
            if people[r] == limit:
                count +=1
                r -=1
                continue
            
            if people[l] + people[r] <= limit:
                count +=1
                l+=1
                r-=1
            else:
                count +=1
                r -=1
            
        return count

