class Solution:
    def trap(self, height: List[int]) -> int:
        # Input: height = [0,2,0,3,1,0,1,3,2,1]
        # the sub arr from [2,0,3] has a trapped amount of 2 
        # the sub arr from [3,1,0,1,3] has a trapped amount of 7
        # cannot trap at index 0 and indicies [8,9] 

        # given a list of non-negative integers height that represent 
        # an elavation map, each value height[i] represents the height of a bar 
        # that has a width of 1 
        
        n = len(height)
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = 0
        max_height = 0
        for i in range(1,n):
            max_height = max(max_height, height[i-1])
            prefix[i] = max_height

        suffix[n-1] = 0
        max_height = 0

        for i in range(n-2, -1,-1):
            max_height = max(max_height, height[i+1])
            suffix[i] = max_height

        area = []
        for i in range(n):
            area.append(min(suffix[i], prefix[i]) - height[i])

        total = 0
        for num in area:
            if num > 0:
                total += num

        return total 



        
        
        