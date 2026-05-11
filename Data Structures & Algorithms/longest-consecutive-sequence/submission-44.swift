class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        var setVer = Set(nums)
        var sequenceCount = 0

        for val in setVer {
            if !setVer.contains(val - 1) {
                var length = 0
                while setVer.contains(val + length) {
                    length += 1
                }
                sequenceCount = max(sequenceCount, length)
            }
        }

        return sequenceCount
    }
}
