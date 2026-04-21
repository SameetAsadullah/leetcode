from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        offset = ord("a")

        for word in strs:
            counts = [0] * 26

            for char in word:
                counts[ord(char) - offset] += 1

            groups[tuple(counts)].append(word)

        return list(groups.values())
