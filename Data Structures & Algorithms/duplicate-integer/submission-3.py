class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myhashset=set()

        for n in nums:
            if n in myhashset:
                return True
            myhashset.add(n)
        return False 

