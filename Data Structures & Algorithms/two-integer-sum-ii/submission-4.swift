class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        var (L, R) = (0, numbers.count - 1)

        while L <= R {
            var currentSum = numbers[L] + numbers[R]
            if currentSum == target {
                return [L + 1, R + 1]
            } else if currentSum < target {
                L += 1
            } else if currentSum > target {
                R -= 1
            }
        }
        return []
    }
}
