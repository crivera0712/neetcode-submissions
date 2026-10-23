class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given a list of numbers, return the k most frequent elements within the array 
        # k is the amount of numbers in the list that we are returning 

        # input = [1,2,2] k = 2
        # output: [1,2]

        # we will be a dict as our ds
        # keys are the ints, values are the freq

        freq = dict()

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # now we have a dict with the frequency of every num
        res = list()

        for i in range(k):
            key = max(freq, key=freq.get)
            res.append(key)
            del freq[key]
            
        return res

        
        


