class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given an integer list, return true if there are any duplicate values
        # if no duplicates return false
        # input [1,1]
        # the integer 1 appears more than once, duplicate value, return false

        res = set()

        for num in nums:
            if num in res:
                return True 
            else: 
                res.add(num)
        
        return False

        

        