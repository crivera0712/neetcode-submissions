class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given a list of numbers and a target number 
        # return two place values such that these places values when added
        # are equal to target 
        # every input has exactly on pair of indicies that satisfy the condition 

        # use a dict, index is key value num
        # subtract the value that we are looking at from target and see if the 
        # compliment is in the dict

        seen = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in seen:
                return [seen[compliment],i]
            else:
                seen[nums[i]] = i
        