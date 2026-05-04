class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #inputs: nums array, int k
        #outputs: the k most frequent elements in the array, i.e. the 2 most frequent elements within the array

        count = {}   #hashmap
        freq = [[] for i in range(len(nums) + 1)]   #frequency array that is the length of the nums list

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        

        results = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                results.append(n)
                if len(results) == k:
                    return results
        # for i in enumerate(nums):
        #     hashMap[nums[i]] = 1 + hashMap.get(i, 0)
        
        # for i, n in hashMap:
        #     maxVal = 0
        #     while hashMap.values[n] > hashMap.values[n - 1]:
        #         maxVal = hashMap.values[n]

        #     print(maxVal)