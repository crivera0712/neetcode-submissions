class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # input = [3,4,5,6,1,2]
        # [3,4,5] [6,1,2] target = 1

        res = -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # left side is sorted 
            if nums[left] <= nums[mid]:
                # target falls within sorted range 
                if nums[left] <= target and nums[mid] > target: 
                    right = mid - 1
                else: 
                    left = mid + 1
            # left range is not sorted, right side is sorted
            else: 
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        

        return res

                
                        
                    