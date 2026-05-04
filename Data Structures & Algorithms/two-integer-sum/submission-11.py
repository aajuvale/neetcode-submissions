class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       # how to solve? use hash map to store values after subtracting from target
       hashMap = {}

       index = 0
       for item in nums:
            # nums[i] + nums[j] == target is the same as target - nums[i] == nums[j]
            subValue = target - item
            if subValue in hashMap:
                return [hashMap.get(subValue), index]
            hashMap[item] = index
            index += 1
