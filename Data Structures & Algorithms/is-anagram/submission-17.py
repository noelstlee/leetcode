class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        wordCount = defaultdict(int) # key: word, value: count
        for word in s:
            wordCount[word] += 1

        for letter in t:
            if letter in wordCount:
                wordCount[letter] -= 1

        for key, value in wordCount.items():
            if value != 0:
                return False
        
        return True
        