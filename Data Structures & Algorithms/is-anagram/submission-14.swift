class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {
        var hashMap: [Character: Int] = [:]
        var hashMapTwo = [Character:Int]()

        for i in s {
            hashMap[i, default: 0] += 1
        }

        for i in t {
            hashMapTwo[i, default: 0] += 1
        }

        return hashMap == hashMapTwo
    }
}
