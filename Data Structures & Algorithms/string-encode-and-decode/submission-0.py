class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            for char in string:
                char = chr(ord(char) + 1)
                encoded_string += char
            encoded_string += "ㅋ" # next string
        return encoded_string

    
    def decode(self, s: str) -> List[str]:
        count = 0
        for char in s:
            if char == "ㅋ":
                count += 1
        total_words = count
        decoded_strs = [""] * total_words
        i = 0
        for char in s:
            if char == "ㅋ":
                i += 1
                continue
            decoded_strs[i] += chr(ord(char) - 1)
        return decoded_strs