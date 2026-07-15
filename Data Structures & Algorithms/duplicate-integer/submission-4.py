from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = defaultdict(int)
        
        for i in nums:
            hmap[i] += 1        # Populate the counter map
            if hmap[i] > 1:     # Check if a duplicate is found
                return True
                
        return False   

        