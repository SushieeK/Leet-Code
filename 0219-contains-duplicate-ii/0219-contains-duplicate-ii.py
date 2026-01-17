class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False


 


        # we can put counter, or not needed here it is n2 complexity
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n): 
        #         if nums[j] == nums[i] and abs(i-j)<=k:
        #             return True
        # return False
        