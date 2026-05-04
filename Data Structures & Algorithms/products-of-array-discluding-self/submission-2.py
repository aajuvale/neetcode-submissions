class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        # how to solve?
        # multiply every number that is not i

        hashMap = {}  # {} means dict means dict {} means dict


        index = 0
        for i in nums:
            hashMap[index] = i 
            index += 1

        secondList = []

        for index, val in hashMap.items():
            hashMap[index] = 1
            result = 1 
            indOne = 0
            while indOne < len(hashMap):
                result *= hashMap[indOne]
                indOne += 1
            

            hashMap[index] = val
            
            secondList.append(result)
           
        
        return secondList