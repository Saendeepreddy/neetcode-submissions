class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        c=0
        if 0 in nums:
            for i in nums:
                if i==0:
                    c+=1
        if c==1:
            res=[0]*len(nums)
            for i in range(len(nums)):
                if nums[i]==0:
                    index=i
                    continue
                else:
                    prod*=nums[i]
            res[index]=prod
            return res                          
        elif c>1:
            return [0]*len(nums)           
        else:            
            prod=1
            for i in nums:
                prod*=i
            res=[]    
            for i in range(len(nums)):
                res.append(prod//nums[i])
            return res    
            