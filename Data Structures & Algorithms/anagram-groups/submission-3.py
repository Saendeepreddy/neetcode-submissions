class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        curr=[]
        for i in strs:
            if i in curr:
                continue
            temp=[]
            curr.append(i)
            for j in strs:
                if sorted(i)==sorted(j):
                    temp.append(j)
            if temp not in res:
                res.append(temp)
        return res           



        