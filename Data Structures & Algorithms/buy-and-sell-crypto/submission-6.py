class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        minprice=prices[0]
        for i in prices:
            if i<minprice:
                minprice=i
            res=max(res,i-minprice)
        return res                 
