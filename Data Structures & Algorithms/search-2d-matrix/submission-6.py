class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS = len(matrix)
        COLS = len(matrix[0])
        L = 0
        R = ROWS * COLS - 1
        
        while L <= R:
            middle = (L + R) // 2

            row = middle // COLS
            col = middle % COLS

            if target > matrix[row][col]:
                L = middle + 1
                
            elif target < matrix[row][col]:
                R = middle - 1
                
            else:
                return True
        
        return False
        