from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last_end = merged[-1][1]

            if start <= last_end:
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged
