class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # given a list of integers 
        # return the number of ints in the list that are 
        # exactly 1 greater then the previous elements 

        # how do we know if we have a string of consecutive elements? 

        # nums = [2,20,4,10,3,4,5]
        # set = [2,20,4,10,3,5]
        # potential starts = [2,20,10]
        # 
        
        if not nums:
            return 0

        arr = set(nums)
        sequence = set()

        
        for num in arr:
            if num - 1 in arr:
                continue
            # potential start, start sequence
            sequence.add(num)
        print(sequence)

        length = 1
        for num in sequence:
            temp = 1
            while temp + num in arr:
                temp += 1
            length = max(length, temp)

        print(sequence)
        print(length)

        return length

            


