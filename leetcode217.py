class Solution:
    def containsDuplicate(self, nums: Tuple[int]) -> bool:
        for i, n in enumerate(nums):
            if n in nums[i+1:]:
                return True
        return False

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
'''
