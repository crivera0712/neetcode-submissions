class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # given a list of strings, group all of the strings that are
        # anagrams of each other into a seperate sublists 
        # it may be returned in any order

        # an anagram is a string that contains the exact same characters as another
        # string but char order can be different

        # dictionary count is key, val is string
        res = defaultdict(list)

        
        for s in strs:
            count = [0] * 26
            # need to compare ascii value 
            for c in s: 
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        
        return list(res.values())





        





        
        
        
        