import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval[0])
        min_heap = [intervals[0][1]]

        for start, end in intervals[1:]:
            if start >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

        return len(min_heap)
