class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var (L, R) = (0, nums.count - 1)
        var currentMin = Int.max

        while L <= R {
            if nums[L] < nums[R] {
                currentMin = min(nums[L], currentMin)
                return currentMin
            }
            let m = (L + R) / 2
            currentMin = min(nums[m], currentMin)
            if nums[m] >= nums[L] {
                L = m + 1
            } else {
                R = m - 1
            }
        }

        return currentMin
    }
}
