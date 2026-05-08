class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var left = [Int](repeating: 0, count: n)
        var right = [Int](repeating: 0, count: n)
        var result = [Int](repeating: 0, count: n)

        // Left products
        left[0] = 1
        for i in 1..<n {
            left[i] = left[i - 1] * nums[i - 1]
        }

        // Right products
        right[n - 1] = 1
        for i in stride(from: n - 2, through: 0, by: -1) {
            right[i] = right[i + 1] * nums[i + 1]
        }

        // Combine
        for i in 0..<n {
            result[i] = left[i] * right[i]
        }

        return result
    }
}
