class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Customer_wealth=[]
        for customer_accounts in accounts:
            individual_wealth= sum(customer_accounts)
            Customer_wealth.append(individual_wealth)
        return max(Customer_wealth)  

            
        
        
        
        
       