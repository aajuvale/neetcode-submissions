class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping character count to list of anagrams

        for string in strs:
            count = [0] * 26 #for every character in alphabet, a through z

            for character in string:
                count[ord(character) - ord("a")] += 1    # This line ord(c) - ord("a") gets the ascii value of the number to store the count
            

            res[tuple(count)].append(string)
        
        return res.values()