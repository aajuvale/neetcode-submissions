class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}

        for idx, val in enumerate(nums):
            if target - val in hashMap:
                if idx <= hashMap.get(target - val, 0):
                    return [idx, hashMap.get(target - val, 0)]
                else:
                    return [hashMap.get(target - val, 0), idx]
            hashMap[val] = idx