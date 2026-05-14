class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var setS = Set<Character>()
        var L = 0
        let arrayS = Array(s)
        var res = 0

        for R in 0..<arrayS.count {
            while setS.contains(arrayS[R]) {
                setS.remove(arrayS[L])
                L += 1
            }
            setS.insert(arrayS[R])
            res = max(res, R - L + 1)
        }

        return res
    }
}
