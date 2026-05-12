class Solution {
    func topKFrequent(_ nums: [Int], _ k: Int) -> [Int] {
        var counter: [Int: Int] = [:]

        for val in nums {
            counter[val, default: 0] += 1
        }

        var sortedCounter = counter.sorted { $0.value > $1.value }
        var returnArray = [Int]()
        var idx = 0
        for (key, val) in sortedCounter {
            if idx < k {
                returnArray.append(key)
            } 
            idx += 1
        }

        return returnArray
    }
}
