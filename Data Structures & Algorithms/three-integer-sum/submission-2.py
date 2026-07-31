class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0 and [nums[i],nums[l],nums[r]] not in res:
                    res.append([nums[i],nums[l],nums[r]])
                    r-=1
                    l+=1
                elif nums[i]+nums[r]+nums[l]>0:
                    r-=1
                else:
                    l+=1     
        return res            

                    

