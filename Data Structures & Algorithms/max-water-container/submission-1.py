class Solution:
    def maxArea(self, heights: List[int]) -> int:
#         Input: height = [1,7,2,5,4,7,3,6]

#         Output: 36
        left = 0
        right = len(heights) - 1
        # width = right - left
        # minVal = minimum of left and right
        # area
        maximumA = 0
        maxW = 0
        result = 0
        while left < right:
            maxW = right - left
            maximumA = maxW * min(heights[left], heights[right])
            result = max(result, maximumA)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        

        
        return result