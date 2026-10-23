class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # given an integer list, return true if there are any duplicate values
        # if no duplicates return false
        # input [1,1]
        # the integer 1 appears more than once, duplicate value, return false

        _sorted = sorted(nums)

        for i in range(len(_sorted) - 1):

            if _sorted[i] == _sorted[i+1]:
                return True
        
        return False

        # time comp o(n)
        # space comp o(n)

        

        