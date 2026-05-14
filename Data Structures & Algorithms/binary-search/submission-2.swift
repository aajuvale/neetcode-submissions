class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var (L, R) = (0, nums.count - 1)

        while L <= R {
            let midPoint = (L + R) / 2
            if nums[midPoint] < target {
                L = midPoint + 1
            } else if nums[midPoint] > target {
                R = midPoint - 1
            } else {
                return midPoint
            }
        }

        return -1
    }
}
