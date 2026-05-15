class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var (L, R) = (0, nums.count - 1)
        var minVal = Int.max
        // var res = Array(repeating: 0, count: nums.count)
        while L <= R {
            if nums[L] < nums[R] {
                minVal = min(nums[L], minVal)
                break
            }
            let mid = (L + R) / 2
            minVal = min(nums[mid], minVal)
            if nums[mid] >= nums[L] {
                L = mid + 1
            } else {
                R = mid - 1
            }
        }

        return minVal
    }
}
