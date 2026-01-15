class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            # adding the value in key, and index in value so thata it can be found
            if diff in map:
                return map[diff],i
            # adding the elemnt to the map after, so that it doesnot self count twice     
            map[nums[i]] =i






        # Bruteforce n2 time 
        # n = len(nums)
        # result = []
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i]+ nums[j] == target:
        #             result.append(i)
        #             result.append(j)
        #             return result
        # return result
        



















        # numToIndex = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in numToIndex:
        #         return numToIndex[complement],i
        #     numToIndex[nums[i]] =i
            
        