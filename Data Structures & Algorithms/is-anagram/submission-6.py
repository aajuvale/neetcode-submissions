class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashS, hashT = {}, {}

        for i in range(len(s)):
            #setting hash maps at the key of the letter of the input, and value is the count of the variable.
            hashS[s[i]] = 1 + hashS.get(s[i], 0) 
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        if hashS == hashT:
            return True
        else:
            return False


        # Misread the instructions, anagrams are not always perfectly reverse ordered
        # arrayS = []
        # arrayT = []

        # arrayS = list(s)

        # arrayT = list(t)
        
        # if len(arrayS) == len(arrayT):
        #     i = 0
        #     # for i in len(arrayS):
        #     while i < len(arrayS):
        #         b = len(arrayT) - 1
        #         # print(b)
        #         # for b in arrayT:
        #         if arrayS[i] == arrayT[b]:
        #             b -= 1
        #             if arrayS[i] == arrayS[len(arrayS) - 1]:
        #                 return True
        #             continue
        #         else: 
        #             return False
                    
        #         i += 1
        # else:
        #     return False


        # This solution mostly works, but it doesn't account for the count of each variable. I think solution may be to just count up the variables in each set.
        # arrayS = []
        # arrayT = []

        # arrayS = list(s)

        # arrayT = list(t)
        # setT = set(arrayT)

        # holdTruth = []

        # # print(len(arrayS) == len(arrayT))
        
        # if len(arrayS) == len(arrayT):
        #     i = 0
        #     # for i in len(arrayS):
        #     while i < len(arrayS):
        #         b = len(arrayT)
        #         # print(b)
        #         while b > 0:
        #             if arrayS[i] in setT:
        #                 holdTruth.append("True")
        #             else:
        #                 holdTruth.append("False")
        #             b -= 1
        #         i += 1
            
        #     i=0
        #     while i < len(holdTruth):
        #         if holdTruth[i] == "True":
        #             if i == len(holdTruth) - 1:
        #                 return True 
        #         else:
        #             return False
        #         i += 1
        # else:
        #     return False



