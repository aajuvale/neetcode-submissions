class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        strVer = ""
        for val in digits:
            strVer += str(val)
        
        intVer = int(strVer)
        stringTwo = str(intVer + 1)
        
        res = []
        for s in stringTwo:
            res.append(s)
        
        return res
        