class Solution {
    func twoSum(_ numbers: [Int], _ target: Int) -> [Int] {
        var (L, R) = (0, numbers.count - 1)
        var setNumbers = Set(numbers)

        while L <= R {
            if numbers[L] + numbers[R] == target {
                return [L + 1, R + 1]
            } else if !setNumbers.contains(target - numbers[L]) {
                L += 1
            } else if !setNumbers.contains(target - numbers[R]) {
                R -= 1
            }
        }
        return []
    }
}
