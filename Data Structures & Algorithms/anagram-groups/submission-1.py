class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        dictionary = {}
        for s in strs:
            ordered = ''.join(sorted(s))
            if ordered not in dictionary:
                dictionary[ordered] = [s]
            else:
                dictionary[ordered].append(s)

        for key in dictionary:
            output.append(dictionary[key])
        return output