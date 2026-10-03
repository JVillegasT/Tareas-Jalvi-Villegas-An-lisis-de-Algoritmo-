class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        kept = 0
        last_end = float("-inf")
        for start, end in intervals:
            if start >= last_end:
                kept += 1
                last_end = end
        return len(intervals) - kept
