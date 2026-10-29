class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # we are given a list of numbers, nums, we must return a list, res, 
        # where res[i] is the product of all the elements in nums except for nums[i]

        # input = [1,2,4,6]
        # output = [48,24,12,8]

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        res = [0] * len(nums)

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        for i in range(len(res)):
            if i == 0:
                res[i] = suffix[i+1]
            elif i == len(res) - 1:
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1] * suffix[i+1]
            
        return res
            

            
        

            
        