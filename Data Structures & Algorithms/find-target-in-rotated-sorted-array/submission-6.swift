class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var (L, R) = (0, nums.count - 1)

        while L <= R {
            let mid = (L + R) / 2

            if target == nums[mid] {
                return mid
            }
            
            if nums[mid] >= nums[L] {
                if target > nums[mid] || target < nums[L] {
                    L = mid + 1
                } else {
                    R = mid - 1
                }
            } else {
                if target < nums[mid] || target > nums[R] {
                    R = mid - 1
                } else {
                    L = mid + 1
                }
            }
        }
        return -1
    }
}
