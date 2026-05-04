class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        removedExtra = ""
        removedList = {}
        s = s.lower()  # setting everything to lower case
        index = 0
        for char in s:
            if char.isalnum():
                removedExtra += char
                removedList[index] = char
                index += 1
        
        reversedString = ""
        for char in range(len(removedList), -1, -1):
            if removedList.get(char - 1) is not None:
                reversedString += str(removedList.get(char - 1))
            print(reversedString)
            
        if removedExtra == reversedString:
            return True
        else:
            return False

        # for index in removedList:
        #     print(index)
        #     print(removedList[index])

        #     topSize = len(removedList) - 1
        #     while topSize != index:
        #         if removedList[index] != removedList[topSize] and topSize % 2 == 0:
        #             return False
        #         topSize -= 1
        #     print(topSize)

        print(removedExtra)
             

        