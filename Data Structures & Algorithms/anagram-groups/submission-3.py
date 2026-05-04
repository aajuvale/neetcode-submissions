class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #inputs: array of strings: str
        #outputs: list that contains sublist with every anagram.

        # if using hash map, what are keys? what are values?
        # keys are characters, values are indices?

        results = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            results[tuple(count)].append(s)
        return results.values()
