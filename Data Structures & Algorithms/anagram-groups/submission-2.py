class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # dictionary of {sortedWord: word}
        hm = {}
        for word in strs:
            sortedWord = str(sorted(word))
            if sortedWord not in hm:
                hm[sortedWord]= [word]
            else:
                hm[sortedWord].append(word)
        
        return list(hm.values())
        