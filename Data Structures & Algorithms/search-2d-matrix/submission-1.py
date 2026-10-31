class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we are given an m x n 2d matrix and an integer target 
        # each row in the matrix is in ascending order 
        # the first integer of every row is greater than the last integer of the prev row
        # return true if the target is in the matrix, false if not 

        # sol should be in O(log(m*n))

        # apply binary search to find the correct row that target is in, if not 
        # found return False

        # when applying binary search we still need to check all rows when we have found
        # a row that may contain our target
        n = len(matrix[0])

        left, right = 0, len(matrix) - 1

        index_last_seen = -1

        while left <= right: 
            mid = (left + right) // 2

            if matrix[mid][n-1] >= target:
                index_last_seen = mid
                right = mid - 1
            else:
                left = mid + 1
        
        if index_last_seen == -1:
            return False

        # found the row that target may be in, apply binary search 

        left, right = 0, n - 1
        while left <= right:
            mid = (left+right) // 2
            if matrix[index_last_seen][mid] == target:
                return True
            if matrix[index_last_seen][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
        
        
            


