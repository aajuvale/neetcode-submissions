class Solution:
    
    def encode(self, strs: List[str]) -> str:
        #encode is putting everything together into ONE string as output
        stringHold = ""
        for item in strs:
            stringHold += item
            stringHold += "😃"

        return stringHold        

    def decode(self, s: str) -> List[str]:
        print(s)
        returnedList = []
        originalString = ""
        for item in s:
            if item != "😃":
                originalString += item
            if item == "😃":
                returnedList.append(originalString)
                originalString = ""

        return returnedList