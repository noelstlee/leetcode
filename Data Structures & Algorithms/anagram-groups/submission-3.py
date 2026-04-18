class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count each letter for word elements in list
        # the count tuple of each word elements will be the key of our dictionary
        # any word elmement in strs list with same count will be appended to our hash map dict
        res = defaultdict(list) # we are initializing with list for edge cases
        for s in strs:
            # intialize count list which will later be converted into tuple to act as key values
            count = [0] * 26 # 26 letters in alphabet
            for c in s:
                # count the letters using ascii
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
