class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i,n in enumerate(numbers):
            comp=target-n
            if comp in seen:
                return [seen[comp]+1,i+1]
            else:
                seen[n]=i  

