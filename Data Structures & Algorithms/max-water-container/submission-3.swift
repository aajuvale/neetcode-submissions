class Solution {
    func maxArea(_ heights: [Int]) -> Int {
        var L = 0
        var R = heights.count - 1
        var maxArea = 0

        while L <= R {
            if heights[L] < heights[R] {
                maxArea = max(maxArea, (heights[L] * (R - L)))
                L += 1
            } else if heights[L] > heights[R] {
                maxArea = max(maxArea, (heights[R] * (R - L)))
                R -= 1
            } else {
                maxArea = max(maxArea, (heights[R] * (R - L)))
                L += 1
                R -= 1
            }
        }

        return maxArea
    }
}
