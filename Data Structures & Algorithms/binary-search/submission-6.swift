class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var (L, R) = (0, nums.count - 1)

        while L <= R {
            var mid = (L + R) / 2

            if nums[mid] < target {
                L = mid + 1
            } else if nums[mid] > target {
                R = mid - 1
            } else {
                return mid
            }
        }
        return -1
    }
}
