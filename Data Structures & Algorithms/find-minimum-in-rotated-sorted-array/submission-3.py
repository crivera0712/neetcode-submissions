class Solution:
    def findMin(self, nums: List[int]) -> int:
        # given a list that was sorted in asc but has been rotated
        # find the minimum value within the list 

        # nums=[9,-5,-2,0,3]
        # [9, | -5, -2, 0, 3]

        left, right = 0, len(nums) - 1

        while left < right: 
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            if nums[mid] < nums[right]:
                right = mid
        
        mid = (left + right) // 2
        
        return nums[mid]

        