class Solution {
    func findMin(_ nums: [Int]) -> Int {
        var (L, R) = (0, nums.count - 1)
        var currMin = Int.max

        while L <= R {
            if nums[L] < nums[R] {
                currMin = min(nums[L], currMin)
                break
            }
            let m = (L + R) / 2
            currMin = min(nums[m], currMin)
            if nums[m] >= nums[L] {
                L = m + 1
            } else {
                R = m - 1
            }
        }

        return currMin
    }
}
