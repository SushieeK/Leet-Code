class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, Current_Number in enumerate(nums):
            if leftsum == (S - leftsum - Current_Number):
                return i
            leftsum += Current_Number
        return -1

