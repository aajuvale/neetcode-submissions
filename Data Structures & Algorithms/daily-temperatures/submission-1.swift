class Solution {
    func dailyTemperatures(_ temperatures: [Int]) -> [Int] {
        var stack = [(Int, Int)]()
        var result = Array(repeating: 0, count: temperatures.count)

        for (idx, temp) in temperatures.enumerated() {
            while let (lastTemp, lastIdx) = stack.last, lastTemp < temp {
                stack.removeLast()
                result[lastIdx] = idx - lastIdx
            }
            stack.append((temp, idx))
        }

        return result
    }
}
