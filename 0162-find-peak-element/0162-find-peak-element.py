class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: 
            return 0
        if nums[0] > nums[1]: 
            return 0
        if nums[n-1] > nums[n-2]: 
            return n-1
        low, high = 1, n-2
        while (low <= high):
            mid = (low+high)//2
            if (nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]):
                return mid
            elif(nums[mid] > nums[mid-1]):
                low = mid +1
            else:
                high = mid - 1
        return -1





        #Bruteforce- n time
        # low = 0
        # high = len(nums) - 1
        # mid = (low + high) // 2
        # n = len(nums)
        # for i in range(n):
        #     left = (i ==0) or (nums[i] > nums[i-1])
        #     right = ( i ==n-1) or (nums[i] > nums[i+1])
        #     if left and right:
        #         return i 
        # return -1


        