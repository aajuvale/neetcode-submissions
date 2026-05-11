class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        let setVer = Set(nums)
        var longest = 0

        for val in setVer {
            if !setVer.contains(val - 1) {
                var length = 0
                while setVer.contains(val + length) {
                    length += 1
                }
                longest = max(length, longest)
            }
        }

        return longest
    }
}
