class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] = nums[i-1]+nums[i]
            i =i+1
        return nums   
            
        
# start working from 1 , as oth position doesnt need any change.        
        
        
        
        
        