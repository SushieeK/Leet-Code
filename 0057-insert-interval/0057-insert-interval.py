class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Append new interval (key change!)
        intervals.append(newInterval)
        
        # Now EXACT merge logic/variables
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda i: i[0])  # Same!
        
        output = [intervals[0]]  # Same var!
        
        for start, end in intervals[1:]:  # Same vars!
            lastEnd = output[-1][1]  # Same var!
            
            if start <= lastEnd:  # Same logic!
                output[-1][1] = max(lastEnd, end)  # Same!
            else:
                output.append([start, end])  # Same!
                
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
