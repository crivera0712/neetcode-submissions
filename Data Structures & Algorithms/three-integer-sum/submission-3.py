class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # given a list of integers, return all of the triplets 
        # such that [nums[i], nums[j], nums[k]] when summed == 0
        # i,j,k are all distinct (different) values

        # nums = [-1,0,1,2,-1,-4]
        # nums.sort() = [-4,-1,-1,0,1,2]
        # output: [[-1,-1,2],[-1,0,-1]]
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # check if a > 0, if so break 
            # this is because left and right pointers will always be
            # ahead of a. if a > 0 there is no possible way to achieve 0
            if a > 0:
                break
            # skip duplicate value
            if i > 0 and a == nums[i-1]:
                continue
            
            # init left and right pointer
            left,right = i + 1, len(nums) - 1
    
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    res.append([a,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    # skip duplicate values until a non dupe is found
                    # and until left < right 
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        
        return res







                
                
