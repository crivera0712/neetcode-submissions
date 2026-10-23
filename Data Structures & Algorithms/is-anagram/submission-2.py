class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # given two strings, cheeck if they are anagrams of each other 
        # two strings are considered anagrams of each other if they contain 
        # the same characters with each character appearing the same number 
        # of times, regardless of order 

        # trap words: anagram 

        # expected return values: 
        # return true if they both ARE anagrams
        # return False if they are NOT anagrams 

        # use a dict

        if len(s) != len(t):
            return False
        
        freq_s = {}
        freq_t = {}

        for x in s:
            if x in freq_s:
                freq_s[x] += 1
            else:
                freq_s[x] = 1

        for x in t: 
            if x in freq_t:
                freq_t[x] += 1
            else:
                freq_t[x] = 1
        
        return freq_s == freq_t
        
         

