class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # given an unsorted list of integers, form a container using
        # two heights that contain the maximum amount of water that a 
        # container can store 
        # heights[i] represents the height of the ith bar
        # we can choose any two bars from the container 
        # max_water = height * width 
        # width can be found be substracting the two different positions in the
        # list
        if not heights:
            return 0 
        
        left, right = 0, len(heights) - 1
        n = len(heights)
        area = -1
        while left < right:

            height = min(heights[left], heights[right])
            check = (right - left) * height
            area = max(area, check)

            
            if heights[left] < heights[right]:
                left +=1
            else: 
                right -= 1
        
        return area


        