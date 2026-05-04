class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       hashM = {}
       for idx, val in enumerate(nums):
            missingVal = target - nums[idx]
            if missingVal in hashM:
                missingIdx = hashM.get(missingVal, 0)
                if idx < missingIdx:
                    return [idx, missingIdx]
                if idx >= missingIdx:
                    return [missingIdx, idx]
            hashM[val] = idx



       
