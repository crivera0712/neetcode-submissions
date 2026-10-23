class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we are given a list of numbers and a target int
        # return whether target is inside the list of given numbers

        # constraints: the list nums is sorted in ascending order
        # all integers in nums is distinct 
        # solution must be in O(logn) time 

        # input: [0,1,3]
        # target = 3
        # 2

        left, right = 0, len(nums) - 1

        mid = (left + right) // 2 # take the floor

        while left <= right:
            if target > nums[mid]: 
                left = mid + 1
            if target < nums[mid]: 
                right = mid - 1
            
            if target == nums[mid]:
                return mid
            
            mid = (left + right) // 2

        return -1

        # time comp: O(logn) 
        # this is because we are splitting the input size by 2 each iteration

        # space comp is O(1), space does not change depending on the input size or n