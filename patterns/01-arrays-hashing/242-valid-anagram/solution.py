# Approach 1: Hash Map
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for char in t:
            if char not in counts:
                return False

            counts[char] -= 1

            if counts[char] < 0:
                return False

        return True


# Approach 2: Frequency Array
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        offset = ord("a")

        for i in range(len(s)):
            counts[ord(s[i]) - offset] += 1
            counts[ord(t[i]) - offset] -= 1

        for count in counts:
            if count != 0:
                return False

        return True
