class Solution:
    def employeeFreeTime(self, schedule):
        intervals = [interval for employee in schedule for interval in employee]
        intervals.sort(key=lambda interval: interval.start)

        free_time = []
        merged_end = intervals[0].end

        for interval in intervals[1:]:
            if interval.start > merged_end:
                free_time.append(Interval(merged_end, interval.start))

            merged_end = max(merged_end, interval.end)

        return free_time
