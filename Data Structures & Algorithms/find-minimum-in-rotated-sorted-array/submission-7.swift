class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var (L, R) = (0, nums.count - 1)
        var minVal = Int.max

        while L <= R {
            if nums[L] < nums[R] {
                minVal = min(minVal, nums[L])
                return minVal
            }
            let mid = (L + R) / 2
            minVal = min(minVal, nums[mid])
            if nums[mid] >= nums[L] {
                L = mid + 1
            } else {
                R = mid - 1
            }
        }

        return minVal
    }
}
