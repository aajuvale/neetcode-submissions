class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var (L , R) = (0, nums.count - 1)

        while L <= R {
            let m = (L + R) / 2
            if nums[m] < target {
                L = m + 1
            } else if nums[m] > target {
                R = m - 1
            } else if nums[m] == target {
                return m
            }
        }

        return -1
    }
}
