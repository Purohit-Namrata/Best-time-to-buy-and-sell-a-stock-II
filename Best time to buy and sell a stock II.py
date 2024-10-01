from typing import List
class Solution:
    def maxprofit(self,prices:List[int])->int:
        i=0
        buy=prices[0]
        sell=prices[0]
        profit=0
        n=len(prices)

        while(i<n-1):
            #look where to buy
            while i<n-1 and prices[i]>=prices[i+1]:
                i+=1
            buy=prices[i]

            #look where to sell
            while i<n-1 and prices[i]<=prices[i+1]:
                i+=1
            sell=prices[i]
            profit+=(sell-buy)
        return profit       
    
s=Solution()
print("Maximum profit ",s.maxprofit([7,1,5,3,6,4]))