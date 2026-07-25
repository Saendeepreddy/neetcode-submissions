class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for i in strs:
            res.setdefault("".join(sorted(i)),[]).append(i)
        return list(res.values())