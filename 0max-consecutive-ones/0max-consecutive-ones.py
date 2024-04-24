class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count= max_count = 0
        for num in nums:
            if num == 0:
                count = 0
            else:
                count += 1
                max_count = max(count, max_count)      
        return max_count
        