class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var (L, R) = (0, nums.count - 1)
        var currentMin = Int.max

        while L <= R {
            if nums[L] < nums[R] {
                currentMin = min(currentMin, nums[L])
                return currentMin
            }
            let mid = (L + R) / 2
            currentMin = min(currentMin, nums[mid])
            if nums[mid] >= nums[L] {
                L = mid + 1
            } else {
                R = mid - 1
            }
        }
        return currentMin
    }
}
