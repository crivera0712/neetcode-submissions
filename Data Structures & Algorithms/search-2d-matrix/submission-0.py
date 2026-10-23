class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we are given an m x n 2d matrix and an integer target 
        # each row in the matrix is in ascending order 
        # the first integer of every row is greater than the last integer of the prev row
        # return true if the target is in the matrix, false if not 

        # sol should be in O(log(m*n))

        # how do we know where to start left & right?
        # is target greater than the last integer of a row? 
        m,n = len(matrix), len(matrix[0])

        lo, hi = 0, len(matrix) - 1
        
        first_true = -1

        while lo <= hi:
            middle = (lo + hi) // 2
            if matrix[middle][n-1] >= target:
                first_true = middle
                hi = middle - 1
            else: 
                lo = middle + 1
        
        if first_true == -1:
            return False
        
        left, right = 0, n-1

        while left <= right: 
            mid = (left + right) // 2
            print(mid)
            if matrix[first_true][mid] < target:
                left = mid + 1
            elif matrix[first_true][mid] > target:
                right = mid - 1
            elif matrix[first_true][mid] == target:
                return True

        return False
        
        