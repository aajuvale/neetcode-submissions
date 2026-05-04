class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       # how to solve? use hash map to store values after subtracting from target, key is character, value is index
       # Iterate through for loop and reverse the problem
       # return when subValue is found within the hashmap
       hashMap = {}

       index = 0
       for item in nums:
            # nums[i] + nums[j] == target is the same as target - nums[i] == nums[j]
            subValue = target - item
            if subValue in hashMap:
                return [hashMap[subValue], index]
            hashMap[item] = index
            index += 1
