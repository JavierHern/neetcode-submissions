class Solution:

    def encode(self, strs: List[str]) -> str:
        full_word = ""
        for word in strs:
            full_word += str(len(word)) + "#" + word
        return full_word


    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1+ length])
            i = j + 1 + length
        return res