class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        # How to solve? create hashmaps for s and t and store the count of each variable as the value and key is character
        # count each character, key is character, value is the count
        # 

        # LENGTH OF string is len(s)
        if len(s) != len(t):
            return False

        hashMapS = {}
        hashMapT = {}

        sList = set()
        
        for c in s:
            sCount = 1
            if c in sList:
                sCount += 1
                # hashMapS[c] = sCount
            sList.add(c)
            hashMapS[c] = sCount
        
        tList = set()
       
        for c in t:
            tCount = 1
            if c in tList:
                tCount += 1
               
            tList.add(c)
            hashMapT[c] = tCount

        # for char in sList:
        #     # hashMapS.add([char, count(char)])
        #     hashMapS[char] = sCount
        
        # for char in tList:
        #     hashMapT[char] = tCount
        print(hashMapS)
        print(hashMapT)
        for key, value in hashMapS.items():
            if hashMapS[key] != hashMapT.get(key, 0):
                return False
                # if value in hashMapT:
                #     # print(hashMapT[key])
                    # return True
        
        return True
