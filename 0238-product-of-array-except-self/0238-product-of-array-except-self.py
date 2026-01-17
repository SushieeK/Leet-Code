class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # store the ans directly, instaed of prefix and sufix arra
        ans = [1] * n
        for i in range (1, n):
            ans[i] = ans[i-1]*nums[i-1]
        sufix = 1
        for i in range (n-2, -1,-1):
            sufix = sufix*nums[i+1]
            ans[i] = ans[i]*sufix

        return ans
        
        
        
        # this way, the time complexity is 3n which si order of n , but space is two extra rrays of length n 
        # prefix = [1] * n
        # sufix = [1] * n
        # ans = [1] * n
        # for i in range (1, n):
        #     prefix[i] = prefix[i-1]*nums[i-1]
        # for i in range (n-2, -1,-1):
        #     sufix[i] = sufix[i+1]*nums[i+1]
        # for i in range(n):
        #     ans[i] = prefix[i]*sufix[i]
        # return ans



        