class Solution {

    func pruneNonAlphanum(_ input: String) -> String {
        var returnVal = ""

        for char in input {
            if char.isNumber || char.isLetter {
                returnVal += String(char).lowercased()
            }
        }

        return returnVal
    }

    func isPalindrome(_ s: String) -> Bool {
        var newS = pruneNonAlphanum(s)
        return newS == String(newS.reversed())
    }
}
