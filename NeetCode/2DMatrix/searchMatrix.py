from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #get the dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])
        
        #binary search to find the row
        top, bot = 0, ROWS-1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        #we have crossed out all the rows and the target is not found
        if not (top <= bot):
            return False
        
        #move onto second binary search
        row = (top + bot) // 2 #this is the row we found with the target value
        l,r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

row1 = [1,3,5,7]
row2 = [10,11,16,20]
row3 = [23,30,34,60]
matrix = [row1, row2, row3]
solution = Solution()
print(solution.searchMatrix(matrix, 3)) # True