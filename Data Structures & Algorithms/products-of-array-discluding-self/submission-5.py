class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        # how to solve?
        # multiply every number that is not i

        hashMap = {}  # {} means dict means dict {} means dict

        index = 0
        for i in nums:
            hashMap[index] = i 
            index += 1

        numList = []

        for index, val in hashMap.items():
            hashMap[index] = 1    # setting every number at the current index to be 1

            result = 1  # setting result to be 1 so that it can be multiplied with every variable
            
            # iterating through using indOne and multiplying each value
            indOne = 0
            while indOne < len(hashMap):
                result *= hashMap[indOne]
                indOne += 1
            

            hashMap[index] = val     # resetting the value so that it isn't one at the end of the loop    
            
            numList.append(result)   # appending the result to the returned numList
           
        
        return numList