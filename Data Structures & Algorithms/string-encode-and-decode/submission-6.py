class Solution:
    
    def encode(self, strs: List[str]) -> str:
        #encode is putting everything together into ONE string as output
        stringHold = ""
        for item in strs:
            stringHold += str(len(item))
            stringHold += "#"
            stringHold += item
            

        return stringHold        

    def decode(self, s: str) -> List[str]:
        # print(s)
        # returnedList = []
        # originalString = ""
        # for item in s:
        #     if item != "#":
        #         originalString += item
        #     if item == "#":
        #         returnedList.append(originalString)
        #         originalString = ""

        # return returnedList
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res