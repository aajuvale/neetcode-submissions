class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # hashMap = {}

        # index = 1
        # for num in numbers:
        #     hashMap[num] = index
        #     index += 1
         
        # for num, index in hashMap.items():

        #     if target - num in hashMap:
                
        #         if num < (target - num):
        #             return [hashMap[num], hashMap[target - num]]
        #         elif num > (target - num):
        #             return [hashMap[target - num], hashMap[num]]

        # how to solve??? two pointer question, index is based with 1 NOT 0


        left = 0
        right = len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right] #totaling teh numbers at the current

            # This code works because it is sorted in non decreasing order already
            # if the sum is greater than target, shift the right pointer to the left 1
            # if the sum is lower than the target, shift the left pointer to the right 1
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left + 1, right + 1] # + 1 is to account for 0 based indexing

    