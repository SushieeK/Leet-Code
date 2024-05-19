# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         ans =[]
#         for i in range(len(nums)):
#             ans.append(nums[nums[i]])
#         return ans

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[i] for i in nums]




        