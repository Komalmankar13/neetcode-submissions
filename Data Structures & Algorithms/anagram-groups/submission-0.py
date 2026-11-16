class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency = {}
        for word in strs:
            key = "".join(sorted(word))

            if key in frequency:
                frequency[key].append(word)
            
            else:
                frequency[key] = [word]
        
        return list(frequency.values())
        