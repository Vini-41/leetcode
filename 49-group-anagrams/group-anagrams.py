from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = defaultdict(list)
        for string in strs:
            a_to_z = [0] * 26
            for char in string:
                index = ord(char) - ord("a")
                a_to_z[index]+= 1
            seen[tuple(a_to_z)].append(string)
        return list(seen.values())