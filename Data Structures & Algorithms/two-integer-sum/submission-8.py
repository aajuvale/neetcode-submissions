class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #inputs: int[] nums, int target, 
        #outputs: i and j such that nums[i] + nums[j] == target and i != j

        
        # for i in range(len(nums)):
        #     j = 0
        #     try:
        #         # print(nums[j])
        #         while nums[i] + nums[j] != target:
        #             j += 1
        #         if i != j:
        #             if j < i:
        #                 return list([j, i])
                    
        #             else:
        #                 return list([i, j])
        #     except IndexError:
        #         break
        #         # continue
        #     # else:
        #     #     continue

        #hash map version
        hashMap = {} #value , index

        for i, n in enumerate(nums):
            diff = target - n #reversing the problem and getting the difference

            # the next lines of code only get executed when the difference is found 
            if diff in hashMap:
                return [hashMap[diff], i]
            
            # Adding the value and index to our hashmap so that it is stored. 
            hashMap[n] = i