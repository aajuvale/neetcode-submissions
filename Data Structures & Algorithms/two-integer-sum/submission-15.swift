class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var hashMap: [Int:Int] = [:]
        for (idx, val) in nums.enumerated() {
            var diff = target - val
            if let diffValue = hashMap[target-val] {
                if idx < diffValue {
                    return [idx, diffValue]
                } else {
                    return [diffValue, idx]
                }
            }
            hashMap[val] = idx
        }

        return []
    }
}
