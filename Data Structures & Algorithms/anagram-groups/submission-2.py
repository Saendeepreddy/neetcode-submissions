class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        for i in strs:
            temp=[]
            if i in res:
                continue
            for j in strs:
                if sorted(i)==sorted(j):
                    temp.append(j)
            if temp not in res:
                res.append(temp)
        return res           



        