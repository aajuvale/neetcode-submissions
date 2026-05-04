class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        removedExtra = ""
        removedList = {}
        s = s.lower()  # setting everything to lower case
        index = 0
        for char in s:
            # checking if the character at the value is alphanumeric
            if char.isalnum():
                removedExtra += char          #adding the values to string
                removedList[index] = char     #adding the values to hashMap removedList with indices attached
                index += 1
        
        reversedString = ""
        for char in range(len(removedList), -1, -1):
            if removedList.get(char - 1) is not None:
                reversedString += str(removedList.get(char - 1))
            print(reversedString)
            
        return removedExtra == reversedString

        