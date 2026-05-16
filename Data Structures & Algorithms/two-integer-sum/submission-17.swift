class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var hashMap: [Int: Int] = [:]

        for (idx, val) in nums.enumerated() {
            if let currentVal = hashMap[target - val] {
                if idx < currentVal {
                    return [idx, currentVal]
                } else {
                    return [currentVal, idx]
                }
                
            }
            hashMap[val] = idx
        }

        return []
    }
}
