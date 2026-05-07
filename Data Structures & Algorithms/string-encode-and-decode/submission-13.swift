class Solution {

    func encode(_ strs: [String]) -> String {
        var encodedStr = ""
        for str in strs {
            encodedStr += String(str.count) + "#" + str
        }
        return encodedStr
    }

    func decode(_ str: String) -> [String] {
        if str.isEmpty {
            return []
        }
        var returnArr = [String]()
        var currentStr = ""
        var arrayStr = Array(str)
        var i = 0
        var j = 0

        while i < arrayStr.count {
            j = i
            while String(arrayStr[j]) != "#" {
                j += 1
            }

            let wordLen = Int(String(arrayStr[i..<j])) ?? 0
            let actualWord = String(arrayStr[j+1..<j+1+wordLen])

            returnArr.append(actualWord)
            i = j + 1 + wordLen
        }
        return returnArr
    }
}
