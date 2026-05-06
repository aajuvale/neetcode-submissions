class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let arrayS = Array(s.lowercased().filter{$0.isLetter || $0.isNumber})
        var (L, R) = (0, arrayS.count - 1)

        while L <= R {
            if (arrayS[L] == arrayS[R]) {
                L += 1
                R -= 1
            } else {
                return false
            }
        }

        return true
    }
}
