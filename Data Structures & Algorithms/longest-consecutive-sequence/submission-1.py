class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        res=0
        for i in nums:
            if i-1 not in s:
                l=0
                while i+l in s:
                    l+=1
                res=max(l,res)    
            
        return res            







        