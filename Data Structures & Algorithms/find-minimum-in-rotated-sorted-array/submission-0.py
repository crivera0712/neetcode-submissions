class Solution:
    def findMin(self, nums: List[int]) -> int:

        # given a rotated list that was previously sorted in asc order
        # find the minimum value in the rotated array 
        # the array can only be sorted between 1 and n times
        # all elemeints are unique 


        # rotate array via binary search to find min value 
        # compare first and last values  
        # is nums[mid] bigger than nums[right]? 

        # n = len(nums) - 1 = 6

        # n // 2 = 3
        
        # [4,1,2,3]

        # [3,4,5,6,1,2]

        # [4,5,6,7]
        # [7,4,5,6]
        # [6,7,4,5]
        # [5,6,7,4]

        #[3,4,5,6,1,2]

        left, right = 0, len(nums) - 1
        
        while left < right: 
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]



        
        

        

        


        

        