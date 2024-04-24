class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num))%2 == 0:
                count += 1
        return count 
    
    
    
# initialize a counter to keep track of the number of even digits
# for each number in the list, convert it to string and find the length - if count of digits is even, inceremt count by 1 
# and do it so on, after parsing through entire list we get the number of even numbers in list
                    
                
        