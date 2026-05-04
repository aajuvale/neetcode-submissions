class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        # how to solve?
        # multiply every number that is not i

        # hashMap = {}  # {} means dict means dict {} means dict

        # index = 0
        # for i in nums:
        #     hashMap[index] = i 
        #     index += 1

        # numList = []

        # for index, val in hashMap.items():
        #     hashMap[index] = 1    # setting every number at the current index to be 1

        #     result = 1  # setting result to be 1 so that it can be multiplied with every variable
            
        #     # iterating through using indOne and multiplying each value
        #     indOne = 0
        #     while indOne < len(hashMap):
        #         result *= hashMap[indOne]
        #         indOne += 1
            

        #     hashMap[index] = val     # resetting the value so that it isn't one at the end of the loop    
            
        #     numList.append(result)   # appending the result to the returned numList
           
        
        # return numList

        # more efficient solution

        results = [1] * (len(nums)) #creating and initializing a result list that is the length of the input array nums
    

        prefix = 1 #declaring and initiliazing variable prefix (variables before input)
        for i in range(len(nums)):
            results[i] = prefix 
            prefix *= nums[i]  # Multiplying nums[i] to prefix 
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):  #for loop that iterates through the length of nums in descending order
            results[i] *= postfix   # Multiplying postfix to results[i]
            postfix *= nums[i]      # multiplying nums to postfix
        
        return results