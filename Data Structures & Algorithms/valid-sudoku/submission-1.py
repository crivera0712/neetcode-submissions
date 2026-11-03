class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # given a 9 x 9 matrix, a matrix is considered a valid board only if:
        # each row contains the digits 1-9 without dupes
        # each column contains the digits 1-9 without dupes
        # each of the nine 3x3 sub matrices of the grid must contain the digits
        # 1 - 9 without dupes

        # step 1:
        # loop through each row in matrix
        # create a set in the outer loop
        # this set will ensure that there are no dupe vals
        for row in board:
            seen = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)

        # step 2:
        # loop through each col in the matrix
        # create a set in the outer loop
        # this set will ensure that there are no dupe vals in the col

        for col in range(len(board[0])):
            seen = set()
            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # step 3:
        # loop through every 3x3 matrix in board
        # create a set to track each sub matrix

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])

        return True
