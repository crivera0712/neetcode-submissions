class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we are given a list of nums, we must return a list that contains
        # the products of all of the elements of nums but output[i] is the 
        # does not contain the nums[i] in its product 

        # using the prefix suffix technique we can implement an algo in 
        # O(n) time 

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        res = []

        prefix[0] = nums[0]

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        suffix[-1] = nums[-1]

        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[i+1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                val = prefix[i-1] * suffix[i+1]
                res.append(val)

        return res




