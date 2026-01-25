class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Append new interval (key change!)
        intervals.append(newInterval)
        
        # If there is zero or one interval, there is nothing to merge - n log n runtime, n - space
        if len(intervals) <= 1:
            return intervals

        # Sort intervals by their start time so potential overlaps are adjacent
        # Sorting runs in O(n log n) time
        intervals.sort(key=lambda i: i[0])
        
        # Initialize the output with the first (earliest-starting) interval
        output = [intervals[0]]
        
        # Iterate over the remaining intervals to merge overlaps
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
             # If the current interval overlaps with the last one in output
            if start <= lastEnd:
                # Merge them by extending the end to the maximum of both
                output[-1][1] = max(lastEnd, end)
            # If there is no overlap with the last merged interval
            else:
                # Add the current interval as a new disjoint interval
                output.append([start, end])
                
        return output





        # # Initialize the result list that will hold the final intervals
        # res = []

        # # Iterate over each interval by index to compare with newInterval
        # for i in range(len(intervals)):
        #     # Case 1: newInterval ends before the current interval starts
        #     # This means newInterval belongs before intervals[i] and will not overlap any later intervals
        #     if newInterval[1] < intervals[i][0]:
        #         # Add the newInterval at its correct position
        #         res.append(newInterval)
        #         # Append all remaining intervals as they are and return
        #         return res + intervals[i:]

        #     # Case 2: newInterval starts after the current interval ends
        #     # This means the current interval is completely before newInterval with no overlap
        #     elif newInterval[0] > intervals[i][1]:
        #         # Copy the current interval into the result
        #         res.append(intervals[i])

        #     # Case 3: intervals overlap with newInterval
        #     # Need to merge by expanding newInterval to cover both
        #     else:
        #         # Update newInterval to be the merged interval of itself and intervals[i]
        #         newInterval = [
        #             min(newInterval[0], intervals[i][0]),
        #             max(newInterval[1], intervals[i][1])
        #         ]

        # # If loop ends, newInterval has not been inserted yet
        # # It should go at the end (possibly merged with previous overlaps)
        # res.append(newInterval)

        # # Return the final merged list
        # return res
