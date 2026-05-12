class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var L = 0
        var R = nums.count - 1

        while L <= R {
            let midpoint = (L + R) / 2
            if nums[midpoint] > target {
                R = midpoint - 1
            } else if nums[midpoint] < target {
                L = midpoint + 1
            } else {
                return midpoint
            }
        }

        return -1
    }
}
