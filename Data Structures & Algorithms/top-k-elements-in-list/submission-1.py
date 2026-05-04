class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
       # build a has map and have COUNT as key, VALUE as value
       # use bucket sort
        hashMap = {}
        frequency = [[] for i in range(len(nums) + 1)]
        
        for item in nums:
            hashMap[item] = 1 + hashMap.get(item, 0)

        for n,c in hashMap.items():
            frequency[c].append(n)

        result = []

        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                result.append(n)
            if len(result) == k:
                return result
             