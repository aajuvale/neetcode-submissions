class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        var (L, R) = (0, numbers.count - 1)

        while L <= R {
            var currentTotal = numbers[L] + numbers[R]

            if currentTotal < target {
                L += 1
            } else if currentTotal > target {
                R -= 1
            } else {
                return [L + 1, R + 1]
            }
        }

        return []
    }
}
