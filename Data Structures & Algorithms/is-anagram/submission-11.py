class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMapS = {}
        # char
        for idx, val in enumerate(s):
            hashMapS[val] = hashMapS.get(val, 0) + 1


        hashMapT = {}
        for idx, val in enumerate(t):
            hashMapT[val] = hashMapT.get(val, 0) + 1

        return hashMapS == hashMapT 