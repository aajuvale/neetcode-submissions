class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        if s.count != t.count {
            return false
        }

        var hashMap = [Character: Int]()

        for i in s {
            hashMap[i, default: 0] += 1
        }

        var hashMapTwo = [Character: Int]()

        for i in t {
            hashMapTwo[i, default: 0] += 1
        }

        return hashMap == hashMapTwo
    }
}
