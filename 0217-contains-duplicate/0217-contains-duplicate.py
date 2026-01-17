class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n complexitry, space is also n for hash set
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False 
        
        # thjis takes n log n 
        # nums.sort()  # O(n log n)
        # for i in range(1, len(nums)):  # O(n)
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        # we can put counter, or not needed here it is n2 complexity
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n): 
        #         if nums[j] == nums[i]:
        #             return True
        # return False
        